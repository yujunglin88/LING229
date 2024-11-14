import os

def load_corpus(corpus_path):
    """ Load the corpus from the file system
    Args:
        corpus_path: str: path to the corpus file
    Returns:
        corpus: str: the corpus as a string
    """
    with open(corpus_path, 'r') as file:
        corpus = file.read()
    return corpus

def load_all_corpora(corpus_dir):
    """ Load all corpora from a directory
    Args:
        corpus_dir: str: path to the directory containing the corpora
    Returns:
        corpora: dict: a dictionary of corpora, where the key is the name of the corpus and the value is the corpus as a string
    """
    corpora = {}
    for file in os.listdir(corpus_dir):
        if file.endswith('.txt'):
            corpus_name = file.split('.')[0]
            corpora[corpus_name] = load_corpus(os.path.join(corpus_dir, file))
    return corpora