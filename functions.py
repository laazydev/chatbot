# Collection of functions from functions.ipynb

## Import Libraries
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

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
