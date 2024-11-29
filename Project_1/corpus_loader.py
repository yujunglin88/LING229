import os

def load_text(text_path):
    """ Load the text from the file system
    Args:
        text_path: str: path to the corpus file
    Returns:
        text: str: the corpus as a string
    """
    with open(text_path, 'r') as file:
        text = file.read()
    return text

def load_corpus(corpus_dir):
    """ Load all corpus from a directory
    Args:
        corpus_dir: str: path to the directory containing the courpus
    Returns:
        corpus: dict: a dictionary of courpus, where the key is the name of the corpus and the value is the corpus as a string
    """
    corpus = {}
    for file in os.listdir(corpus_dir):
        if file.endswith('.txt'):
            corpus_name = file.split('.')[0]
            corpus[corpus_name] = load_text(os.path.join(corpus_dir, file))
    return corpus