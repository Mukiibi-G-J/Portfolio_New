from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    profile = Profile.objects.all()[0]
    single_name = profile.full_name.split(" ")[1]
    print(single_name)
    skills = Skill.objects.all()
    return render(
        request,
        "index.html",
        {"profile": profile, "skills": skills, "single_name": single_name},
    )
