'''
Date:14/11/2024
Author: Angelina Rose Varghese
Description:A program to Count the number of vowels in a word.
'''
word=(input("Enter a word: "))
vowels=str("aeiouAEOIU")
vowel_count=0
for i in word:
    if (i in vowels):
        vowel_count=vowel_count+1
print("no. of vowels in the word are",vowel_count)





