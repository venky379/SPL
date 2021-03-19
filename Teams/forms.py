from .models import UserProfile,TeamRegister
from django.forms import ModelForm
from django.core.exceptions import ValidationError
class RegisterForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        
class TeamRegisterForm(ModelForm):
    class Meta:
        model = TeamRegister
        fields = ['Team_title','Team_fee','Captain_No']

    def clean(self):
        team_title = self.cleaned_data.get('Team_title')
        team_inst = None
        try:
            team_inst = TeamRegister.objects.get(Team_title=team_title)
        except Exception as e:
            pass
        if team_inst:
            raise ValidationError('Team name already registered')
        else:
            pass
       
        # if not self.instance.image == image:
        #     # validate image
        # return None
        
