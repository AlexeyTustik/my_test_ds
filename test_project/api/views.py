from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response


class ReviewClassification(APIView):
    def post(self, request):
        data = request.data
        text = data['text']
        model = ApiConfig.model
        text_stemmed = ApiConfig.stem_text(text)
        result = model.predict([text])
        return Response(result, status=200)
