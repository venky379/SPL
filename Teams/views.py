# views.py
from django.shortcuts import render, redirect
# from .forms import Accounts
from .forms import RegisterForm, TeamRegisterForm
from .models import TeamRegister, UserProfile

# Create your views here.
def home(response):
    team_qury = TeamRegister.objects.all()
    total_fee = 0
    for i in team_qury:
        total_fee += int(i.Team_fee)
    return render(response, "home.html", {"total_fee":total_fee})

def team_register(response):
    form = TeamRegisterForm()
    teamnames = TeamRegister.objects.all()
    total_fee = 0
    for i in teamnames:
        total_fee += int(i.Team_fee)
    if response.method == "POST":
        form = TeamRegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/team_register")
        return render(response, "teamregister.html", {"form":form,"teamnames":teamnames,"total_fee":total_fee})
    else:
        return render(response, "teamregister.html", {"form":form,"teamnames":teamnames,"total_fee":total_fee})

def user_register(response,team_id):
    team_inst = TeamRegister.objects.get(id = team_id)
    form = RegisterForm(initial={"play_to":team_inst})
    usernames = UserProfile.objects.filter(play_to__id = team_id)
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/user_register/"+team_id)
        return render(response, "userregister.html", {"form":form,"usernames":usernames,"team_id":team_inst})
    else:
        return render(response, "userregister.html", {"form":form,"usernames":usernames,"team_id":team_inst})

def user_edit(response,team_id, user_id):
    team_inst = TeamRegister.objects.get(id = team_id)
    user_inst = UserProfile.objects.get(id = user_id)
    form = RegisterForm(instance = user_inst)
    usernames = UserProfile.objects.filter(play_to__id = team_id)
    if response.method == "POST":
        form = RegisterForm(response.POST)
        user_inst.Captain=response.POST.get('play_to')
        user_inst.Captain=response.POST.get('Username')
        user_inst.Captain=response.POST.get('AadhaarNo')
        user_inst.Captain=response.POST.get('Age')
        if response.POST.get('Captain'):
            user_inst.Captain= True 
        else:
            user_inst.Captain=False
        if response.POST.get('Wicket_keeper'):
            user_inst.Wicket_keeper= True 
        else:
            user_inst.Wicket_keeper=False
        user_inst.save()
        # if form.is_valid():
            # instance = form.save(commit=False)
            # user_inst.update(**instance)
            # form.save()
        return redirect("/user_register/"+team_id)
        # else:
        #     form = RegisterForm()
        return render(response, "userregister.html", {"form":form,"usernames":usernames,"team_id":team_inst})
    else:
        return render(response, "userregister.html", {"form":form,"usernames":usernames,"team_id":team_inst})

def team_edit(response,team_id):
    team_inst = TeamRegister.objects.get(id = team_id)
    form = TeamRegisterForm(instance=team_inst)
    teamnames = TeamRegister.objects.all()
    total_fee = 0
    for i in teamnames:
        total_fee += int(i.Team_fee)
    if response.method == "POST":
        form = TeamRegisterForm(response.POST)
        team_inst.Team_title=response.POST.get('Team_title')
        team_inst.Team_fee=response.POST.get('Team_fee')
        team_inst.Captain_No=response.POST.get('Captain_No')
        team_inst.save()
        return redirect("/team_register")
        return render(response, "teamregister.html", {"form":form,"teamnames":teamnames,'total_fee':total_fee})
    else:
        return render(response, "teamregister.html", {"form":form,"teamnames":teamnames,'total_fee':total_fee})