from rest_framework import serializers, exceptions
from django.contrib.auth.models import User

class UserSignupSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(label='Username')
    email = serializers.EmailField(label="Email Address")
    password1 = serializers.CharField(label="Password", write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(label="Confirm Password", write_only=True, style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'id')
        extra_kwargs = {"id": {"read_only": True}}

    def save(self, request):
        username = request.data.get("username")
        password1 = request.data.get("password1")
        password2 = request.data.get("password2")
        email = request.data.get("email")

        if password1 != password2:
            raise exceptions.ValidationError("Invalid password confirmation")

        try:
            user = User.objects.create_user(email=email, username=username, password=password1)
        except Exception as e:
            raise exceptions.ValidationError("This user already exists")

        user.save()
        return user  