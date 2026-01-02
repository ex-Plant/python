

myDictionary = {
    "name": "Konrad",
    "age": "9"
}

get_age = lambda name: myDictionary.get(name)
get_age = lambda name: myDictionary.get(name, 'not found')
print(get_age('name')) # Konrad
print(get_age('not found test ')) # not found