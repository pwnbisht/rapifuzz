from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = [
            "id", "email", "password", "first_name", "last_name",
            "country_code", "mobile", "address", "country",
            "state", "city", "pin_code", "fax", "phone", 
            "is_staff", "is_active", "created_at", "updated_at",
        ]
        read_only_fields = ['id']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "This email is already registered."
            )
        return value
    
    def validate_mobile(self, value):
        """Ensure mobile contains only digits."""
        if not value.isdigit():
            raise serializers.ValidationError(
                "Mobile number must contain only digits."
            )
        if User.objects.filter(mobile=value).exists():
            raise serializers.ValidationError(
                "This mobile is already registered."
            )
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        return user
    

class ArtistLoginSerializer(serializers.Serializer):
    """
    Serializer for handling artist login.

    This serializer is responsible for validating the email and password
    during the login process.
    """
    email = serializers.EmailField()
    password = serializers.CharField(
        style={"input_type": "password"},
        trim_whitespace=False,
    )