#Magic 8 Ball
#Create a program where it ask the user to make a wish
#Turn the user input() into a TextBlob (make sure you copy/paste then import the code like we did for Chatbot)
#Magic Eight Ball will use some logic (other than completely random) to give 8 different replies 
#replies are like: "Your wish will come true", "That will never happen", "Your wish will come true when the wolf howls at the next full moon."
#The logic should be based on the some word or word combination that the user uses
#It can also be something like the number of words used, whether there are odd or even number of words etc.
#There must be 8 different replies

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from textblob.classifiers import NaiveBayesClassifier

import nltk

try:
  nltk.data.find("tokenizers/punkt")
  nltk.data.find("taggers/averaged_perceptron_tagger")
  nltk.data.find("corpora/movie_reviews")
except LookupError:
  nltk.download('punkt')
  nltk.download('averaged_perceptron_tagger')
  nltk.download('movie_reviews')

def main():
  import random
  wish = input("What is your wish?")
  wishlist = ["Fat chance","Never will happen"]
  wishblob = TextBlob(wish)
  if wishblob.sentiment.polarity > 0:
    print("Your wish will come true")
  elif wishblob.sentiment.polarity < 0:
    print("No chance this will come to pass")
  elif len(wish) > 15 and len(wish)<25:
    print("You should ask again")
  elif len(wish)>25:
    print("Yes, it will happen")
  elif wishblob.sentiment.subjectivity > 0.5:
    print("You are asking too much")
  elif wishblob.sentiment.subjectivity < 0.5:
    print("The wish will come true in 5 years.")
  else:
    random.choice(wishlist)

main()

  
