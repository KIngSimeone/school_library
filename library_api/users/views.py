from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from api_utility.views import success_response, paginated_response, created_response
from .serializers import AdminSerializer
from .utils import create_admin
# class HelloView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)

class AdminView(APIView):
    """
    List all Admins or create a new admin
    """
    def post(self, request):
        data = request.data
        first_name = data["first_name"]
        last_name = data["last_name"]
        user_name = data["user_name"]
        password = data["password"]

        admin = create_admin(first_name, last_name, user_name, password)
        if not admin:
            return Response({"message": "Admin creation failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = AdminSerializer(admin)
        data = serializer.data
        return created_response(message="successfully created admin", body=data)


