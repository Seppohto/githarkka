def hello():
    return "Hello World!"

class Person :

    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def __repr__(self):
        return '{' + self.name + ', ' + str(self.age)+ '}'

    # getter method
    def get_name(self):
        return self._name
      
    # setter method
    def set_name(self, x):
        self._name = x
    
    # getter method
    def get_age(self):
        return self._age
      
    # setter method
    def set_age(self, x):
        self._age = x

