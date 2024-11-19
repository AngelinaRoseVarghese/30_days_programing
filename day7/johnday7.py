'''
Author: John Kuriakose
Description:A program to Count the number of vowels in a word.
'''
input_word=(input("Enter a word: "))
vowels = str("aeiouAEOIU")
vowel_count=0
for i in input_word:
    if (i in vowels):
        vowel_count=vowel_count+1
print("no. of vowels in the word are",vowel_count)