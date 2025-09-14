# a = {"John","Jake", "Eric"}
# b = {"John", "Jill"}

# print(a.intersection(b))
# print(b.intersection(a))
# print(a.symmetric_difference(b))
# print(b.symmetric_difference(a))
# print(a.difference(b))
# print(b.difference(a))
# print(a.union(b))

print(set("my name is mujeeb and mujeeb is my name"))
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
thisset.add("orange")

set2 = {"pineapple","mango", "papaya"}
thisset.update(set2)
print(thisset)
# thisset.remove("banana")
thisset.discard("banana")
x = thisset.pop()

thisset.clear()
del thisset
