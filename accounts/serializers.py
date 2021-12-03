from rest_framework import serializers

from accounts.models import Adress, User


class AdressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adress
        fields = '__all__'
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }


class UserSerializer(serializers.ModelSerializer):

    adress = AdressSerializer(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'is_superuser', 'adress']

        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        adress_serialized = AdressSerializer(data=validated_data.pop('adress'))
        adress_serialized.is_valid(raise_exception=True)
        adress = adress_serialized.save()

        return User.objects.create_user(**validated_data, adress=adress)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
