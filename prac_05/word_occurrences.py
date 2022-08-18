"""
CP1404/CP5632 Practical
Count word from a text
"""

words_repeat = {}
input_text = input("Text: ").split()

for word in input_text:
    words = words_repeat.get(word, 0)
    words_repeat[word] = words+1

words = list(words_repeat)
words.sort()

for word in words:
    print(f"{word}  :  {words_repeat[word]}")
