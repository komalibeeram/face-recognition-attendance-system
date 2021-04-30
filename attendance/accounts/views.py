from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from . import models
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
# Create your views here.
def home(request):
    return render(request, template_name='base.html')

@login_required
def profile(request):
    if request.user.is_student:
        return render(request, 'accounts/student.html')
    else:
        return render(request, 'accounts/staff.html')