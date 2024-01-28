import operator
import matplotlib.pyplot as plt
import numpy as np

# 1. Dictionary.
# key: letter
# value: letter's number of appearances in a set containing every 5-letter english word

appearance_numbers = {'a': 0,
                      'b': 0,
                      'c': 0,
                      'd': 0,
                      'e': 0,
                      'f': 0,
                      'g': 0,
                      'h': 0,
                      'i': 0,
                      'j': 0,
                      'k': 0,
                      'l': 0,
                      'm': 0,
                      'n': 0,
                      'o': 0,
                      'p': 0,
                      'q': 0,
                      'r': 0,
                      's': 0,
                      't': 0,
                      'u': 0,
                      'v': 0,
                      'w': 0,
                      'x': 0,
                      'y': 0,
                      'z': 0, }


# 2. Creating a list containing every five letter valid word.
file = open('words_alpha.txt','r')  #file taken from https://github.com/dwyl/english-words
valid_words = str(file.read()).split()
file.close()

five_letter_words = []

for word in valid_words:
    if len(word) == 5:
        five_letter_words.append(word)


#3. Counting appearances in words for every letter - appearance counted only as a 0 or 1, repetitions irrelevant
for word in five_letter_words:
    temp_letters = []
    for letter in word:
        if letter not in temp_letters:
            temp_letters.append(letter)
            appearance_numbers[letter] += 1



#4. Sorting by appearances, descending, and then printing'''
import heapq
appearance_numbers_sorted = sorted(appearance_numbers.items(), key=operator.itemgetter(1), reverse=True)
print(appearance_numbers_sorted)
letters = [n[0] for n in appearance_numbers_sorted][:10]
#print(letters)


#5. Function which for top10 letters finds out their number of appearances in every position from 1st to 5th
def appearance_counter_by_position_in_a_word(letter,words):
    positions = [0, 0, 0, 0, 0]
    for word in words:
        for i in range(5):
            if letter == word[i]:
                positions[i] += 1
            i += 1

    return positions


#6. Function which prints appearances by position in a word
def plotting_appearances_by_position(letters, five_letter_words):
    labels = ['1st letter', '2nd letter', '3rd letter', '4th letter', '5th letter']
    fig,ax = plt.subplots()
    fig.set_figwidth(13)
    fig.set_figheight(6)
    x = np.arange(len(labels))
    width = 0.083
    i = 0
    for letter in letters:
        apps = appearance_counter_by_position_in_a_word(letter,five_letter_words)
        print(letter,apps)
        rect = ax.bar(x + i*width, apps, width, label=letter)
        i += 1

    ax.set_ylabel('Number of apperances')
    ax.set_title('Appearances by position in a word\n(BTW overall appearances: a=7247, e=6728, s=5871, r=4864,'
                 ' i=4767, o=4613, l=3923, t=3866, n=3773, u=3241)')
    plt.xticks(x+len(letters)/2*width - width/2, labels)

    ax.legend()
    plt.show()
    return


#7. function which prints which letter is most likely to be in a word with a given letter'''
def finding_accompanying_letters(letters, five_letter_words):
    for letter in letters:
        accompanying_letters = {'a': 0,
                              'b': 0,
                              'c': 0,
                              'd': 0,
                              'e': 0,
                              'f': 0,
                              'g': 0,
                              'h': 0,
                              'i': 0,
                              'j': 0,
                              'k': 0,
                              'l': 0,
                              'm': 0,
                              'n': 0,
                              'o': 0,
                              'p': 0,
                              'q': 0,
                              'r': 0,
                              's': 0,
                              't': 0,
                              'u': 0,
                              'v': 0,
                              'w': 0,
                              'x': 0,
                              'y': 0,
                              'z': 0, }

        for word in five_letter_words:
            temp_list = []
            if letter in word:
                for i in range(len(word)):
                    if word[i] != letter and word[i] not in temp_list:
                        temp_list.append(word[i])
                        accompanying_letters[word[i]] += 1

        accompanying_letters_sorted = sorted(accompanying_letters.items(), key=operator.itemgetter(1), reverse=True)
        print('{}: '.format(letter), accompanying_letters_sorted)


finding_accompanying_letters(letters, five_letter_words)
'''an efficient solution which allows a quick comparison of relative positions of letters is needed here. Right now
I made it manually on a piece of paper ;)'''
plotting_appearances_by_position(letters,five_letter_words)






