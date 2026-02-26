from django.shortcuts import render,redirect
from .forms import signupForm,ProfileUpdateForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required,permission_required
from rest_framework import viewsets, permissions
from .models import Todo
from .serializers import TodoSerializer

@login_required
def home(request):
    return render(request,'home.html',{'user':request.user})

def signup_view(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = signupForm()
    return render(request,'signup.html',{'form':form})


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request,'profile_update.html',{'form':form})

@permission_required('app1.is_staff',raise_exception=True)
def abc(request):
    return redirect('home')


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)