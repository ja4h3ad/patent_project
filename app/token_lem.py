import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import wordpunct_tokenize
nltk.download('wordnet')
import contractions
import string

# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer


# initialize the data_cleaning process
# tokenize the input
ui_entry = "I have a really good idea!!!!  The whole point of it is that I'm a super-genius!!!!!..."


def data_clean(ui_entry):
    # identify object to Lemmatize
    lemmatizer = WordNetLemmatizer
    tokenizer = wordpunct_tokenize
    clean1 = []
    # remove contractions
    for word in ui_entry.split():
        clean1.append(contractions.fix(word))
    clean1 = ' '.join(clean1).lower()
    # remove punctuation with str object
    remove_punct = clean1.translate(str.maketrans('', '',string.punctuation))
    tokens = tokenizer(remove_punct)
    lemmatized_words = []
    for token in tokens:
        lemmies = lemmatizer.lemmatize((token))
        lemmatized_words.append(lemmies)

    # vectorizer = TfidfVectorizer(analyzer=lambda x:x)
    # X = vectorizer.fit_transform(ui_tokens)
    # dfv = pd.DataFrame({'original_string':  ui_entry, 'tokenized_data':  ui_tokens, 'vectors':  X})
    # add_user_input = repo.load_user_input()
    # return dfv





