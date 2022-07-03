import re
from sklearn.base import BaseEstimator, TransformerMixin
from nltk.stem import PorterStemmer

class TextTransformer(BaseEstimator, TransformerMixin):
  def fit(self, X, y=None):
    self.stemmer = PorterStemmer()
    return self
  
  def formatting(self, text):
    words = re.sub('[^a-zA-Z]',' ', text).lower().split()
    words_stemmed = [self.stemmer.stem(word) for word in words] 
    return ' '.join(words_stemmed)

  def transform(self, X):
    X_copy = X.copy()
    return X_copy.apply(self.formatting)
