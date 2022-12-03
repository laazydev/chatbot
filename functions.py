# Collection of functions from functions.ipynb

## Import Libraries
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Download Stopword library from NLTK
nltk.download('stopwords')
stopwords = stopwords.words('english')

# Remove negation
stopwords.remove('not')
stopwords.remove('with')


## Function lists
def NewCustomer(name, phone, address):
    # Read the latest CSV
    df = pd.read_csv('database/customer.csv')
    
    # Get the last index, then plus 1
    newId = df.iloc[-1, 0] + 1
    data = {
        'id': newId,
        'name': name.lower(),
        'phone': str(phone),
        'address': address
    }

    # Convert the Dictionary to DataFrame
    toAppend = pd.DataFrame(data, index=[1])

    # Append the dataframe to tht CSV
    toAppend.to_csv('database/customer.csv', mode='a', index=False, header=False)


def GetCustomer(phone):
    df = pd.read_csv('database/customer.csv')

    for idrange in range(len(df)):
        if df.iloc[idrange, 2] == int(phone):
            return df.iloc[idrange, 1], df.iloc[idrange, 3]
        else:
            pass

def checkPhone(number):
    # Error = 0
    # True = 1

    if number[0] == '0':
        number = number[1:]
    
    if len(number) == 10:
        return 1, number
    else:
        return 0, number

# Preprocess the intent
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

def checkNumber(text):
    oneTrigger = ['one', '1']
    for i in text:
        if i[1] == 'NUM':
            # Only allow one order at a time
            if i[0] in oneTrigger:
                return True
            else: 
                return False