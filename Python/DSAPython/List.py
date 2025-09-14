# myList = []
# myList.append(1)
# myList.append(2)
# myList.append(3)
# myList.append(4)
# print(myList)
# print(myList[0])
# print(myList[1])
# print(myList[2])
# print(myList[3])

# for i in myList:
#     print(i ,end = " ")


# myList.append(5)    
# print()
# print(myList)
# print(len(myList))
# myList.remove(5)
# print(myList)
# myList.clear()
# print(myList)
# mylist1 = myList.copy()
# print(mylist1)
# myList = [1, 2, 1, 4, 5]
# mylist1 = myList.copy()
# print(mylist1)
# print(myList.count(1))
# myList.extend([6, 7, 8])
# print(myList)
# print(myList.index(4))
# myList.insert(2, 3)
# print(myList)
# print(myList.pop())
# print(myList)   
# print(myList.reverse())
# print(myList)
# myList.sort()
# print(myList)
# myList.remove(6)
# print(myList)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newList = []
# for x in fruits:
#     if "a" in x:
#         newList.append(x)   
# print(newList)
# newlist = [x for x in fruits if "a" in x]
# print(newlist)


sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
newlist = [x for x in words if x != "the"]
print(newlist)
