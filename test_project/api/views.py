from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response


class ReviewClassification(APIView):
    def post(self, request):
        if not 'text' in data:
            return Response('no text in payload', status=400)
        data = request.data
        text = data['text']
        model = ApiConfig.model
        text_stemmed = ApiConfig.stem_text(text)
        if text_stemmed == '':
            return Response('no words in text', status=400)
        result = model.predict([text])
        result_dict = {'score': result, 'type' : 'positive' if result > 5 else 'negative'}
        return Response(result_dict, status=200)
