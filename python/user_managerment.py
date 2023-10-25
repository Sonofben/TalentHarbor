from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        first_name = data['first_name']
        last_name = data['last_name']
        password = data['password']
        email = data['email']

        # Check if the user with the given email already exists
        existing_user = User.objects.filter(email=email).first()
        if existing_user:
            return JsonResponse({'message': 'User with this email already exists.'}, status=400)

        # Create a new user with the provided information
        user = User(first_name=first_name, last_name=last_name, email=email, username=email)
        user.set_password(password)
        user.save()
        login(request, user)

        return JsonResponse({'message': 'User registered and logged in successfully!'})
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data['email']
        password = data['password']

        # Authenticate the user email and password
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful!'})
        else:
            return JsonResponse({'message': 'Login failed. Input Correct email and password.'}, status=401)
# User Logout
@csrf_exempt
@login_required
def user_logout(request):
    logout(request)
    return JsonResponse({'message': 'Logged out successfully!'})
# Get User Profile
@csrf_exempt
@login_required
def get_user_profile(request):
    user = request.user
    serialized_user = serializers.serialize('json', [user])
    return JsonResponse({'user': serialized_user})