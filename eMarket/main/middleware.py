from asyncio.windows_events import NULL
from .models import profile


class ProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.user.is_authenticated:
            request.user_photo = profile.objects.get(user = request.user) 
        

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
