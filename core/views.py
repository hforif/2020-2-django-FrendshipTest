from django.shortcuts import render, redirect, get_object_or_404
from .models import Player, Master
from .forms import MasterForm
from django.urls import reverse

# Create your views here.

def result(request,pk):
    ctx = {}
    player=get_object_or_404(Master, pk=pk)
    if request.method=="POST":
        if player.current==1:
            if request.POST['choice1']=='1' or request.POST['choice1']=='2':
                if request.POST["choice1"]=="1":
                    player.choice1=True
                    player.save()
                player.current+=1
                player.save()
                return render(request, 'core/choice2.html',{'player':player})

        if player.current==2:
            if request.POST['choice2']=='1' or request.POST['choice2']=='2':
                if request.POST["choice2"]=="1":
                    player.choice2=True
                    player.save()
                player.current+=1
                player.save()
                return render(request, 'core/choice3.html',{'player':player})

        if player.current==3:
            if request.POST['choice3']=='1' or request.POST['choice3']=='2':
                if request.POST["choice3"]=="1":
                    player.choice3=True
                    player.save()
                player.current+=1
                player.save()
                return render(request, 'core/choice4.html',{'player':player})

        if player.current==4:
            if request.POST['choice4']=='1' or request.POST['choice4']=='2':
                if request.POST["choice4"]=="1":
                    player.choice4=True
                    player.save()
                player.current+=1
                player.save()
                return render(request, 'core/choice5.html',{'player':player})
        
        if player.current==5:
            if request.POST['choice5']=='1' or request.POST['choice5']=='2':
                if request.POST["choice5"]=="1":
                    player.choice5=True
                    player.save()
                player.current+=1
                player.save()
                return render(request, 'core/choice6.html',{'player':player})

        if player.current==6:
            if request.POST['choice6']=='1' or request.POST['choice6']=='2':
                if request.POST["choice6"]=="1":
                    player.choice6=True
                    player.save()
                player.current+=1
                player.save()
                return render(request, 'core/choice7.html',{'player':player})

        if player.current==7:
            if request.POST['choice7']=='1' or request.POST['choice7']=='2':
                if request.POST["choice7"]=="1":
                    player.choice7=True
                    player.save()
                player.current+=1
                player.save()
                return render(request, 'core/choice8.html',{'player':player})

        if player.current==8:
            if request.POST['choice8']=='1' or request.POST['choice8']=='2':
                if request.POST["choice8"]=="1":
                    player.choice8=True
                    player.save()
                player.current+=1
                player.save()
                return render(request, 'core/choice9.html',{'player':player})

        if player.current==9:
            if request.POST['choice9']=='1' or request.POST['choice9']=='2':
                if request.POST["choice9"]=="1":
                    player.choice9=True
                    player.save()
                player.current+=1
                player.save()
                return render(request, 'core/choice10.html',{'player':player})

        if player.current==10:
            if request.POST['choice10']=='1' or request.POST['choice10']=='2':
                if request.POST["choice10"]=="1":
                    player.choice10=True
                    player.save()
                player.current+=1
                player.save()
                return redirect('complete')
    
    else:
        a = Master.objects.order_by('-id')[0].id
        player = get_object_or_404(Master, id=a)
        ctx['player'] = player
        return render(request, 'core/choice1.html', ctx)

