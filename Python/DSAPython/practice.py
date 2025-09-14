sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
newlist = [x for x in words if x != "the"]
print(newlist)