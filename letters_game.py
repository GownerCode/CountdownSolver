import random

# random Letters function returns 9 random letters, like the show
def random_letters():
    return [chr(random.randint(97, 97 + 25)) for _ in range(9)]


# ordering the dictionary into a python dict by first letter for efficiency
def init_dict():
    words = []
    with open("words_alpha.txt", "r") as dct:
        words = dct.readlines()

    dict_ordered = {}

    for i in range(97, 97 + 26):
        c = chr(i)
        letter_words = []
        for w in words:
            if w[0] == c and len(w[:-1]) < 10:
                letter_words.append(w[:-1])
        dict_ordered[c] = letter_words
    return dict_ordered


# check if a word can be spelled by the letters
def is_possible(word, L):
    for letter in word:
        if letter in L:
            L.remove(letter)
        else:
            return False
    return True


# solving the letters puzzle
def solve_puzzle(LETTERS, dict_ordered):
    possible_words = []
    for key in dict_ordered:
        if key in LETTERS:
            for word in dict_ordered[key]:
                L = list(LETTERS)
                if is_possible(word, L):
                    possible_words.append(word)
    possible_words.sort(key=len)
    possible_words.reverse()
    pw_dict = {}
    for word in possible_words:
        pw_dict[word] = len(word)
    return pw_dict

print(solve_puzzle(LETTERS, init_dict()))