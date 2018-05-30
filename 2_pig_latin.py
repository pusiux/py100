word = input()
v = "aeiouy"
index = 0
for l in v:
    index = word.find(l)
    print(word[index::] + word[0:index] + "ay")
    break
