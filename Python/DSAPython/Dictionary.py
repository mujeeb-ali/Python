thisdic = {
  "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year" : 2020
}

print(thisdic)
print(len(thisdic))
print(type(thisdic))
x = thisdic.get("model")
y = thisdic.keys()
print(x)
print(y)

x = thisdic.values()
print(x)

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

phomebook = {
    "John" : [938477566, 93123566],
    "Jack" : 938377264,
    "Jill" : 947662781,
    12 : 93243435344
}

print(phomebook[12])

