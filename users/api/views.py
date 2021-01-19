from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from users.models import Users

from users.api.serializers import UserSerializer

# create account


@api_view(['POST', ])
def registration_view(request):
    serializer = UserSerializer(data=request.data)
    response = {}
    if serializer.is_valid():
        account = serializer.save()
        # token = Token.objects.create(user=account)
        response['status'] = 'success'
        response['message'] = 'account registered successfully'
        # response['token'] = token.key

    else:
        data = serializer.errors
    return Response(response)

# get active veterinary officers


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def active_officers(request):
    users = Users.objects.all().filter(is_active=True).exclude(is_superuser=True)
    serialized_users = UserSerializer(users, many=True)
    context = {
        "status": "success",
        "data": serialized_users.data
    }
    return Response(context)

# Deactivate officer


@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def deactivate(request, id):
    obj, created = Users.objects.update_or_create(
        pk=id,
        defaults={"is_active": False},
    )
    context = {
        "status": "success",
        "message": "deactivated"
    }
    return Response(context)


# update veterinary details
@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def update_view(request, id):
    obj, created = Users.objects.update_or_create(
        id=id,
        defaults={"name": request.data['name'], "county": request.data['county'],
                  "id_no": request.data['id_no'], "phone_number": request.data['phone_number']},
    )
    context = {
        "status": "success",
        "message": "updated successfully"
    }
    
    return Response(context)
    
