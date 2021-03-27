from django.contrib import admin

from .models import TeamRegister,UserProfile,Schedule


class TeamRegisterAdmin(admin.ModelAdmin):
    fields = ['Team_title',"Team_slug",'Team_fee','Captain_No']
    list_display = ('Team_title', 'Captain_No','Team_fee')
admin.site.register(TeamRegister, TeamRegisterAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    fields = ['play_to','Username', 'AadhaarNo', 'Age','Captain','Wicket_keeper']
    list_display = ('Username', 'play_to')
admin.site.register(UserProfile, UserProfileAdmin)

class ScheduleAdmin(admin.ModelAdmin):
    fields = ['Team1','Team2', 'Winning_status', 'Schedule_time']
    list_display = ('Team1','Team2', 'Winning_status', 'Schedule_time')
admin.site.register(Schedule, ScheduleAdmin)