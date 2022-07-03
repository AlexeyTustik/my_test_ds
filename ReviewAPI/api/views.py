from django.shortcuts import render
from .apps import ApiConfig, TextTransformer
from rest_framework.views import APIView
from rest_framework.response import Response


class ReviewClassification(APIView):
	def post(self, request):
		data = request.data
        text = data['text']
        model = ApiConfig.model
        result = model.predict([text])
		return Response(result, status=200)
