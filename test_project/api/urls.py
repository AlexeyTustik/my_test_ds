from django.urls import path
from .views import ReviewClassification

urlpatterns = [
	path('review/', ReviewClassification.as_view(), name='review_classification')
]
