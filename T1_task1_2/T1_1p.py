# Створити симуляцію роботи пральної машини.
# Це завдання може включати моделювання циклу 
# роботи пральної машини, наприклад, заповнення водою, 
# прання, полоскання та віджимання, з відповідними 
# часовими затримками та станами в симуляції. 

import time

class washingmachine():
    def __init__(stateW):
        stateW.states = ['Запуск', 'Набирання води', 'прання', 'Полоскання', 'Віджимання', 'Повне завершення прання']
        stateW0 = None
    def zapusk(stateW):
        stateW0 = stateW.states[0]
        print(f'Режим - {stateW0}')
        time.sleep(1)
    def plus_water(stateW):
        stateW0 = stateW.states[1]
        print(f'Режим - {stateW0}')
        time.sleep(1)
    def wait(stateW):
        print('Зачекайте...')
        time.sleep(2)
    def prannya_start(stateW):
        stateW0 = stateW.states[2]
        print(f'Режим - Початок {stateW0}')
        time.sleep(1)
    def prannya_stop(stateW):
        stateW0 = stateW.states[2]
        print(f'Режим - Завершення {stateW0}')
        time.sleep(1)
    def poloskannya(stateW):
        stateW0 = stateW.states[3]
        print(f'Режим - {stateW0}')
        time.sleep(1)
    def vidzhym(stateW):
        stateW0 = stateW.states[4]
        print(f'Режим - {stateW0}')
        time.sleep(1)
    def stop(stateW):
        stateW0 = stateW.states[5]
        print(f'Режим - {stateW0}')
        time.sleep(3)
    def rechi(stateW):
        print('Шо? Діставай речі')
washing_machine = washingmachine()
washing_machine.zapusk()
washing_machine.plus_water()
washing_machine.wait()
washing_machine.prannya_start()
washing_machine.prannya_stop()
washing_machine.poloskannya()
washing_machine.vidzhym()
washing_machine.stop()
washing_machine.rechi()
