from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.

# AJAX view to check if email exists
def check_email(request):
    email = request.GET.get('email', None)
    exists = User.objects.filter(email=email).exists()
    if not email or '@' not in email or '.' not in email.split('@')[-1]:
        return JsonResponse({'exists': exists, 'valid': False})
    else:
        return JsonResponse({'exists': exists, 'valid': True})
# AJAX view to check if username exists

def check_username(request):
    username = request.GET.get('username', None)
    exists = User.objects.filter(username=username).exists()
    return JsonResponse({'exists': exists})

# AJAX view to validate login credentials
def validate_login(request):
    username = request.GET.get('username')
    password = request.GET.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        return JsonResponse({'valid': True})
    else:
        return JsonResponse({'valid': False, 'message': 'Invalid username or password.'})

# View for the index page
@login_required
def index(request):
    return render(request, 'index.html')

def landingpage(request):
    show_modal = request.GET.get('show_modal')
    return render(request, 'landingpage.html', {'show_modal': show_modal})

# View for login
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return render(request, 'landingpage.html', {'show_modal': 'login_page'})

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return render(request, 'landingpage.html', {'show_modal': 'login_page'})
        else:
            login(request, user)
            messages.success(request, "Logged in Successfully!")
            return redirect('index')
    # For GET, show landing page with both modals
    return render(request, 'landingpage.html')

def signin(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'landingpage.html', {'show_modal': 'signin'})
        if not email or '@' not in email or '.' not in email.split('@')[-1]:
            messages.error(request, "Invalid email address!")
            return render(request, 'landingpage.html', {'show_modal': 'signin'})
        if not first_name or not last_name or not username or not password or not email:
            messages.error(request, "All fields are required!")
            return render(request, 'landingpage.html', {'show_modal': 'signin'})
        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long!")
            return render(request, 'landingpage.html', {'show_modal': 'signin'})
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken!")
            return render(request, 'landingpage.html', {'show_modal': 'signin'})

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account created Successfully! Please log in.")
        # Redirect to landingpage with login modal open
        return redirect("/?show_modal=login_page")
    # For GET, show landing page with both modals
    return render(request, 'landingpage.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect('landingpage')