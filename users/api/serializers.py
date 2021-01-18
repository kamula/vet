from django.db.models.base import Model
from rest_framework import serializers
from users.models import Users


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Users
        fields = ('name', 'email', 'county', 'id_no',
                  'phone_number', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = Users(
            name=self.validated_data['name'],
            email=self.validated_data['email'],
            county=self.validated_data['county'],
            id_no=self.validated_data['id_no'],
            phone_number=self.validated_data['phone_number']

        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError(
                {'password': 'passwords must match'})
        user.set_password(password)
        user.save()
        return user
