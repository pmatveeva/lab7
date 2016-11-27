from django.shortcuts import render, redirect
from shop.models import Category, Item
from django.views import View
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth.hashers import make_password
from django.contrib import auth
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='',login_url='/login')
def index(request):
    return render(request, 'index.html', {'var_name': request.user.username})


@login_required(redirect_field_name='',login_url='/login')
def shopping(request):
    data = Category.objects.all()
    return render(request, 'product.html', context={'menu': data, 'var_name': request.user.username})


class NewView(View):
    def get(self, request):
        data_search_n = Item.objects.filter(category_id=1).all()
        if len(data_search_n) == 0:
            return render(request, 'search-empty.html', {'var_name': request.user.username})
        else:
            return render(request, 'search.html', context={'search': data_search_n, 'var_name': request.user.username})


class BasicView(View):
    def get(self, request):
        data_search_b = Item.objects.filter(category_id=2).all()
        if len(data_search_b) == 0:
            return render(request, 'search-empty.html')
        else:
            return render(request, 'search.html', context={'search': data_search_b,'var_name':request.user.username})


class SaleView(View):
    def get(self, request):
        data_search_n = Item.objects.filter(category_id=3).all()
        if len(data_search_n) == 0:
            return render(request, 'search-empty.html')
        else:
            return render(request, 'search.html', context={'search': data_search_n, 'var_name': request.user.username})


class RegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','id':'username', 'placeholder':'Enter login',}),\
        min_length=5, label='Login:')
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control','id':'name', 'placeholder':'Enter name',}),\
        max_length=30, label='Name:')
    surname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'surname', 'placeholder': 'Enter surname', }), \
        max_length=30, label='Surname:')
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Enter email', })
    )
    password = forms.CharField(min_length=8, label='Password:', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'password', 'placeholder': 'Enter password', }))
    password2 = forms.CharField(min_length=8, label='Confirm password:', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'password2', 'placeholder': 'Confirm password', }))

    def clean_password2(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')
        if p1 != p2:
            raise forms.ValidationError ('Passwords does not match')

    def save(self):
        u = User()
        u.username = self.cleaned_data.get('username')
        u.password = make_password(self.cleaned_data.get('password'))
        u.first_name = self.cleaned_data.get('name')
        u.last_name = self.cleaned_data.get('surname')
        u.email = self.cleaned_data.get('email')
        u.is_staff = False
        u.is_active = True
        u.is_superuser = False
        u.save()

    def clean_username(self):
        username=self.cleaned_data.get('username')
        try:
            u=User.objects.get(username=username)
            raise forms.ValidationError('This login already uses')
        except User.DoesNotExist:
            return username


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        return render(request, 'registration.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def log(request):
    errors = []
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username:
            errors.append('Input login')
        elif not password:
            errors.append('Input password')
        else:
            user = authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                if not request.POST.get('remember'):
                    request.session.set_expiry(0)
                return redirect('/')
            else:
                errors.append('Wrong login or password')
    return render(request, 'login.html', {'errors': errors})


def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


