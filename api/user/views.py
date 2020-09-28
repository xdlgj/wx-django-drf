from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        print(request.data)
        return Response({"status": True})


