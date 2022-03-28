class Duck(): # here we implicitly inherit from 'object'
    def __init__(self, param_name):
        self.__hidden_name = param_name # double-underscore is 'name mangling'
    def getName(self): # getter method
        return self.__hidden_name
    def setName(self,new_name): # setter method
        # validate the incoming name
        if(isinstance(new_name, str)):
            self.__hidden_name = new_name
    # we specify the setter then nthe getter
    name = property(getName, setName) # treat 'name' as a property, accessed by methods

if __name__ == '__main__':
    fowl = Duck('howard')
    fowl.setName('Ethel')
    # try to change the __hidden_name
    fowl.__hidden_name = 'changed' # this actually adds an arbitrary new property to the object
    ## use the 'name' property
    fowl.name = 'Timnit'
    print( fowl.getName() )
    # it IS posible to still access the name-mangled value
    print(fowl._Duck__hidden_name)