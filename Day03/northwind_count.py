with open('northwind.txt','r') as f:
    lines=f.read()
print(lines)
words=lines.split()
print(words)
counter={}
for i in range(0,len(words)):
    
    counter[words[i]]+=1
