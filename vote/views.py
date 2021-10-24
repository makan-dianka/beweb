from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import MemberForm
from . models import Member

def home(request):
    return render(request, 'vote/home.html')

def vote(request):
    nom_dispo = Member.objects.all()
    names = []
    if request.method=="POST":
        form = MemberForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get("Votre_nom") #request.POST.get("Votre_nom")
            for name in nom_dispo:
                names.append(name.Votre_nom)
            if username in names:
                message =  (f"Hello {username}, vous avez déjà voté !")
                return render(request, "vote/vote.html", {'message':message, 'form':form})
            else:
                form.save()
                return redirect(f"/successful/{username}/")
    else:
        form = MemberForm
    context = {'form':form}
    return render(request, 'vote/vote.html', context)

def success(request, name):
    obj = Member.objects.get(Votre_nom=name)
    return render(request, 'vote/success.html', {'obj':obj})

def scrutin(request):
    obj = Member.objects.all()
    total = len(obj)
    return render(request, 'vote/scrutin.html', {'total':total}) 

def voteurs(request):
    obj = Member.objects.all()
    total = len(obj)
    return render(request, 'vote/voteurs.html', {'total':total, 'members':obj})