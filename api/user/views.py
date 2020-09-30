from rest_framework.views import APIView
from rest_framework.response import Response


class LoginView(APIView):
    """
    用户登录
    """

    def post(self, request, *args, **kwargs):
        print(request.data)
        return Response({"status": True})


