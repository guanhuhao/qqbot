import os 
f = open("in","r",encoding="UTF-8")
w = open("saying","w",encoding="UTF-8")
for line in f :
    if line == "\n" : continue
    w.write(line)
    print(line)


