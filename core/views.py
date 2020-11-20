from django.shortcuts import render, get_object_or_404
from .models import Player, Master

# Create your views here.

def result(request,pk):
    ctx = {}
    player=get_object_or_404(Player,pk=pk)
    if request.method=="POST":
        if request.POST['choice1']=='1' or request.POST['choice1']=='2':
            if request.POST["choice1"]=="1":
                player.choice1=True
                player.save()
            return render(request, 'core/choice2.html',{'player':player})

        if request.POST['choice2']=='1' or request.POST['choice2']=='2':
            if request.POST["choice2"]=="1":
                player.choice2=True
                player.save()
            return render(request, 'core/choice3.html',{'player':player})

        if request.POST['choice3']=='1' or request.POST['choice3']=='2':
            if request.POST["choice3"]=="1":
                player.choice3=True
                player.save()
            return render(request, 'core/choice4.html',{'player':player})

        if request.POST['choice4']=='1' or request.POST['choice4']=='2':
            if request.POST["choice4"]=="1":
                player.choice4=True
                player.save()
            return render(request, 'core/choice5.html',{'player':player})
        
        if request.POST['choice5']=='1' or request.POST['choice5']=='2':
            if request.POST["choice5"]=="1":
                player.choice5=True
                player.save()
            return render(request, 'core/choice6.html',{'player':player})

        if request.POST['choice6']=='1' or request.POST['choice6']=='2':
            if request.POST["choice6"]=="1":
                player.choice6=True
                player.save()
            return render(request, 'core/choice7.html',{'player':player})

        if request.POST['choice7']=='1' or request.POST['choice7']=='2':
            if request.POST["choice7"]=="1":
                player.choice7=True
                player.save()
            return render(request, 'core/choice8.html',{'player':player})

        if request.POST['choice8']=='1' or request.POST['choice8']=='2':
            if request.POST["choice8"]=="1":
                player.choice8=True
                player.save()
            return render(request, 'core/choice9.html',{'player':player})

        if request.POST['choice9']=='1' or request.POST['choice9']=='2':
            if request.POST["choice9"]=="1":
                player.choice9=True
                player.save()
            return render(request, 'core/choice10.html',{'player':player})

        if request.POST['choice10']=='1' or request.POST['choice10']=='2':
            if request.POST["choice10"]=="1":
                player.choice10=True
                player.save()
            return render(request, '')
    
    else:
        player = get_object_or_404(Master, id=1)
        ctx['player'] = player
        return render(request, 'core/choice1.html', ctx)