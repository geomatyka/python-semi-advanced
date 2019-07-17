from time import ctime


class CashDesk:

    def __init__(self, manager):
        self.manager = manager
        self.f = open('cash_desk.txt', 'w')

    def new_order(self, order):
        print('BEGIN')
        self.save(order.name + ';' + ctime(order.placing_h))
        self.manager.new_order(order)

    def save(self, mess):
        self.f.write(mess + '\n')

    def __del__(self):
        self.f.close()
