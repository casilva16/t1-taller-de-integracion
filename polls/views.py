from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul')
    databcs = response.json()

    response2 = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad')
    databb = response2.json()

    s1bb, s2bb, s3bb, s4bb, s5bb,  = make_seasons(databb, True)
    s1bcs, s2bcs, s3bcs, s4bcs, s6bcs = make_seasons(databcs, False)

    ctx = {'s1': s1bcs, 's2': s2bcs, 's3': s3bcs, 's4': s4bcs, 's6': s6bcs,
    's1bb': s1bb, 's2bb': s2bb, 's3bb': s3bb, 's4bb': s4bb, 's5bb': s5bb
    }
    return render(request, 'index.html', ctx)
    

def episode_bcs(request, episode_id):
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes/'+episode_id)
    data = response.json()
    episode = data[0]
    
    response2 = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters/')
    personas = response2.json()
    ctx = {'episode': episode, 'personas': personas}
    return render(request, 'episode_bcs.html', ctx)


def character(request, char_id):
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters/'+char_id)
    data = response.json()
    personaje = data[0]

    return render(request, 'character.html', {'personaje': personaje})


def make_seasons(data, valor):
    if valor: # es bb
        seasons = [[] for i in range(5)]
        for i in data:
            temp = int(i['season']) - 1
            seasons[temp].append(i)
        return seasons[0], seasons[1], seasons[2], seasons[3], seasons[4]


    else:# es bcs
        seasons = [[] for i in range(5)]
        for i in data:
            if i['season'] == '6':
                seasons[4].append(i)
            else:
                temp = int(i['season']) - 1
                seasons[temp].append(i)
        return seasons[0], seasons[1], seasons[2], seasons[3], seasons[4]

        

    