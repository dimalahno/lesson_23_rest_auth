from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .decorators import role_required
from .forms import CustomUserCreationForm
from .models import Project


@login_required
@role_required(['admin', 'manager', 'user'])
def project_list(request):
    # Все могут видеть проекты
    # пример: список проектов
    ...

@login_required
@role_required(['admin'])
def manage_users(request):
    # Только админ
    ...

@login_required
@role_required(['admin', 'manager'])
def create_project(request):
    # Менеджер и админ создают проект
    if request.method == 'POST':
        # логика создания проекта
        pass
    return render(request, 'core/create_project.html')

@login_required
@role_required(['user'])
def complete_task(request, task_id):
    # Только обычный пользователь выполняют задание
    ...


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # авто-вход после регистрации
            return redirect('home')  # перенаправление после регистрации
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'core/home.html')


class ProjectCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Project
    fields = ['name', 'description']

    def test_func(self):
        return self.request.user.role in ['admin', 'manager']