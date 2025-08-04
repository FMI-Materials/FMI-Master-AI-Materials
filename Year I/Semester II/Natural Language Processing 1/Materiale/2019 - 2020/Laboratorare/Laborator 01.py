# import nltk
# from nltk.book import *
# nltk.word_tokenize("It was late. I saw a cat chasing a mouse.")
# from nltk.corpus import stopwords
# stopwords.words('english')

import string
import time
import numpy as np
from nltk.book import text2

tokens = text2.tokens
vocabulary = text2.vocab()

# 2
start = time.time()
tokens_without_punctuation = [x for x in tokens if x.isalnum()]

# for token in tokens:
#     # valid = True
#     # for character in token:
#     #     if character in string.punctuation:
#     #         valid = False
#     #         break
#     #
#     # if valid:
#     #     tokens_without_punctuation.append(token)
#     if token.isalnum():
#         tokens_without_punctuation.append(token)

print('------------- Task 2 ------------- ')
print('Number of words in the text :', len(tokens_without_punctuation))
print('Time :', time.time() - start)
print('')

# 3
start = time.time()
print('------------- Task 3 ------------- ')
print('Text title :', text2.name)
print('Time :', time.time() - start)
print('')

# 4
start = time.time()
vocabulary_without_punctuation = {}
for key, value in vocabulary.items():
    # valid = True
    # for character in key:
    #     if character in string.punctuation:
    #         valid = False
    #         break
    #
    # if valid:
    #     vocabulary_without_punctuation[key] = value
    if key.isalnum():
        vocabulary_without_punctuation[key] = value

print('------------- Task 4 ------------- ')
print('Length of the vocabulary :', len(vocabulary_without_punctuation))
print('Time :', time.time() - start)
print('')

# 5
start = time.time()


def nr_words_with_lg(lg):
    tokens_with_lg = []
    for token in tokens_without_punctuation:
        if len(token) == lg:
            tokens_with_lg.append(token)

    return len(tokens_with_lg)


lg = 3
print('------------- Task 5 ------------- ')
print('Number of words with length', lg, ':', nr_words_with_lg(lg))
print('Time :', time.time() - start)
print('')

# 6
start = time.time()
vocabulary_without_punctuation_sorted = sorted(list(vocabulary_without_punctuation))


def first_N_lt(N, lt):
    ind = 0
    for word in vocabulary_without_punctuation_sorted:
        if ind == N:
            break

        if word[0] == lt:
            ind = ind + 1
            print(ind, ':', word)


first_N_lt(10, 'c')
print('------------- Task 6 ------------- ')
print('Time :', time.time() - start)
print('')

# 7
start = time.time()
lens = [len(word) for word in vocabulary_without_punctuation_sorted]
min_len = min(lens)
max_len = max(lens)

shortest_words = [word for word in vocabulary_without_punctuation_sorted if len(word) == min_len]
longest_words = [word for word in vocabulary_without_punctuation_sorted if len(word) == max_len]

print('------------- Task 7 ------------- ')

print('Min len :', min_len)
print('Shortest words :', shortest_words)

print('Max len :', max_len)
print('Longest words :', longest_words)

print('Time :', time.time() - start)
print('')

# 8
start = time.time()

# Can use text2.vocab() as well, which contains the frequencies as well
vals, counts = np.unique(tokens_without_punctuation, return_counts=True)
N = 10
count_sort_ind = np.argsort(-counts)
print('------------- Task 8 ------------- ')
for i in range(N):
    ind = count_sort_ind[i]
    print(i, ':', vals[ind], counts[ind])

print('Time :', time.time() - start)
print('')

# 9
start = time.time()
print('------------- Task 9 ------------- ')
print('Mean length of all words :', np.mean(np.array(lens)))
print('Time :', time.time() - start)
print('')

# 10
start = time.time()
once_words = []
for i in range(len(counts)):
    if counts[i] == 1:
        once_words.append(vals[i])

print('------------- Task 10 ------------- ')
print('Words that appear only once :', once_words)
print('Time :', time.time() - start)
print('')

# 11
start = time.time()
print('------------- Task 11 ------------- ')
print(text2.collocation_list())
print('Time :', time.time() - start)
print('')
