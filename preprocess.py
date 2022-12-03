import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download Stopword library from NLTK
nltk.download('stopwords')
stopwords = stopwords.words('english')

# Remove negation
stopwords.remove('not')
stopwords.remove('with')

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
