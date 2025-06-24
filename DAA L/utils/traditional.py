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