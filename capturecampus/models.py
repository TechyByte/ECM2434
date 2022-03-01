from django.db import models

# Create your models here.

class Team(models.Model):
    name= models.CharField(max_length=250)
    score_1= models.IntegerField(default=0)
    def getName(self):
        return self.name
    
    def __str__(self):
        return self.name
    def getTeamScore(self):
        return self.score_1


class Player(models.Model):
    team = models.ForeignKey("Team",  on_delete=models.CASCADE)
    name = models.CharField(max_length=250,default='Player')
    score =  models.IntegerField(default=0)
    def captured_flag(self):
        self.score += 1
        return self.name + " has gotten another flag " + str(self.score) +" "+ self.team.name + " has "+ str(self.team.score_1 + 1) + " points"
    
    def getTeamScore(self):
        return self.team.score_1    
    def getTeamName(self):
        return self.team.name
    def getTeam(self):
        return self.team
    def __str__(self):
        return self.name
