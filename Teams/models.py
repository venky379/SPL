from django.db import models
from django.template.defaultfilters import slugify # new

class TeamRegister(models.Model):
    Team_title = models.CharField(max_length=200)
    Team_slug = models.SlugField(null=False,blank=True, default='')
    Team_fee = models.CharField(max_length=200,null=False,blank=True,default=0)
    Captain_No = models.CharField(max_length=200,null=False,blank=True,default='')
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.Team_title
    def save(self, *args, **kwargs): # new
        if not self.Team_slug:
            self.Team_slug = slugify(self.Team_title)
        return super().save(*args, **kwargs)
        
class UserProfile(models.Model):
    play_to = models.ForeignKey(TeamRegister, on_delete=models.CASCADE,default='')
    Username = models.CharField(max_length=200)
    AadhaarNo = models.CharField(max_length=200,unique=True)
    Age = models.IntegerField(default=0,null=True)
    Captain = models.BooleanField(default=False)
    Wicket_keeper = models.BooleanField(default=False)

def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.Username

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

class Schedule(models.Model):
    Team1 = models.CharField(max_length=200)
    Team2 = models.CharField(max_length=200)
    Winning_status = models.CharField(max_length=200,null=False,blank=True,default='')
    Schedule_time = models.CharField(max_length=200,null=False,blank=True,default='')
    # Wicket_keeper = models.BooleanField(default=False)

def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.Team1