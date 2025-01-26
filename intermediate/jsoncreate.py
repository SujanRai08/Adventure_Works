import json
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
user = User("max",27)
def encode_user(o):
    if isinstance(o,User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("object of type is not json serializable")
    
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def encode_user(o):
        if isinstance(o,User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        else:
            raise TypeError("object of type is not json serializable")

userJson = UserEncoder().encode(user)
print(userJson)

#  encoding to decoding

def decode_user(dct):
    if User.__name__ in dct:
        return user(name = dct["name"], age =dct["age"])
    return dct
user = json.loads(userJson,object_hook=decode_user)
print(type(user))
print(user)
