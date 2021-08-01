# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 01:19:57 2021

@author: akanksh.belchada
"""


import nltk
# nltk.download()

paragraph="Twenty years I spent in ISRO. I was given the opportunity to be the project director for India’s first satellite launch vehicle, SLV3. The one that launched Rohini. These years played a very important role in my life of a scientist. After my ISRO years, I joined DRDO and got a chance to be the part of India’s guided missile program. It was my second bliss when Agni met its mission requirements in 1994.The Department of Atomic Energy and DRDO had this tremendous partnership in the recent nuclear tests, on May 11 and 13. This was the third bliss. The joy of participating with my team in these nuclear tests and proving to the world that India can make it, that we are no longer a developing nation but one of them. It made me feel very proud as an Indian. The fact that we have now developed for Agni a re-entry structure, for which we have developed this new material. A very light material called carbon-carbon.One day an orthopedic surgeon from Nizam Institute of Medical Sciences visited my laboratory. He lifted the material and found it so light that he took me to his hospital and showed me his patients. There were these little girls and boys with heavy metallic calipers weighing over three kilograms each, dragging their feet around.He said to me: Please remove the pain of my patients. In three weeks, we made these floor reaction orthosis 300-gram calipers and took them to the orthopedic center. The children didn’t believe their eyes. From dragging around a three kg load on their legs, they could now move around! Their parents had tears in their eyes. That was my fourth bliss!Why is the media here so negative? Why are we in India so embarrassed to recognise our own strengths, our achievements? We are such a great nation."
sentences=nltk.sent_tokenize(paragraph)
print(sentences)

#Tokenization
words=nltk.word_tokenize(paragraph)


#Stemming
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

stemmer=PorterStemmer()

print((stopwords.words("english")))

for i in range(len(sentences)):
    words=nltk.word_tokenize(sentences[i])
    words=[stemmer.stem(word) for word in words if word not in (stopwords.words('english'))]
    sentences[i]=' '.join(words)
print(sentences[0])
print(sentences[1])
print(sentences[2])

#Lemmatization
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

Lemmatizer=WordNetLemmatizer()
paragraph="Twenty years I spent in ISRO. I was given the opportunity to be the project director for India’s first satellite launch vehicle, SLV3. The one that launched Rohini. These years played a very important role in my life of a scientist. After my ISRO years, I joined DRDO and got a chance to be the part of India’s guided missile program. It was my second bliss when Agni met its mission requirements in 1994.The Department of Atomic Energy and DRDO had this tremendous partnership in the recent nuclear tests, on May 11 and 13. This was the third bliss. The joy of participating with my team in these nuclear tests and proving to the world that India can make it, that we are no longer a developing nation but one of them. It made me feel very proud as an Indian. The fact that we have now developed for Agni a re-entry structure, for which we have developed this new material. A very light material called carbon-carbon.One day an orthopedic surgeon from Nizam Institute of Medical Sciences visited my laboratory. He lifted the material and found it so light that he took me to his hospital and showed me his patients. There were these little girls and boys with heavy metallic calipers weighing over three kilograms each, dragging their feet around.He said to me: Please remove the pain of my patients. In three weeks, we made these floor reaction orthosis 300-gram calipers and took them to the orthopedic center. The children didn’t believe their eyes. From dragging around a three kg load on their legs, they could now move around! Their parents had tears in their eyes. That was my fourth bliss!Why is the media here so negative? Why are we in India so embarrassed to recognise our own strengths, our achievements? We are such a great nation."
sentences=nltk.sent_tokenize(paragraph)

for i in range(len(sentences)):
    words=nltk.word_tokenize(sentences[i])
    words=[Lemmatizer.lemmatize(word) for word in words if word not in (stopwords.words('english'))]
    sentences[i]=' '.join(words)
print(sentences[0])
print(sentences[1])
print(sentences[2])


''''Illustration'''
string='Historical'
print(Lemmatizer.lemmatize(string),stemmer.stem(string))

#Bag of Words
paragraph="Twenty years I spent in ISRO. I was given the opportunity to be the project director for India’s first satellite launch vehicle, SLV3. The one that launched Rohini. These years played a very important role in my life of a scientist. After my ISRO years, I joined DRDO and got a chance to be the part of India’s guided missile program. It was my second bliss when Agni met its mission requirements in 1994.The Department of Atomic Energy and DRDO had this tremendous partnership in the recent nuclear tests, on May 11 and 13. This was the third bliss. The joy of participating with my team in these nuclear tests and proving to the world that India can make it, that we are no longer a developing nation but one of them. It made me feel very proud as an Indian. The fact that we have now developed for Agni a re-entry structure, for which we have developed this new material. A very light material called carbon-carbon.One day an orthopedic surgeon from Nizam Institute of Medical Sciences visited my laboratory. He lifted the material and found it so light that he took me to his hospital and showed me his patients. There were these little girls and boys with heavy metallic calipers weighing over three kilograms each, dragging their feet around.He said to me: Please remove the pain of my patients. In three weeks, we made these floor reaction orthosis 300-gram calipers and took them to the orthopedic center. The children didn’t believe their eyes. From dragging around a three kg load on their legs, they could now move around! Their parents had tears in their eyes. That was my fourth bliss!Why is the media here so negative? Why are we in India so embarrassed to recognise our own strengths, our achievements? We are such a great nation."
sentences=nltk.sent_tokenize(paragraph)



#Cleaning the text data
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
lemmatizatizer=WordNetLemmatizer()
corpus=[]
paragraph="Twenty years I spent in ISRO. I was given the opportunity to be the project director for India’s first satellite launch vehicle, SLV3. The one that launched Rohini. These years played a very important role in my life of a scientist. After my ISRO years, I joined DRDO and got a chance to be the part of India’s guided missile program. It was my second bliss when Agni met its mission requirements in 1994.The Department of Atomic Energy and DRDO had this tremendous partnership in the recent nuclear tests, on May 11 and 13. This was the third bliss. The joy of participating with my team in these nuclear tests and proving to the world that India can make it, that we are no longer a developing nation but one of them. It made me feel very proud as an Indian. The fact that we have now developed for Agni a re-entry structure, for which we have developed this new material. A very light material called carbon-carbon.One day an orthopedic surgeon from Nizam Institute of Medical Sciences visited my laboratory. He lifted the material and found it so light that he took me to his hospital and showed me his patients. There were these little girls and boys with heavy metallic calipers weighing over three kilograms each, dragging their feet around.He said to me: Please remove the pain of my patients. In three weeks, we made these floor reaction orthosis 300-gram calipers and took them to the orthopedic center. The children didn’t believe their eyes. From dragging around a three kg load on their legs, they could now move around! Their parents had tears in their eyes. That was my fourth bliss!Why is the media here so negative? Why are we in India so embarrassed to recognise our own strengths, our achievements? We are such a great nation."
sentences=nltk.sent_tokenize(paragraph)
    
for i in range(len(sentences)):
    review=re.sub('[^a-zA-Z]',' ',sentences[i])
    review=review.lower()
    review=review.split()
    review=[Lemmatizer.lemmatize(word) for word in review if word not in (stopwords.words('english'))]
    review=' '.join(review)
    corpus.append(review)
print(corpus)

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
x=cv.fit_transform(corpus).toarray()

print(x)


#TF-IDF ( Term frequency - Inverse document Frequency )
from sklearn.feature_extraction.text import TfidfVectorizer
tfidfv=TfidfVectorizer()
x2=tfidfv.fit_transform(corpus).toarray()
print(x2)