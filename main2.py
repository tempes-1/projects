menu = int(input('welcome \n1)input airport details \n2)input flight details \n3)price plan and profit \n4)clear data \n5)quit \noption:'))

aircraftSpecs = [
    ['Medium Narrow Body', 'Large Narrow Body', 'Medium Wide Body'], # type
    [8,7,5], # running cost per seat per 100km
    [2650, 5600, 4050], # maximum distance
    [180,220, 406], # capacity if all standard seats
    [8,10,14] # minimum first class seats if any
]


def airportDetails():

    ukAirport = input('which uk airport, LPL or BOH:').upper()
    if ukAirport != 'LPL' and ukAirport != 'BOH':
        print('invalid uk airport')
    else:
        print('valid')
        overseasAirport = input('which overseas airport(code): ').upper()
        f = open('airport.csv', 'r')
        for i in f:
            if overseasAirport == i[:3]:
                elements = i.split(',')
                print(elements[1])
                found = True
                break
            else:
                found = False
        if not(found):
            print('invalid overseas code')
        else:
            return ukAirport, overseasAirport
    return '',''
    
def flightDetails():
    normalSeats = 0
    firstClassSeats =0
    print('possible aircraft types : ', aircraftSpecs[0])
    aircraftType = input('enter aircraft type: ').title()
    if aircraftType not in aircraftSpecs[0]:
        print('invalid type')
    else:
        index = aircraftSpecs[0].index(aircraftType)
        firstClassSeats = int(input('number of first class seats: '))
        if firstClassSeats ==0:
            print('invalid')
        else:
            if firstClassSeats < aircraftSpecs[4][index]:
                print('invalid')
            elif firstClassSeats > aircraftSpecs[3][index]:
                print('invalid')
            else:
                normalSeats = aircraftSpecs[3][index] - (firstClassSeats*2)
                return aircraftType, normalSeats, firstClassSeats
    return '', 0, 0

def calculations(fcPrice,stanPrice, line, i):
    if ukAirport == 'LPL':
        airport = 2
    else:
        airport = 3
    flightCostPerSeat = aircraftSpecs[1][i] * int(line[airport])/100
    flightCost = flightCostPerSeat * (firstClassSeats + normalSeats)
    flightIncome = (firstClassSeats*fcPrice) + (normalSeats*stanPrice)
    flightProfit = flightIncome - flightCost
    return flightCostPerSeat, flightCost, flightIncome, round(flightProfit,2)
    





def priceAndProfit(ukAirport, overseasAirport , firstClassSeats , normalSeats , type ):
    if (ukAirport != 'LPL' and ukAirport != 'BOH') or (overseasAirport not in ['JFK','ORY','MAD','AMS','CAI']):
        print('invalid airports')
    else:
        if type not in aircraftSpecs[0]:
            print('invalid aircraft type')
        else:
            if firstClassSeats == 0:
                print('invalid')
            else:

                f = open('airport.csv', 'r')
                index = aircraftSpecs[0].index(type)
                lines = f.readlines()
                for i in range(5):
                    if lines[i][:3] == overseasAirport:
                        line = lines[i][:len(lines[i])-1 if overseasAirport != 'CAI' else len(lines[i])] #searching the csv file for the line which we need and pulling it
                        line = line.split(',')
    
                if ukAirport == 'LPL':
                    if aircraftSpecs[2][index] >= int(line[2]):#comparing max distance and distance between airports 
                        firstPrice = float(input('price for first class seat: '))
                        standardPrice = float(input('price for standard seat: '))
                        a,b,c,d =(calculations(firstPrice, standardPrice, line, index))
                        print(f'flight cost per seat: {a}\nflight cost: {b}\nflight income: {c}\nflight profit: {d}')
                        
                    else:
                        print('invalid')
                    
                else:
                    if aircraftSpecs[2][index] >= int(line[3]):#comparing max distance and distance between airports 
                        
                        firstPrice = float(input('price for first class seat: '))
                        standardPrice = float(input('price for standard seat: '))
                        a,b,c,d =calculations(firstPrice, standardPrice, line, index)
                        print(f'flight cost per seat: {a}\nflight cost: {b}\nflight income: {c}\nflight profit: {d}')
                    else:
                        print('invalid')
                
def clear():
    ukAirport =''
    pverseasairport = ''
    type = ''
    normalSeats= 0
    firstClassSeats = 0
    





while menu !=5:
    if menu == 1:
        ukAirport, overseasAirport =airportDetails()

    elif menu ==2:
        
        type, normalSeats, firstClassSeats = flightDetails()
        
    elif menu == 3:
        priceAndProfit(ukAirport, overseasAirport,firstClassSeats,normalSeats, type)
    elif menu == 4:
        clear()
    else:
        print('invalid option')

    menu = int(input('welcome \n1)input airport details \n2)input flight details \n3)price plan and profit \n4)clear data \n5)quit \noption:'))

print('program has ended')