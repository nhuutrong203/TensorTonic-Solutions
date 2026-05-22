def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    word_count = {}

    for sentence in sentences:
        for token in sentence:
            if token not in word_count:
                word_count[token] = 1
            else:
                word_count[token] += 1

    return word_count