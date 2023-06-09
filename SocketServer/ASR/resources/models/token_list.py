# -*- coding: utf-8 -*-
"""token_list.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hZhtInhwDGYMLiCQjWVV87wfgQw04NNy
"""

import pickle
import pandas as pd

df = pd.DataFrame()

file_path = './token_list.pkl'
df = pd.read_pickle(file_path)

# List of Korean consonants and vowels
initials = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

vowels = [
    'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'
]

finals = [
    '', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

# Generate all possible combinations of Korean syllables
syllables = []

for initial in initials:
    for vowel in vowels:
        for final in finals:
            # Calculate the unicode code point for the syllable
            code = 0xAC00 + (initials.index(initial) * 588) + (vowels.index(vowel) * 28) + finals.index(final)
            # Convert the code point to the corresponding character
            syllable = chr(code)
            syllables.append(syllable)

# Print the generated syllables
for syllable in syllables:
    df.append("'"+syllable+"',")

file_path2 = './token_list2.pkl'
df_list = df 

with open(file_path2, 'wb') as f:
    pickle.dump(df_list, f)