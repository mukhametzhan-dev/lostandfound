from django.views.decorators.csrf import csrf_exempt
from pyexpat.errors import messages
from django.views.generic import ListView
from .forms import ItemForm, ProfileEditForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import (get_object_or_404, render, redirect)
from django.contrib import messages
from .models import *
from django.db.models import Q


class IndexView(ListView):
    template_name = 'index.html'
    model = Item
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.all()
@login_required
def profile_view(request):
    found_items = Item.objects.filter(found_by=request.user.username)
    lost_items = Item.objects.filter(creator_username=request.user.username).exclude(found_by=request.user.username)
    context = {
        'found_items': found_items,
        'lost_items': lost_items,

    }
    return render(request, 'profile.html', context)
@login_required
def FoundView(request):
    item = get_object_or_404(Item, pk=request.POST['item'])
    item.found_by = request.user.username
    item.save()
    return redirect('index')


@login_required
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.creator_username = request.user.username
            item.save()
            return redirect('index')  
    else:
        form = ItemForm()
    return render(request, 'item_form.html', {'form': form})


@login_required
def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item.html', {'item': item})


@login_required
def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item updated successfully! ')
            return render(request, 'index.html', {'error_message': 'Item updated successfully!'})
            return redirect('index')
        
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_form.html', {'form': form})


@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Item deleted successfully! ')
        return render(request, 'index.html', {'error_message': 'Item deleted successfully!'})
        return redirect('index')
    
    return render(request, 'item_delete.html', {'item': item, 'confirm_delete': True})


def my_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("User logged in successfully")
            return redirect('index')
        else:
            print("Invalid login credentials")
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
        
    else:
        return render(request, 'login.html')


def my_registration_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            error_message = "This username is already taken"
            return render(request, 'registration.html', {'error_message': error_message})

        if pass1 != pass2:
            error_message = "Passwords didn't match!"
            return render(request, 'registration.html', {'error_message': error_message})

        myuser = User.objects.create_user(username, email, pass1)
        myuser.is_staff = True
        myuser.save()

        messages.success(request, "Your account has been signed up successfully!")
        return redirect('login')

    return render(request, "registration.html")

def gallery(request):
    context = {}

    return render(request, 'gallery.html')

def my_logout_view(request):
    logout(request)
    return redirect('login')


def search_items(request):
    query = request.GET.get('query')
    if query:
        items = Item.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    else:
        items = Item.objects.all()
    return render(request, 'search_results.html', {'items': items, 'query': query})


def about_us(request):
    return render(request, 'about.html')

# @login_required
# def profile(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#          ip = request.META.get('REMOTE_ADDR')
#     if request.method == 'POST':
#         u_form = ProfileEditForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             return redirect('profile')
#     else:
#         u_form = ProfileEditForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form,
#     }

#     return render(request, 'profile.html', context)

@login_required
def profile(request):
    found_items = Item.objects.filter(found_by=request.user.username)
    lost_items = Item.objects.filter(creator_username=request.user.username).exclude(found_by=request.user.username)

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    if request.method == 'POST':
        u_form = ProfileEditForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = ProfileEditForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'last_login_ip': ip,
        'found_items': found_items,
        'lost_items': lost_items,}
    

    return render(request, 'profile.html', context)
@login_required
def pic(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
    else:
        form = ProfileUpdateForm()
       # form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'profile.html', {'form': form})
@login_required
def update_profile_image(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile image updated successfully!")
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    
    return render(request, 'profile.html', {'form': form})
@csrf_exempt
def home(request):
    return render(request, 'home.html')