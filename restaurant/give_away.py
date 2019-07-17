from time import time, sleep, ctime


class GiveAway:

    def __init__(self, manager):
        self.manager = manager
        self.f = open('give_away.txt', 'w')

    def call_customer(self, order):
        print('Wydawka...', end='', flush=True)
        sleep(1)
        print('Wydawka')
        self.customer_collected_order(order)

    def customer_collected_order(self, order):
        order.pickup_h = time()
        self.save(order.name + ';' + ctime(order.pickup_h))
        self.manager.customer_collected_order(order)

    def save(self, mess):
        self.f.write(mess + '\n')

    def __del__(self):
        self.f.close()
