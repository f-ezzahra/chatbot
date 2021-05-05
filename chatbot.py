from newspaper import Article
import random 
import string 
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import  cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')
nltk.download('punkt' , quiet=True)
def greeting_response(text1):
  text1 = text1.lower()
  bot_greetings = ['salam cv ?dkhol lhad site fih kolchi enjoy: open classroom']
  user_greetings = ['oui','ah','yes','ok','wakha']
 
 
 
  for word in text1.split():
    if word in user_greetings:
      return random.choice(bot_greetings)
def index_sort(list_var):
  lenght = len(list_var)
  list_index = list(range(0,lenght))
  x = list_var
  for i in range(lenght):
    for j in range(lenght):
      if x[var_list[i]] > x[var_list[j]]:
       biss = x[var_list[i]]
       x[var_list[i]] = x[var_list[j]]
       x[var_list[j]] = biss
  return list_index
def bot_response(user_input):
  user_input = user_input.lower()
  sentence_list.append(user_input)
  bot_response = ''
  cm = CountVectorizer().fit_transform(sentence_list)
  similarity_scores = cosine_similarity(cm[-1] , cm)
  similarity_scores_list = similarity_scores.flatten()
  index = index_sort(similarity_scores_list)
  index = index[1:]
  response_flag = 0
  j = 0
  for i in range(len(index)):
    if similarity_scores_list[index[i]] > 0.0:
     bot_response =  bot_response +' ' +bot_response[index[i]]
     response_flag = 1
     j=j+1
     if j>2:
       break
    if response_flag == 0:
      bot_response =  bot_response +' ' +"smahlya mafhamtch"
      sentence_list.remove(user_input)
  return bot_responce
 
#begin chat
print('ila bghiti chi had li y3awanak bach t3alam les langages informatiques marhba bik m3ana :-)')
exit_list = ['exit,nhadro apres','bslama','mamsalich db','la sf','la','non','no']
while(True):
    user_input = input()
    if user_input in exit_list:
     print('fsac:ok merci bslama , see u soon')
     break
    else:
      if greeting_response(user_input) != None:
        print('fsac: '+greeting_response(user_input))
      else : 
        print('smahlyfa mafhamtch')
