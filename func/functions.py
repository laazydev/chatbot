# Collection of functions from functions.ipynb

## Import Libraries
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from tabulate import tabulate


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

    # Starts with 0
    if number[0] == '0':
        number = number[1:]
    elif number[0] == '+':
        if number[1:3] == '44':
            number = number[3:]
            # This works
    elif number[0:2] == '44':
        number = number[2:]
    
    if len(number) == 10:
        return 1, number
    else:
        return 0, number

def negationCheck(text):
    negations = ["dont", "not", "never"]
    for negs in negations:
        if negs in text:
            return True
        else:
            return False

def isOrder(text):
    orderTriggers = ['want', 'buy', 'order']
    for ords in orderTriggers:
        if ords in text:
            return True
        else:
            return False

def isPizza(text):
    if 'pizza' in text:
        return True
    else:
        return False

def getPizzaList(data):
    testinggg = []

    for j in range(len(data)):
        testinggg.append([data.iloc[j][1].capitalize(), data.iloc[j][10], data.iloc[j][3]])

    return tabulate(testinggg, headers=["Pizza name", 'Price', 'Calories'])

def boolConfirm(text):
    positive_bool = ['yes', 'yesh', 'yeah', 'yup', 'yea', 'yuh']
    negative_bool= ['no', 'noh', 'nope', 'nah', 'naur', 'naw']

    posFlag = False
    negFlag = False

    for pos in positive_bool:
        if pos in text:
            posFlag = True
        
    for neg in negative_bool:
        if neg in text:
            negFlag = True

    if posFlag == True and negFlag == False:
        # Positive
        return 1
    elif posFlag == False and negFlag == True:
        # Negative
        return -1
    else:
        # Not understandable
        return 0

def getReceipt(orders, header=['Order Details', 'Price']):
    return tabulate(orders, header)