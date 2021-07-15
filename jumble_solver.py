# TL;DR: Jumble solver using a hash table and letter-wise sorting of all english words.
# O(n) time and space complexity in the average case but with room for optemization both
# algorithmically/mathematically and infrastructurally.
# I highly recommend reading jumble_solver.ipynb for the full explanation.

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = word_file.read().split()
    return valid_words

def get_sorted_words_table(english_words):
    sorted_words_table = dict()
    for idx, word in enumerate(english_words):
        word = "".join(sorted(word))
        if word in sorted_words_table:
            sorted_words_table[word].append(idx)
        else:
            sorted_words_table[word] = [idx]
    return sorted_words_table

def get_all_unique_alphabetical_substrings(word):
    all_substrings = [word[i: j] for i in range(len(word)) for j in range(i + 1, len(word) + 1)]
    # can't think of a way to generate all substring except the original in one line
    all_substrings.remove(word)
    return set(["".join(sorted(substring)) for substring in all_substrings])

def jumble(word):
    all_unique_alphabetical_substrings = get_all_unique_alphabetical_substrings(word)
    match_idxs = []
    for substr in all_unique_alphabetical_substrings:
        if substr in sorted_words_table:
            match_idxs += sorted_words_table[substr]
    return [english_words[idx] for idx in match_idxs]


if __name__ == '__main__':
    english_words = load_words()
    sorted_words_table = get_sorted_words_table(english_words)
    print(jumble(input()))
