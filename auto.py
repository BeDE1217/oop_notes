bmw = {
    'model' : 'e46',
    'engine': False,
    'speed' : 0,
    'max_speed': 160
}
fiat = {
    'model': 'tipo',
    'engine': False,
    'speed': 0,
    'max_speed': 240
}
def start_engine(car):
     if not car['engine']:
         car['engine'] = True
         print('Silnik odpalony')
     else:
         print('silnik był juz odpalony!')

def stop_engine(car):
    if car['speed'] == 0:
        car['engine'] == False
        print('Silnik jest zgaszony')
    else:
        print('najpierw zatrzymaj samochód')

def speed_up(car, amount):
    if car['engine']:
        car['speed'] = min(car['speed']+ amount, car['max_speed'])
        print(f'jedziesz z prędkością {car["speed"]}')
    else:
        print('odpal silnik najpierw')
def slow_down(car,amount):
    car['speed'] = max(car['speed'] - amount, 0)
    print(f'jedziesz z prędkoscia {car["speed"]}')



speed_up(bmw,20)
start_engine(bmw)
speed_up(bmw,20)
speed_up(bmw,50)
speed_up(bmw,200)
stop_engine(bmw)
slow_down(bmw,50)
slow_down(bmw,250)
stop_engine(bmw)
