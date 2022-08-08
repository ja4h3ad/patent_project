# please note that for the purposes of the week 5 assignment, the user input will be solicited
# ~ artificially, however the actual user input will be derived from the web form

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
import db.sql_repo
repo = db.sql_repo.patentsSQL()

while True:

    ui_simulation = input ("Type your string here.  Please be sure to use a descriptive phrase")

    if len(ui_simulation) > 150:
        print ("Error! Only 150 characters allowed!")

    else:
        break
print ("Your input was:", ui_simulation)


# initialize the data_cleaning process
# tokenize the input
ui_tokens = word_tokenize(ui_simulation)
vectorizer = TfidfVectorizer(analyzer=lambda x:x)
X = vectorizer.fit_transform(ui_tokens)
print ("Shape", X.shape)
dfv = pd.DataFrame({'original_string':  ui_simulation, 'tokenized_data':  ui_tokens, 'vectors':  X})
add_user_input = repo.load_user_input()
for i, row in dfv.iterrows():
    # here %S means string values
    sql = "INSERT INTO patents.webForm (original_string,tokenized_data,vectors) " \
          "VALUES (%s,%s,%s)"
    cursor.execute(sql)
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    conn.commit()


