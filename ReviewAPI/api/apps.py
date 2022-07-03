import os
import joblib
from django.apps import AppConfig
from django.conf import settings
from sklearn.base import BaseEstimator, TransformerMixin
from nltk.stem.porter import PorterStemmer
import re

class TextTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        self.stemmer = PorterStemmer()
        return self

    def formatting(self, text):
        words = re.sub('[^a-zA-Z]', ' ', text).lower().split()
        words_stemmed = [self.stemmer.stem[word] for word in words]
        return ' '.join(words_stemmed)

    def transform(self, X):
        X_copy = X.copy()
        return X_copy.apply(self.formatting)


class ApiConfig(AppConfig):
    name = 'api'
    transformer_file = os.path.join(settings.MODELS, 'transformer.joblib')
    model_file = os.path.join(settings.MODELS, 'final_pipeline.joblib')
    TextTransformer = joblib.load(transformer_file)
    model = joblib.load(model_file)
