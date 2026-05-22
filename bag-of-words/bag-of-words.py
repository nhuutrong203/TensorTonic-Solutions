import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    word_to_index = dict(zip(vocab, range(len(vocab))))
    bags = np.zeros(len(vocab), dtype=int)

    for token in tokens:
        if token in word_to_index:
            index = word_to_index[token]
            bags[index] += 1

    return bags
    
    