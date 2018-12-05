from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete).',
            'It is similar to traditional Django view.',
            'Gives you the most control over the logic.',
            'Is mapped mannually to URLs.'
        ]

        return Response({'message': 'This is an api message!', 'an_apiview': an_apiview})
