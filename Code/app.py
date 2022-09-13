import pickle
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import word_tokenize
import re
import nltk
import string
from flask import Flask, render_template, url_for, flash, redirect, request

nltk.download('stopwords')
nltk.download('wordnet')

# Cleaning text 
def clean_text(text):
    text = str(text).lower() # Lowering the case
    text = re.sub('\[.*?\]', '', text) #Remove any text in the square brackets
    text = re.sub('https?://\S+|www\.\S+', '', text) # Remove any links present 
    text = re.sub('<.*?>+', '', text) # 
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text) # Remove punctuation
    text = re.sub('\n', '', text) # Removing the next line character
    text = re.sub('\w*\d\w*', '', text) # Removing the words contaitning numbers
    text = re.sub('[^a-zA-Z]', ' ', text)
    return text
# Text preprocessing
lemma = WordNetLemmatizer()
stemmer = PorterStemmer()
def preprocess(text):
    words = word_tokenize(text)
    words = [lemma.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    words = [stemmer.stem(word) for word in words]
    return " ".join(words)
def test(text, model, tfidf_vectorizer):
    text = clean_text(text)
    text = preprocess(text)
    text_vector = tfidf_vectorizer.transform([text])
    predicted = model.predict(text_vector)
    newmap = {0: 'fantasy', 1: 'science',2: 'crime', 3: 'history', 4: 'horror', 5: 'thriller', 6: 'psychology', 7: 'romance', 8: 'sports', 9: 'travel'}

    return newmap[predicted[0]]

file = open('bookgenremodel_svc.pkl', 'rb')
model = pickle.load(file)
file.close()

file1 = open('F:\\Projects\\Book_genre\\Code\\tfdifvector.pkl', 'rb')
tfidf_vectorizer = pickle.load(file1)
file1.close()

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST']) ## This is our homepage route 

def home():
    if request.method == 'POST':
        my_dict = request.form
        text = my_dict['summary']
        prediction = test(text, model, tfidf_vectorizer)
        return render_template('index.html', genre = prediction, text = str(text)[:100], showresult = True)
    return render_template('index.html')
@app.route("/about") ## This will go to our about page 
def about():
    return render_template('about.html', title = 'About')

if __name__ == "__main__":
    app.run(host = 'localhost', port=5000, debug = True)