# to count number of vowels in a word
word=(input("Enter a word"))
v=str("aeiou")
v_count=0
for j in word:
    if(j in v):
        v_count=v_count+1
print("number of v in the word",v_count)       