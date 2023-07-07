from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
import datetime

# Create your views here.
comments = []

class Commentform(forms.Form):
    
    new_comment = forms.CharField(label="Add your comment", min_length=2)


def Commentlist(request):
   
   
    if request.method == "POST":
        form = Commentform(request.POST)

        
        if form.is_valid():
            
            comment = form.cleaned_data["new_comment"]
           
        
            comments.append(comment)
            date = datetime.datetime.now()
            comments.append(date)
     
            
            
            return HttpResponseRedirect(reverse("mycomments"))
        else:
            return render(request, 'comment/index.html', {"form": form})
    length = len(comments)
    return render(request, "comment/index.html", {"comments":comments, "form":Commentform(), "length":length})




