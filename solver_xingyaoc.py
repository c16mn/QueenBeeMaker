from collections import defaultdict
import itertools
import json
import string
import sys

def make_lookup_dict() -> dict:
    file = open('scrabble.txt', 'r')
    lookup_dict = defaultdict(list)
    for word in file.readlines():
        word = word.strip()
        if len(word) < 4 or len(set(word)) > 7:
            continue
        for letter in string.ascii_uppercase:
            if letter in word:
                lookup_dict[letter].append(word)
    return lookup_dict

def clean_and_check_input(letters: str, center: str) -> tuple:
    letters = letters.upper()
    center = center.upper()
    if len(center) != 1:
        raise TyperError('Length of "center" must be 1.')
    if not letters.isalpha():
        raise TyperError('"letters" must only contain the alphabet.')
    return letters, center


def solve(letters: str, center: str):
    letters, center = clean_and_check_input(letters, center)
    with open('spelling_bee_lookup.json', 'r') as fp:
        words_with_center_letter = json.load(fp)[center]
    for word in words_with_center_letter:
        if len(set(word).union(set(letters))) == len(set(letters)):
            yield word

# ld = make_lookup_dict()
# with open('spelling_bee_lookup.json', 'w') as fp: json.dump(ld, fp)


if __name__ == "__main__":
    letters, center = sys.argv[1], sys.argv[2]
    valid_words = solve(letters, center)
    print(list(valid_words))

