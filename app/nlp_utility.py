import nltk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('punkt')


# initialize the data_cleaning process
# tokenize the input

def data_clean():
    search_terms = ''
    documents = []
    ui_entry = ''
    ui_tokens = word_tokenize(ui_entry)
    vectorizer = TfidfVectorizer(analyzer=lambda x:x)
    X = vectorizer.fit_transform(ui_tokens)
    dfv = pd.DataFrame({'original_string':  ui_entry, 'tokenized_data':  ui_tokens, 'vectors':  X})
    add_user_input = repo.load_user_input()
    return dfv





