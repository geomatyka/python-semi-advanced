class Optional:

    def __init__(self, element):
        self.element = element

    def get(self):
        if self.element is not None:
            return self.element
        raise ElementNotPresent

    def is_present(self):
        return self.element is not None

    def map(self, function):
        if self.is_present():
            self.element = function(self.element)

    def filter(self, function):
        if self.is_present():
            if not function(self.element):
                self.element = None

    def if_present(self, function):
        if self.is_present():
            function(self.element)


class ElementNotPresent(Exception):
    pass
