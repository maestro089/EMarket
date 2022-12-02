from .models import profile
from django.contrib.auth.models import User

def photo_user(request):
        return {profile.objects.filter(user = request.user)}

