from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from textblob.classifiers import NaiveBayesClassifier


#Go to rotten tomatoes 
#Get 5 pos reviews of pos and get 5 neg reviewa
# Use the NaiveBayes Analyzer to see how accurate it is 
# Use the training method to improve it. 
import nltk

try:
  nltk.data.find("tokenizers/punkt")
  nltk.data.find("taggers/averaged_perceptron_tagger")
  nltk.data.find("corpora/movie_reviews")
except LookupError:
  nltk.download('punkt')
  nltk.download('averaged_perceptron_tagger')
  nltk.download('movie_reviews')

filename = "reviews.txt"
file = open(filename, "r")

data = file.readlines()
file.close()

with open('training.json', 'r') as file:
  cl = NaiveBayesClassifier(file, format="json")

print(cl.classify("I hate this thing!"))
print(cl.classify("This new design needs lots of improvement"))
print(cl.classify("I have no problems with this at all!"))


print(cl.prob_classify("I hate this thing!").prob("pos"))
print(cl.prob_classify("I hate this thing").prob("neg"))

print(cl.prob_classify("I hate this thing!").prob("pos"))
print(cl.prob_classify("This new design needs lots of improvement").prob("neg"))
print(cl.prob_classify("I have no problems with this at all!").prob("pos"))


print(cl.prob_classify("I love this movie").prob("pos"))
sentence = TextBlob("I have no problems with this at all!")
print(sentence.sentiment)
'''
index = 1
for line in data:
  text = TextBlob(line, analyzer=NaiveBayesAnalyzer())
  #text = TextBlob(line)
  senti = text.sentiment
  print(str(index)+ " "+str(senti))
  file.write(str(index)+", "+str(senti)+"\n")
  index += 1 

file.close()
'''

#list of sentences
#seperate list of sentiment for 49 reveiws
