from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from . forms import SondageForm, CreateUserForm, MemberForm
from . models import Sondage, Member

def home(request):
    return render(request, 'vote/home.html')

def ajout(request):
    obj = Member.objects.all()
    if request.method=='POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MemberForm
    context = {'form':form, 'obj':obj}
    return render(request, 'vote/ajout.html', context)

def register(request):
    form = CreateUserForm
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vote:loginpage')
    context = {'form': form}
    return render(request, 'vote/acconts/registration/register.html', context)

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('vote:vote')
        else:
            messages.info(request, 'Votre nom ou mot de passe est incorrect')
    return render(request, 'vote/acconts/login/login.html')

def vote(request):
    nom_dispo = Sondage.objects.all()
    names = []
    if request.method=="POST":
        form = SondageForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("votre_nom") #request.POST.get("Votre_nom")
            for name in nom_dispo:
                names.append(name.votre_nom)
            if username in names:
                message =  (f"Hello {username}, vous avez déjà voté !")
                return render(request, "vote/vote.html", {'message':message, 'form':form})
            else:
                form.save()
                return redirect(f"/successful/")
    else:
        form = SondageForm
    context = {'form':form}
    return render(request, 'vote/vote.html', context)

def success(request):
    obj = Sondage.objects.all()
    candidat = Member.objects.all()
    context = {'obj': obj, 'candidats': candidat}
    return render(request, 'vote/success.html', context)

# def scrutin(request):
#     obj = Member.objects.all()
#     total = len(obj)
#     return render(request, 'vote/scrutin.html', {'total':total}) 

# def voteurs(request):
#     obj = Member.objects.all()
#     total = len(obj)
#     return render(request, 'vote/voteurs.html', {'total':total, 'members':obj})