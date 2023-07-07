


#######
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
tasks = []

class Newform(forms.Form):
    new_task = forms.CharField(label="input task", min_length=2)
    emailtask = forms.EmailField(label="")
def task(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render (request, 'index.html', {'tasks': request.session["tasks"]})


def add(request):
    if request.method == "POST":
        form = Newform(request.POST)
        if form.is_valid():
            task= form.cleaned_data["new_task"]
            task2 = form.cleaned_data["emailtask"]
            request.session["tasks"] += [task]
            request.session["tasks"] += [task2]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "add.html",{"form": form})
    return render(request, "add.html", {"form":Newform()})