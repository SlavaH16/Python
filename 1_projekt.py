#Textový analyzátor

#Úvod
line = "-" * 45
print("""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Miloslav Houška
email: slava.89@seznam.cz""")
print(line)

#Uživatelský přístup
username = input("username: ")
password = input("password: ")
print(line)

user = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

if user.get(username) != password:
  print("unregistered user, terminating the program..")
  quit()
else:
  print("Welcome to the app,", username)
  print("We have 3 texts for you.")
  print(line)

#Výběr textů
texts = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''
At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''
The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

number_of_texts = len(texts) + 1
allowed_value = str(list(range(1,number_of_texts)))
select_text = input("Enter a number btw. 1 and 3 to select: ")
print(line)

if select_text not in allowed_value:
  print("wrong value, terminating the program..")
  quit()

#Analýza
selected_text = texts[int(select_text) -1]
words = []

#Počet slov
for word in selected_text.split():
  clean_word = word.strip(",.")
  words.append(clean_word)

count_words = len(words)
print("There are", count_words, "words in the selected text.")

#Počet slov začínajících velkým písmenem
title_words = []

for title_word in words:
  if title_word.istitle():
    title_words.append(title_word)

count_title_words = len(title_words)
print("There are", count_title_words, "titlecase words.")

#Počet slov psaných velkými písmeny
upper_words = []

for upper_word in words:
  if upper_word.isupper() and upper_word.isalpha():
    upper_words.append(upper_word)

count_upper_words = len(upper_words)
print("There are", count_upper_words, "uppercase words.")

#Počet slov psaných malými písmeny
lower_words = []

for lower_word in words:
  if lower_word.islower():
    lower_words.append(lower_word)

count_lower_words = len(lower_words)
print("There are", count_lower_words, "lowercase words.")

#Počet čísel
numeric_strings = []

for numeric_string in words:
  if numeric_string.isdigit():
    numeric_strings.append(numeric_string)

count_numeric_strings = len(numeric_strings)
print("There are", count_numeric_strings, "numeric strings.")

#Suma všech čísel
sum_numbers = 0

for sum in numeric_strings:
  int_sum = int(sum)
  sum_numbers = sum_numbers + int_sum

print("The sum of all the numbers", sum_numbers)

#Graf
print(line)

print("LEN".rjust(3), "|", "OCCURENCES".center(20), "|", "NR.")

print(line)

many_words = {}

for word in words:
  length_word = len(word)
  if length_word not in many_words:
    many_words[length_word] = 1
  else:
    many_words[length_word] = many_words[length_word] + 1


sorted_length = list(many_words.items())

for index, par in enumerate(sorted(sorted_length, reverse=False),1):
  stars = par[1] * "*"
  print(str(index).rjust(3), "|", stars.ljust(20), "|", par[1])


