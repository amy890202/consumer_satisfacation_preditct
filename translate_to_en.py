
!pip install googletrans==3.1.0a0
from googletrans import Translator, constants
from pprint import pprint

translator = Translator(service_urls=['translate.googleapis.com'])
#print(out)
comment_text = X.iloc[0:,4:5]
comment_text_list = comment_text.values.tolist()

english_comment = []
 
for i in comment_text_list:
  if type(i[0]) == type('ab'):
  #out = re.sub(r'[^\w\s]','',i[0])
    translation = translator.translate(i[0], dest='en')
    #print(f"{translation.text}")
    english_comment.append(f"{translation.text}")
  english_comment.append(None)
#print(english_comment)
