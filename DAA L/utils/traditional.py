def rabin_karp_similarity(text1, text2):
    chunk_size = 10  # Number of words per chunk
    matches = 0
    total = 0

    words1 = text1.split()
    chunks = [' '.join(words1[i:i + chunk_size]) for i in range(0, len(words1) - chunk_size + 1)]

    for chunk in chunks:
        if chunk in text2:
            matches += 1
        total += 1

    return (matches / total) * 100 if total > 0 else 0


def boyer_moore_similarity(text1, text2):
    def preprocess_bad_character(pattern):
        bad_char = {}
        for i in range(len(pattern)):
            bad_char[pattern[i]] = i
        return bad_char

    def boyer_moore_search(pattern, text):
        m = len(pattern)
        n = len(text)
        if m == 0 or n == 0 or m > n:
            return 0

        bad_char = preprocess_bad_character(pattern)
        s = 0
        occurrences = 0

        while s <= n - m:
            j = m - 1
            while j >= 0 and pattern[j] == text[s + j]:
                j -= 1
            if j < 0:
                occurrences += 1
                s += m  # Full pattern shift
            else:
                next_char_index = s + j
                mismatched_char = text[next_char_index]
                last_occurrence = bad_char.get(mismatched_char, -1)
                s += max(1, j - last_occurrence)
        return occurrences

    chunk_size = 10
    words1 = text1.split()
    chunks = [' '.join(words1[i:i + chunk_size]) for i in range(0, len(words1) - chunk_size + 1)]
    total = len(chunks)
    matches = 0

    for chunk in chunks:
        if boyer_moore_search(chunk, text2) > 0:
            matches += 1

    return (matches / total) * 100 if total > 0 else 0
