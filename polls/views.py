from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul')
    databcs = response.json()

    response2 = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad')
    databb = response2.json()

    s1bb, s2bb, s3bb, s4bb, s5bb  = make_seasons(databb, True)
    s1bcs, s2bcs, s3bcs, s4bcs, s6bcs = make_seasons(databcs, False)
    rango = [1, 2, 3, 4, 5]
    rango2 = [1, 2, 3, 4, 6]
    #ctx = {'s1': s1bcs, 's2': s2bcs, 's3': s3bcs, 's4': s4bcs, 's6': s6bcs,
    #'s1bb': s1bb, 's2bb': s2bb, 's3bb': s3bb, 's4bb': s4bb, 's5bb': s5bb, 'range': range(5)
    #}
    ctx2 = {'range': rango, 'range2': rango2}
    return render(request, 'index.html', ctx2)
    

def episodesbb(request, i):
    response2 = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad')
    databb = response2.json()
    s1bb, s2bb, s3bb, s4bb, s5bb  = make_seasons(databb, True)

    if int(i) == 1:
        ctx = {'season': s1bb, 'n': 1}
    elif int(i) == 2:
        ctx = {'season': s2bb, 'n': 2}
    elif int(i)  == 3:
        ctx = {'season': s3bb, 'n': 3}   
    elif int(i)  == 4:
        ctx = {'season': s4bb, 'n': 4}
    elif int(i) == 5:
        ctx = {'season': s5bb, 'n': 5}

    return render(request, 'episodesbb.html', ctx)


def episodesbcs(request, j): 
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul')
    databcs = response.json()
    s1bcs, s2bcs, s3bcs, s4bcs, s6bcs = make_seasons(databcs, False)
    
    if int(j) == 1:
        ctx = {'seasonbcs': s1bcs, 'c': 1}
    elif int(j) == 2:
        ctx = {'seasonbcs': s2bcs, 'c': 2}
    elif int(j)  == 3:
        ctx = {'seasonbcs': s3bcs, 'c': 3}   
    elif int(j)  == 4:
        ctx = {'seasonbcs': s4bcs, 'c': 4}
    elif int(j) == 5:
        ctx = {'seasonbcs': s6bcs, 'c': 6}
    
    return render(request, 'episodesbcs.html', ctx)


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
    quotes = []
    response2 = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/quotes')
    data2 = response2.json()
    for quote in data2:
        if quote['author'] == personaje['name']:
           quotes.append(quote)

    ctx = {'personaje': personaje, 'quotes': quotes}
    return render(request, 'character.html', ctx)


def search_results(request, name): # recibe letra o nombre
    responde = response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters/')
    data = response.json()

    for personaje in data:
        if name in personaje.name:
            ctx = {'personaje': personaje}
            return render(request, 'search_results.html', ctx)


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

        

    