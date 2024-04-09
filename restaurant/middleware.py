from django.shortcuts import redirect
from django.urls import reverse

class RedirectOn404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            return redirect(reverse('home_restaurant')) # Redirect to home page
        return response
