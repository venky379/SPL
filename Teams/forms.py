from .models import UserProfile,TeamRegister
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from django import forms
class RegisterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 
    class Meta:
        model = UserProfile
        fields = '__all__'
        
class TeamRegisterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TeamRegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 

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
        
class scheduleForm(forms.Form):
    subject = forms.CharField(max_length=100, help_text='100 characters max.')
    message = forms.CharField()
    sender = forms.EmailField(help_text='A valid email address, please.')
    cc_myself = forms.DateField(required=False)
