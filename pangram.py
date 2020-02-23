def is_pangram(sentence):
    abc = "abcdefghijklmnopqrstuvwxyz"
    for letter in abc:
        if letter not in sentence.lower():
            return False
    return True