def result2(request,pk):
    ctx = {}
    player=get_object_or_404(Player,pk=pk)
    master= Master.objects.order_by('-id')[0]
    if request.method=="POST":
        if player.current==1:
            if request.POST['choice1']=='1' or request.POST['choice1']=='2':
                if request.POST["choice1"]=="1":
                    player.choice1=True
                    player.save()
                player.current+=1
                player.save()
                return render(request, 'core/choice2.html',{'player':player,'master':master})

        if player.current==2:
            if request.POST['choice2']=='1' or request.POST['choice2']=='2':
                if request.POST["choice2"]=="1":
                    player.choice2=True
                    player.save()
                player.current+=1
                player.save()
                return render(request, 'core/choice3.html',{'player':player,'master':master})

        if player.current==3:
            if request.POST['choice3']=='1' or request.POST['choice3']=='2':
                if request.POST["choice3"]=="1":
                    player.choice3=True
                    player.save()
                player.current+=1
                player.save()
                return render(request, 'core/choice4.html',{'player':player,'master':master})

        if player.current==4:
            if request.POST['choice4']=='1' or request.POST['choice4']=='2':
                if request.POST["choice4"]=="1":
                    player.choice4=True
                    player.save()
                player.current+=1
                player.save()
                return render(request, 'core/choice5.html',{'player':player,'master':master})
        
        if player.current==5:
            if request.POST['choice5']=='1' or request.POST['choice5']=='2':
                if request.POST["choice5"]=="1":
                    player.choice5=True
                    player.save()
                player.current+=1
                player.save()
                return render(request, 'core/choice6.html',{'player':player,'master':master})

        if player.current==6:
            if request.POST['choice6']=='1' or request.POST['choice6']=='2':
                if request.POST["choice6"]=="1":
                    player.choice6=True
                    player.save()
                player.current+=1
                player.save()
                return render(request, 'core/choice7.html',{'player':player,'master':master})

        if player.current==7:
            if request.POST['choice7']=='1' or request.POST['choice7']=='2':
                if request.POST["choice7"]=="1":
                    player.choice7=True
                    player.save()
                player.current+=1
                player.save()
                return render(request, 'core/choice8.html',{'player':player,'master':master})

        if player.current==8:
            if request.POST['choice8']=='1' or request.POST['choice8']=='2':
                if request.POST["choice8"]=="1":
                    player.choice8=True
                    player.save()
                player.current+=1
                player.save()
                return render(request, 'core/choice9.html',{'player':player,'master':master})

        if player.current==9:
            if request.POST['choice9']=='1' or request.POST['choice9']=='2':
                if request.POST["choice9"]=="1":
                    player.choice9=True
                    player.save()
                player.current+=1
                player.save()
                return render(request, 'core/choice10.html',{'player':player,'master':master})

        if player.current==10:
            if request.POST['choice10']=='1' or request.POST['choice10']=='2':
                if request.POST["choice10"]=="1":
                    player.choice10=True
                    player.save()
                player.current+=1
                player.save()
                pk = Player.objects.order_by('-id')[0].id
                return redirect(reverse('result_', kwargs={'pk':pk}))
    
    else:
        a = Player.objects.order_by('-id')[0].id
        master= Master.objects.order_by('-id')[0]
        player = get_object_or_404(Player, id=a)
        ctx['player'] = player
        ctx['master'] = master
        return render(request, 'core/choice1.html', ctx)

def master_home(request):
    if request.method == "POST":
        name = request.POST['name']
        Master.objects.create(name=name)
        pk = Master.objects.order_by('-id')[0].id
        print(pk)
        return redirect(reverse('result', kwargs={'pk':pk}))
    else:
        return render(request, "core/master_home.html", )


def player_home(request, pk):
    if request.method == "POST":
        name = request.POST['name']
        Player.objects.create(name=name)
        pk = Player.objects.order_by('-id')[0].id
        return redirect(reverse('result2', kwargs={'pk':pk}))
    else:
        friends = Master.objects.get(pk=pk).friends
        player_count = len(Player.objects.all())
        name = Master.objects.order_by('-id')[0].name
        return render(request, "core/player_home.html", {"player_count": player_count, "friends": friends, "name":name})


def complete(request):
    pk = Master.objects.order_by('-id')
    return render(request, "core/complete.html", {"pk": pk[0].id})


def result_(request, pk):
    master = Master.objects.order_by('-id')[0]
    players = Player.objects.all()
    count_list = []
    for i in range(len(players)):
        count = 0
        if master.choice1 == players[i].choice1:
            count += 1
        if master.choice2 == players[i].choice2:
            count += 1
        if master.choice3 == players[i].choice3:
            count += 1
        if master.choice4 == players[i].choice4:
            count += 1
        if master.choice5 == players[i].choice5:
            count += 1
        if master.choice6 == players[i].choice6:
            count += 1
        if master.choice7 == players[i].choice7:
            count += 1
        if master.choice8 == players[i].choice8:
            count += 1
        if master.choice9 == players[i].choice9:
            count += 1
        if master.choice10 == players[i].choice10:
            count += 1
        name = players[i].name
        a = (name, count)
        count_list.append(a)
    b, player = count_list[-1]
    ctx = {'count_list': count_list, 'players': players, 'player': player}
    master = Master.objects.order_by('-id')[0]
    master.friends +=1
    master.save()
    return render(request, "core/result.html", ctx)
