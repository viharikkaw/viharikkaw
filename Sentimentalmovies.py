import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet') 
nltk.download('movie_reviews')
from nltk.corpus import movie_reviews,stopwords 
from nltk.tokenize import word_tokenize 
import random
#list = [x for x in arr for y in arr.get()]
document=[(list(movie_reviews.words(field)),category) for category in movie_reviews.categories() for field in movie_reviews.fileids(category)]
all_words
