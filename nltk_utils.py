import numpy as np
import nltk
from nltk.stem.snowball import SnowballStemmer
import spacy
nltk.download('punkt')
nltk.download('stopwords')
nlp = spacy.load("fr_core_news_sm")
stemmer =  SnowballStemmer("french")

def tokenize(sentence:str):
    """
    split sentence into array of words/tokens
    a token can be a word or punctuation character, or number
    """
    sentence=sentence.replace("'"," ").replace('é','e').replace('-',' ')
    return nltk.word_tokenize(sentence,language='french')
    # token=nlp(sentence)
    # return [str(i) for i in token]


def stem(word):
    """
    stemming = find the root form of the word
    examples:
    words = ["organize", "organizes", "organizing"]
    words = [stem(w) for w in words]
    -> ["organ", "organ", "organ"]
    """
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bag   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag