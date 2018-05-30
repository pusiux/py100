word = input()
v = "aeiouy"
count=0
for l in v:
    if(l in word):
        count+=1
print(count)
