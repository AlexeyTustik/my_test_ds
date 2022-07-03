from django.shortcuts import render
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response

class ReviewClassification(APIView):
	def post(self, request):
		data = request.data
		return Response(data, status=200)
