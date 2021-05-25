from django.shortcuts import render
import requests

# Create your views here.
#url = "https://hummingbirdv1.p.rapidapi.com/anime/steins-gate"

# headers = {
#    'x-rapidapi-key': "e5cca01e94msh13b50c3f5cb7543p139c26jsn9bd955386cb9",
#    'x-rapidapi-host': "hummingbirdv1.p.rapidapi.com"
# }


def index(request):

    return render(request, 'anime/index.html')


def home(request):
    '''
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    '''
    url = "https://simpleanime.p.rapidapi.com/anime/get/download/MTQ4Nzcz"

    headers = {
        'x-rapidapi-key': "e5cca01e94msh13b50c3f5cb7543p139c26jsn9bd955386cb9",
        'x-rapidapi-host': "simpleanime.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)
    geodata = response.json()

    titles = []
    t = []
    for r in geodata['data']:
        titles.append(r)
        for title in titles:
            t.append(title)
            print(title)
    # print(geodata)
    return render(request, 'anime/home.html', {
        'ip': t,
        # 'country': geodata
    })


def latest(request):

    url = "https://simpleanime.p.rapidapi.com/anime/list/recent"

    headers = {
        'x-rapidapi-key': "e5cca01e94msh13b50c3f5cb7543p139c26jsn9bd955386cb9",
        'x-rapidapi-host': "simpleanime.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    geodata = response.json()
    # print(response.title)
    titles = []
    t = []
    for r in geodata['data']:
        titles.append(r)
        for title in titles:
            t.append(title)
            print(title)
    return render(request, 'anime/latest.html', {
        'datas': t
    })


def details(request, vid_id):
    url = "https://simpleanime.p.rapidapi.com/anime/info/videos/" + vid_id

    headers = {
        'x-rapidapi-key': "e5cca01e94msh13b50c3f5cb7543p139c26jsn9bd955386cb9",
        'x-rapidapi-host': "simpleanime.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    geodata = response.json()
    # print(response.title)
    titles = []
    t = []
    covers = []
    for r in geodata['data']:
        titles.append(r)
        for title in titles:
            t.append(title)
            # print(title)
    for cover in geodata['episode']:
        covers.append(cover)
        # print(covers)
    return render(request, 'anime/detail.html', {
        'data': title,
        'epi': covers[0]
    })
