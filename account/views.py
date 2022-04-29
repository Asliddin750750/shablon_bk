from django.shortcuts import render
from rest_framework.views import APIView

from config.responses import ResponseSuccess


class MeView(APIView):
    def get(self, request):
        return ResponseSuccess({
            'hello': 'salom'
        })
