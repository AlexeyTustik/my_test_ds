import joblib
import re
from django.apps import AppConfig
from django.conf import settings
from nltk.stem.porter import PorterStemmer


class ApiConfig(AppConfig):
    name = 'api'
    model = joblib.load(settings.MODEL)
    stemmer = PorterStemmer()

    def stem_text(text):
        words = re.sub('[^a-zA-Z]',' ', text).lower().split()
        words_stemmed = [ApiConfig.stemmer.stem(word) for word in words] 
        return ' '.join(words_stemmed)