import collections
import string


with open('northwind.txt','r') as f:
    lines=f.read()
    words=lines.split()

new_words=[] #list of new words
for word in words: 
    strip_word=word.strip(',').strip('.')
    new_words.append(strip_word.lower())
#print(new_words)

word_counter={} 
for word in new_words: #Counts words
    if word not in word_counter:
        word_counter[word]=0
    word_counter[word]+=1
print(word_counter)

##letter_counter={}
##for i in range(0,len(new_words)): #Counts letters
##    letters=list(new_words[i])
##    for let in letters:
##        if let not in letter_counter:
##            letter_counter[let]=0
##        letter_counter[let]+=1
##print(letter_counter)


letter_counter = collections.Counter()
letters=list(lines.lower())
allowed=list(string.ascii_letters)
for lett in letters:
    if lett in allowed:
        letter_counter[lett] += 1
print(letter_counter)    
