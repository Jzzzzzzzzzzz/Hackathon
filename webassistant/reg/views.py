from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import login as django_login
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))


# def login_view(request):
#
#     redirect_url = reverse('index')
#     if request.method == "GET":
#         if request.user.is_authenticated:
#              return redirect(redirect_url)
#         else:
#
#             return render(request, 'login.html')
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect(redirect_url)
#     return render(request, 'login.html', {"error": "Пользователь не найден"})

def login_view(request):
    redirect_url = reverse('index')  # URL для перенаправления после успешного входа

    if request.method == "GET":  # Если GET-запрос
        if request.user.is_authenticated:  # Если пользователь уже вошел
            return redirect(redirect_url)
        return render(request, 'login.html')  # Показываем страницу входа

    elif request.method == "POST":  # Если POST-запрос
        username = request.POST.get('username')  # Получаем логин
        password = request.POST.get('password')  # Получаем пароль

        user = authenticate(request, username=username, password=password)  # Проверяем пользователя

        if user is not None:  # Если пользователь найден
            login(request, user)  # Входим
            return redirect(redirect_url)
        else:  # Если пользователь не найден
            return render(request, 'login.html', {"error": "Пользователь не найден"})

    return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False) # Сначала создаём объект пользователя
            # user.role = form.cleaned_data['role'] # Устанавливаем роль
            user.save()   # Сохраняем пользователя в базу
            login(request,user) #логиним
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, "Registration.html", {'form': form})

