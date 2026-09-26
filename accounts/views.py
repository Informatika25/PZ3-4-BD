from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course
from django.http import HttpResponse
# Create your views here.


@login_required
def profile(request):
    return render(request, "profile.html")


@login_required
def course_list(request):
    courses = Course.objects.select_related('department').all()
    return render(
    request,
    'course_list.html',
{
        'courses': courses,
        }
    )