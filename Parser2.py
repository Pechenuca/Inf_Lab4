import re
import time

t1 = time.time()
readfile = open("x.xml", encoding="utf-8").read().split("\n")
writefile = open("ya.yml", "w", encoding="utf-8")
k = 0
for i in readfile:
    s1 = i.replace("<", "").replace(">", ":")
    newstring = re.sub("<\w+>.*", "  " * k + s1, i)
    if re.findall("<\w+>.*", i):
        k += 1
    if re.findall("/\w*>", i):
        k = k - 1
    if re.findall("/", i):
        newstring = newstring[:newstring.rfind("/")]
    if re.findall("\w+", newstring):
        writefile.write(newstring + "\n")
writefile.close()
print((time.time() - t1) * 10)
