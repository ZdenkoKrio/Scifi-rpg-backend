from django.shortcuts import render


def home(request):
    """Render the home page with API documentation links."""
    return render(request, "home.html")
