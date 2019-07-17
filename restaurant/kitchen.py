from time import sleep, time, ctime

class Kitchen:

    def __init__(self, manager):
        self.manager = manager
        self.f = open('kitchen.txt', 'w')

    def prepare_meal(self, order):
        print('Kuchnia...', end='', flush=True)
        sleep(1)
        print('Kuchnia')
        self.meal_ready(order)

    def meal_ready(self, order):
        order.completion_h = time()
        self.save(order.name+ ';' + ctime(order.completion_h))
        self.manager.meal_ready(order)

    def save(self, mess):
        self.f.write(mess + '\n')

    def __del__(self):
        self.f.close()
