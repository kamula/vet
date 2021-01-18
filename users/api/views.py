from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from users.api.serializers import UserSerializer

@api_view(['POST',])
def registration_view(request):
    serializer = UserSerializer(data=request.data)
    response = {}
    if serializer.is_valid():
        account = serializer.save()
        response['status'] = 'success'
        response['message'] = 'account registered successfully'
    else:
        data = serializer.errors
    return Response(response)
