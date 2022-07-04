from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response


class ReviewClassification(APIView):
    def post(self, request):
        data = request.data
        if not 'text' in data:
            return Response('no text in payload', status=400)
        text = data['text']

        text_stemmed = ApiConfig.stem_text(text)
        model = ApiConfig.model
        if text_stemmed == '':
            return Response('no words in text', status=400)
        result = model.predict([text_stemmed])
        result_dict = {
            'score': result[0], 'type': 'positive' if result > 5 else 'negative'}
        return Response(result_dict, status=200)
