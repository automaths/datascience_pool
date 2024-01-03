def all_thing_is_obj(thing: any) -> int:
    if (type(thing) == list):
        print("List :", type(thing))
    elif (type(thing) == tuple):
        print("Tuple :", type(thing))
    elif (type(thing) == set):
        print("Set :", type(thing))
    elif (type(thing) == dict):
        print("Dict :", type(thing))
    elif (type(thing) == str):
        print(thing, "is in the kitchen :", type(thing))
    else:
        print("Type not found")
    return (42)


