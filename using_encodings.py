# we need to be able to encode a class representing a name (str) and a cost (float)
import json

class Item: # this implicitly inherits from object
    '''
    This class encapsulates items that havev a name and a cost
    name is a string, cost is a positive float
    '''
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name 
    @property
    def cost(self):
        return self.__cost
    @cost.setter
    def cost(self, new_cost):
        self.__cost = new_cost 

# class to encode our 'Item' as json
class Itemencoder(json.JSONEncoder):
    def default(self, obj): # override the built-in 'default' of JSONEncoder
        # check we have an 'item' instance
        if isinstance(obj, Item):
            return obj.__dict__ # return our 'Item' as a dict
        else:
            # if the type is NOT an 'Item', just use default encoding
            return json.JSONEncoder.default(self, obj)

if __name__ == '__main__':
    # can we just encode our class?
    z = Item('Zoe', 28)
    # z_j = json.dumps(z) # fails
    # z_j = json.dumps(z.__dict__) # just use the class dictionary
    z_j = json.dumps(z, cls=Itemencoder) # use our custom encoder class
    print(z_j)