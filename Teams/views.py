# views.py
from django.shortcuts import render, redirect
# from .forms import Accounts
from .forms import RegisterForm, TeamRegisterForm, scheduleForm
from .models import TeamRegister, UserProfile,Schedule

# Create your views here.
def home(response):
    team_qury = TeamRegister.objects.all()
    total_fee = 0
    for i in team_qury:
        total_fee += int(i.Team_fee)
    return render(response, "home.html", {"team_qury":team_qury,"total_fee":total_fee})
def feesummary(response):
    team_qury = TeamRegister.objects.all()
    total_fee = 0
    for i in team_qury:
        total_fee += int(i.Team_fee)
    return render(response, "feesummary.html", {"team_qury":team_qury,"total_fee":total_fee})

def schedule(response):
    teams_list = TeamRegister.objects.filter(Team_fee__gte=500)
    schedule_list = Schedule.objects.all()
    team_qury = TeamRegister.objects.all()
    scheduled_list = []
    for i in schedule_list:
        scheduled_list.append(i.Team1)
        scheduled_list.append(i.Team2)
    not_scheduled_list = []
    for i in teams_list:
        if i.Team_title in scheduled_list:
            pass
        else:
            not_scheduled_list.append(i.Team_title)
    if response.POST:
        Schedule.objects.create(Team1 = response.POST['team1'], Team2 = response.POST['team2'], Schedule_time = response.POST['datetime'])
        return redirect("/schedule")
    if response.GET and response.GET['Actions'] == 'Delete':
        Schedule.objects.filter(id = response.GET['id']).delete()
        return redirect("/schedule")
    return render(response, "schedule.html", {"teamnames":team_qury,'schedule_list':schedule_list,'not_scheduled_list':not_scheduled_list})

def player_list(response):
    player_list = UserProfile.objects.all()
    team_qury = TeamRegister.objects.all()
    return render(response, "player_list.html", {"player_list":player_list,"teamnames":team_qury,})


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
        # user_inst.play_to=response.POST.get('play_to')
        user_inst.Username=response.POST.get('Username')
        user_inst.AadhaarNo=response.POST.get('AadhaarNo')
        user_inst.Age=response.POST.get('Age')
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
        return render(response, "userregister.html", {"form":form,"usernames":usernames,"team_id":team_inst,"user_inst":user_inst})

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
        return render(response, "teamregister.html", {"form":form,"teamnames":teamnames,'total_fee':total_fee,"team_inst":team_inst})