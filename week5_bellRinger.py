# # Problem Set 1: Indexing and Slicing Strings
# # Basic Indexing:
# # Given the string magic = 'abracadabra',
# magic = 'abracadabra'
# # a. Retrieve the 5th character. 
# fifth_char = print(magic[4])
# # b. Retrieve the second to last character.
# second_to_last_char =print(magic[-2])
# # c. Find the first occurrence of the letter 'c'.
# first_c_index=print(magic.index('r'))
# last_a_index=print(magic.rindex('a'))
# # rindex finds the last occurrence of a specified value.
# # Advanced Slicing:
# # Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# # a. Extract the letters 'hij'.
# # hij=print(alphabet[7:10])
# hij=print(alphabet.index('hij'))
# hiji=print(alphabet[7:10])
# # b. Extract every second letter starting from 'a' to 'm'.
# m_index= print(alphabet.index('m'))
# every_second= print(alphabet[0:13:2])

# #  c. Reverse the entire string using slicing.
# reversed_alphabet=print(alphabet[ : :-1])

# i_have_a_dream= "i have a dream that one day this nation will rise up" 
# reversed_i_have_a_dream=print(i_have_a_dream[ : :-1])


# # Problem Set 2: Extracting Information
# # From Descriptions:
# # Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
# famous_quote = "Ask not what your country can do for you — ask what you can do for your country"
# john_f_kennedy = print(famous_quote.find("John F. Kennedy"))
# #output: eighty-three
# extracted_name = print(famous_quote[83:])

# # Manipulating Words:
# # Given the string info = "Python is fun. Fun is good. Good is subjective.",
# # a. Extract the word 'subjective' without knowing its exact position.
# # b. Extract every third word.
# # c. Reverse the positions of the words, but keep the characters in each word in the same order.
# # Manipulating Words:
# info = "Python is fun. Fun is good. Good is subjective."

# # a. Extract the word 'subjective' without knowing its exact position
# subjective_index = info.find("subjective")
# print(info[subjective_index:])  

# # b. Extract every third word
# words = info.split()
# print(words[::3])  

# # c. Reverse the positions of the words, but keep characters in each word the same
# print(' '.join(words[::-1]))  

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
# Upper & Lower:
text = "MAY THE FORCE BE WITH YOU."
# String Joining and Splitting:
motto = ["Make", "haste", "slowly."]
# a. Convert the list into a single string
joined_motto = ' '.join(motto)
print(joined_motto)
joined_motto_split=joined_motto.split('a')
print(joined_motto_split)



# Problem Set 4: String Properties and Advanced Operations
# 1. Repetition
print("Iteration" * 7)

# 2. Word Search
quote = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
if "moonlight" in quote:
    print("The word 'moonlight' appears in the quote.")
else:
    print("The word 'moonlight' does not appear in the quote.")

# 3. Length and Count
word = "Supercalifragilisticexpialidocious"

# a. Number of characters
print(len(word))

# b. Number of 'i' letters
print(word.count('i'))