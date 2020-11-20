from django.shortcuts import render, redirect, get_object_or_404
from .models import Player, Master
from .forms import MasterForm


# Create your views here.
def master_home(request):
    if request.method == "POST":
        name = request.POST['name']
        Master.objects.create(name=name)
        return render(request, "core/master_home.html")
    else:
        return render(request, "core/master_home.html", )


def player_home(request, pk):
    friends = Master.objects.get(pk=pk).friends
    player_count = len(Player.objects.all())
    name = Master.objects.order_by('-id')[0].name
    return render(request, "core/player_home.html", {"player_count": player_count, "friends": friends, "name":name})


def complete(request):
    pk = Master.objects.order_by('-id')
    return render(request, "core/complete.html", {"pk": pk[0].id})


def result(request, pk):
    master = Master.objects.get(id=pk)
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
    master = Master.objects.get(pk=pk)
    master.friends +=1
    master.save()
    return render(request, "core/result.html", ctx)
