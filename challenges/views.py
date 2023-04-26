from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

# Create your views here.

def monthly_challenge(request,month):
    challenge_text = None
    if month =="January":
        challenge_text = "Eat no meat for entrie month!"
    elif month =="Febraury":
        challenge_text ="Walk for atleast 20 minutes every day!"
    elif month == "march":
        challenge_text = "Learn Django for atleast 20 min every day!"
    else:
        return HttpResponseNotFound("This month is not supported!")
        
    return HttpResponse(challenge_text)