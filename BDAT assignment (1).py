#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Question 1.
a = 5 
b = 5.0
c = 5 > 1
d = '5'
e = 5 * 2
f = '5' * 2
g = '5' + '2'
h = 5 / 2
i = 5 % 2
j = {5, 2, 1}
k = 5 == 3
l = Pi = (3.14159)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))



# In[1]:


#Question 2a.
word = "Supercalifragilisticexpialidocious"
letter_count = len(word)
print("Number of letters:", letter_count)


# In[3]:


#Question 2b
word = "Supercalifragilisticexpialidocious"
substring = "ice"

if substring in word:
    print("Substring 'ice' is present in the word.")
else:
    print("Substring 'ice' is not present in the word.")


# In[4]:


#Question 2c.
words = ["Supercalifragilisticexpialidocious", "Honorificabilitudinitatibus", "Bababadalgharaghtakamminarronnkonn"]

longest_word = max(words, key=len)
print("The longest word is:", longest_word)


# In[5]:


#Question 2d.
composers = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
first_composer = min(composers)
last_composer = max(composers)
print("First composer:", first_composer)
print("Last composer:", last_composer)


# In[13]:


#Question 3
a = 2
b = 2
c = 2
import math
def triangleArea(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
# Example usage
area = triangleArea(2, 2, 2)
print(area)




# In[15]:


#Question 4.
def separateOddEven(numbers):
    odd_numbers = []
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return odd_numbers, even_numbers

numbers = [25, 47, 42, 56, 32]
odd_nums, even_nums = separateOddEven(numbers)

print("Odd Numbers:", odd_nums)
print("Even Numbers:", even_nums)


# In[16]:


#Question 5a.
def inside(x, y, x1, y1, x2, y2):
    if x >= x1 and x <= x2 and y >= y1 and y <= y2:
        return True
    else:
        return False

print(inside(1, 1, 0, 0, 2, 3))  
print(inside(-1, -1, 0, 0, 2, 3)) 



# In[19]:


#Question 5b.
def inside(x, y, x1, y1, x2, y2):
    if x >= x1 and x <= x2 and y >= y1 and y <= y2:
        return True
    else:
        return False

# Check if the point (1, 1) lies in both rectangles. where rectangle1 (x1,y1)=(0.3.0.5) and (x2,y2)=(1.1,,0.7).and 
#rectangle2 (x1,y1)=(0.5, 0.2) and (x2,y2)=(1.1, 2)
lies_in_rectangle1 = inside(1, 1, 0.3, 0.5, 1.1, 0.7)
lies_in_rectangle2 = inside(1, 1, 0.5, 0.2, 1.1, 2)
lies_in_both_rectangles = lies_in_rectangle1 and lies_in_rectangle2

print(lies_in_both_rectangles)


# In[31]:


#Question 6.

def pig(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if word[0].lower() in vowels:
        pig_word = word + 'way'
    else:
        pig_word = word[1:] + word[0] + 'ay'
    
    return pig_word

pig_word1 = pig('happy')
print(pig_word1)  

pig_word2 = pig('Enter')
print(pig_word2) 


# In[40]:


#Question 7.


# In[ ]:


#Question 8.

