import string

def boyer_moore(text, pattern, alphabet):
    bad_char_dict, shift_table = _preprocessing(pattern, alphabet)
    result = []

    index = 0
    while index < len(text) - len(pattern):
        # Failed position is always relative to index. Hence it starts at len(pattern) - 1
        failed_pos = _match(text, pattern, index, len(pattern) - 1)

        if failed_pos < 0:
            # Means we have a match
            result.append(index) # Add match pos to result list
            index += shift_table[0] # And shift according to preproccessed table
        else:
            # Else a mismatch
            char_at_mismatch = text[index + failed_pos]
            index += max(shift_table[failed_pos+1],
                        failed_pos - bad_char_dict[char_at_mismatch])

    return result

def _match(text, pattern, index, j):
    while j >= 0 and pattern[j] == text[index + j]:
        j -= 1
    return j


"""
This part contains the preprocessing neccessary to prepare
the Boyer Moore Search Alg.
"""

def _preprocessing(pattern, alphabet):
    bad_char_dict = _bad_character_setup(pattern, alphabet)
    shift_table = _good_suffix_setup(pattern)
    return bad_char_dict, shift_table

def _bad_character_setup(pattern, alphabet):
    bc_dict = {}
    for c in alphabet:
        bc_dict[c] = -1

    for index, symbol in enumerate(pattern):
        bc_dict[symbol] = index

    return bc_dict


def _good_suffix_setup(pattern):
    m = len(pattern)
    f = [0] * (m + 1)
    shift_table = [0] * (m + 1)

    f, shift_table = _good_suffix_preprocess1(pattern, f, shift_table, m)
    shift_table = _good_suffix_preprocess2(f, shift_table, m)

    return shift_table

def _good_suffix_preprocess1(pattern, f, s, m):
    i = m
    j = m + 1
    f[i] = j
    while i > 0:
        while j <= m and pattern[i-1] != pattern[j-1]:
            if s[j] == 0: s[j] = j - i
            j = f[j]
        i -= 1
        j -= 1
        f[i] = j

    return f, s

def _good_suffix_preprocess2(f, s, m):
    j = f[0]
    for i in range(0, m + 1):
        if s[i] == 0: s[i] = j
        if i == j: j = f[j]

    return s


if __name__ == "__main__":
    text = "PANPANMAN"
    pattern = "PAN"
    alphabet = list(string.ascii_uppercase)
    res = boyer_moore(text, pattern, alphabet)
    print(res)

    text = "ababababababbababbaabababbababbabab"
    pattern = "abbabab"
    alphabet = list(string.ascii_lowercase)
    res = boyer_moore(text, pattern, alphabet)
    print(res)
