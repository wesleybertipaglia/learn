# encapsulation
# public: accessible inside and outside the class
# private: accessible only iside the class
# getter: used to get a private prop
# setter: used to set a private prop

class  Person:
    def __init__(self, name, age, id):
        self.name = name # public
        self.age = age
        self.__id = id # private

    def get_id(self): # getter
        return self.__id
    
    def set_id(self, id): # setter
        self.__id = id

# instances
bea = Person('Bea', 22, '34642348787')
print(bea.get_id())
bea.set_id('2454656')