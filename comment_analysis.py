import joblib
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
import os
from google.colab import drive
drive.mount('/content/drive')



##出現提示欄進行授權

os.chdir('/content/drive/Shareddrives/專題/comment_sentiment') #切換該目錄
os.listdir() #確認目錄內容

happy = r" ([xX;:]-?[dD)]|:-?[\)]|[;:][pP]) "
sad = r" (:'?[/|\(]) "
nltk.download('wordnet')
nltk.download('punkt')
def stem_tokenize(text):
    stemmer = SnowballStemmer("english")
    stemmer = WordNetLemmatizer()
    return [stemmer.lemmatize(token) for token in word_tokenize(text)]

def lemmatize_tokenize(text):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in word_tokenize(text)]

class TextPreProc():
  def __init__(self, use_mention=False):
      self.use_mention = use_mention

  def fit(self, X, y=None):
      return self

  def transform(self, X, y=None):
      # We can choose between keeping the mentions
      # or deleting them
      if self.use_mention:
          X = X.str.replace(r"@[a-zA-Z0-9_]* ", " @tags ")
      else:
          X = X.str.replace(r"@[a-zA-Z0-9_]* ", "")
          
      # Keeping only the word after the #
      X = X.str.replace("#", "")
      X = X.str.replace(r"[-\.\n]", "")
      # Removing HTML garbage
      X = X.str.replace(r"&\w+;", "")
      # Removing links
      X = X.str.replace(r"https?://\S*", "")
      # replace repeated letters with only two occurences
      # heeeelllloooo => heelloo
      X = X.str.replace(r"(.)\1+", r"\1\1")
      # mark emoticons as happy or sad
      X = X.str.replace(happy, " happyemoticons ")
      X = X.str.replace(sad, " sademoticons ")
      X = X.str.lower()
      return X


model = joblib.load('sentiment_analysis_sklearn_model')
pipeline = joblib.load('pipeline')
X = pd.read_csv("olist_order_reviews_dataset_final.csv",encoding="ISO-8859-1")
comment = X.iloc[0:,7:8]
sentiment_list = []
for j in range(len(comment["english_comment"])):
  text = comment["english_comment"][j]
  #print(text)
  if type(text)==type('ab'):
    pipe = pipeline.transform(pd.Series(text))
    proba = model.predict_proba(pipe)[0]
    #print(text)
    if proba[0]>proba[1]:
      sentiment_list.append(0)
    else:
      sentiment_list.append(1)
    #print(sentiment_list)
  else:
    sentiment_list.append(None)
  #print(sentiment_list)
  
