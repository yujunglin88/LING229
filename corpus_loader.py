import os
from nltk.corpus import PlaintextCorpusReader
import pandas as pd

def load_text(text_path) -> str:
    """ Load the text from the file system
    Args:
        text_path: str: path to the corpus file
    Returns:
        text: str: the corpus as a string
    """
    with open(text_path, 'r', encoding="utf8") as file:
        text = file.read()
    return text

def load_corpus(corpus_dir) -> (PlaintextCorpusReader, dict, pd.DataFrame): # type: ignore
    """ Load all corpus from a directory
    Args:
        corpus_dir: str: path to the directory containing the courpus
    Returns:
        corpus: PlaintextCorpusReader: the corpus
        corpus_dict: dict: dictionary containing the corpus
        corpus_df: DataFrame: DataFrame containing the corpus
    """
    corpus = PlaintextCorpusReader(corpus_dir, '.*')
    corpus_dict = {}
    for file in os.listdir(corpus_dir):
        if file.endswith('.txt'):
            corpus_name = file.split('.')[0]
            corpus_dict[corpus_name] = load_text(os.path.join(corpus_dir, file))
    corpus_df = pd.DataFrame(corpus_dict.items(), columns=['filename', 'text'])
    return corpus, corpus_dict, corpus_df