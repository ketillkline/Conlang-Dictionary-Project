import csv, os

path = r"./Files/Arkabanga.csv"
words = {

}
with open(path, encoding="UTF8") as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        cat, word, meaning, shelf1, shelf2, shelf3 = row
        words[word] = meaning

# ------- Get close to 0(1) time ------------------ #

target_letter = "o"
word_list = []
vowels = ['a', 'i', 'o', 'e', 'u', 'o']
vowel_count = {}
for key in words.keys():
    word_list.append(key)
for word in word_list:
    for letter in word:
        for vowel in vowels:
            if letter == vowel:
                if vowel in vowel_count.keys():
                    vowel_count[vowel]+=1
                else:
                    vowel_count[vowel] = 1

for key, value in vowel_count.items():
    print(f"{key}: {value}")

# -------------------------------------------------- #
# ----- What consonants do we have? ----------- #

