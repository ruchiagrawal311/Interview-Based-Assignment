#!/usr/bin/env python
# coding: utf-8

# ###  Write a program that takes a string as input, and counts the frequency of each word in the string, there might be repeated characters in the string. Your task is to find the highest frequency and returns the length of the highest-frequency word.
# 
# 
# Note - You have to write at least 2 additional test cases in which your program will run successfully and provide an explanation for the same.
# Example input - string = “write write write all the number from from from 1 to 100” Example output - 5
# Explanation - From the given string we can note that the most frequent words are “write” and “from” and the maximum value of both the values is “write” and its corresponding length is 5
# 

# In[1]:


def find_highest_frequency_word_length(string):
    # Split the string into words
    words = string.split()

    # Count the frequency of each word
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Find the highest frequency
    max_frequency = 0
    for count in word_counts.values():
        if count > max_frequency:
            max_frequency = count

    # Find the length of the highest-frequency word
    highest_frequency_word_length = 0
    for word, count in word_counts.items():
        if count == max_frequency and len(word) > highest_frequency_word_length:
            highest_frequency_word_length = len(word)

    return highest_frequency_word_length


string1 = "write write write all the number from from from 1 to 100"
print("Output of 1st Test Case: ")
print(find_highest_frequency_word_length(string1))

string2 = "apple apple orange banana banana apple"
print("Output of 2nd Test Case: ")
print(find_highest_frequency_word_length(string2))  
# Explanation: The most frequent word is "apple" with a frequency of 3, and its length is 5.

