#!/usr/bin/env python
# coding: utf-8

# ### Consider a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just one character at the index in the string, and the remaining characters will occur the same number of times. Given a string, determine if it is valid. If so, return YES , otherwise return NO .
# 
# 
# Note - You have to write at least 2 additional test cases in which your program will run successfully and provide an explanation for the same.
# Example input 1 - s = “abc”. This is a valid string because frequencies are { “a”: 1, “b”: 1, “c”: 1 } Example output 1- YES
# Example input 2 - s “abcc”. This string is not valid as we can remove only 1 occurrence of “c”. That leaves character frequencies of { “a”: 1, “b”: 1 , “c”: 2 }
# Example output 2 - NO
# 

# In[1]:


CHARS = 26

def ValidString(s):
    freq = [0] * CHARS

    for i in range(len(s)):
        freq[ord(s[i]) - ord('a')] += 1

    freq1 = 0
    count_freq1 = 0
    for i in range(CHARS):
        if freq[i] != 0:
            freq1 = freq[i]
            count_freq1 = 1
            break

    freq2 = 0
    count_freq2 = 0
    for j in range(i + 1, CHARS):
        if freq[j] != 0:
            if freq[j] == freq1:
                count_freq1 += 1
            else:
                count_freq2 = 1
                freq2 = freq[j]
                break

    for k in range(j + 1, CHARS):
        if freq[k] != 0:
            if freq[k] == freq1:
                count_freq1 += 1
            elif freq[k] == freq2:
                count_freq2 += 1
            else:
                return False

        if count_freq1 > 1 and count_freq2 > 1:
            return False

    return True


if __name__ == "__main__":
    str1 = "abcbc"
    if ValidString(str1):
        print("YES")
    else:
        print("NO")

    # Example test cases
    s = "abc"
    if ValidString(s):
        print("YES")
    else:
        print("NO")

    s = "abcc"
    if ValidString(s):
        print("YES")
    else:
        print("NO")

    # Additional test cases
    s = "aabbcc"
    if ValidString(s):
        print("YES")
    else:
        print("NO")

    s = "aabbccc"
    if ValidString(s):
        print("YES")
    else:
        print("NO")

    s = "aabbbcc"
    if ValidString(s):
        print("YES")
    else:
        print("NO")

    s = "aabbcccc"
    if ValidString(s):
        print("YES")
    else:
        print("NO")

        

