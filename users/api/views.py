from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view

from users.api.serializers import UserSerializer

@api_view(['POST',])
def registration_view(request):
    serializer = UserSerializer(data=request.data)
    response = {}
    if serializer.is_valid():        
        account = serializer.save()
        token = Token.objects.create(user = account)
        response['status'] = 'success'
        response['message'] = 'account registered successfully'
        # response['token'] = token.key
        
    else:
        data = serializer.errors
    return Response(response)
