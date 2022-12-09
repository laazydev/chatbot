import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import math
import re
from collections import Counter
import difflib
import pandas as pd
from tabulate import tabulate

# Download Stopword library from NLTK
nltk.download('stopwords')
stopwords = stopwords.words('english')

# Remove negation
stopwords.remove('not')
stopwords.remove('with')

# Import database
pizza_df = pd.read_csv('pizza.csv', sep=';')

def preprocess(textinput):
    # Lower all characters
    textinput = textinput.lower()

    # Remove punctuations
    string.punctuation = string.punctuation + '-'
    text_filtered = ''.join([char for char in textinput if char not in string.punctuation])

    # Tokenize the word
    text_tokens = word_tokenize(text_filtered)

    # Remove stopword from the text
    tokens_without_sw = [word for word in text_tokens if word.lower() not in stopwords]

    # Removing any stopwords from the sentence
    filtered_sentence = (" ").join(tokens_without_sw)

    post = nltk.pos_tag(word_tokenize(filtered_sentence), tagset='universal') 
    return post

WORD = re.compile(r"\w+")

# Calculate the cosine similarity between two vectors
def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

# Return the text to vector
def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

def checkTypo(a, b):
    seq = difflib.SequenceMatcher(None, a, b)
    d = seq.ratio()*100
    return d

def getReco(text, dataframe=pizza_df):
    texttovec = text_to_vector(text)
    toReco = []

    for i in range(len(dataframe)):
        tempvec = text_to_vector(pizza_df.iloc[i][2].lower())
        stringvec = text_to_vector(text.lower())
        if get_cosine(tempvec, stringvec) != 0: toReco.append([pizza_df.iloc[i][1].capitalize(), pizza_df.iloc[i][10]])
        
    return tabulate(toReco, headers=['Pizza Name', 'Price'])
    
def getBill(pizzaOrder):
    totalPrice = 0
    pizza_df = pd.read_csv('pizza.csv', sep=';')
    for m in pizzaOrder:
        for n in range(len(pizza_df)):
            if pizza_df.iloc[n][1] == m:
                totalPrice += pizza_df.iloc[n][10]
    return totalPrice
