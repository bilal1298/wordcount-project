from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def count(request):
    inputtext = request.GET['inputtext']
    wordlist = inputtext.split()

    dictionary = {}

    for single in wordlist:
        if single in dictionary:
            dictionary[single] += 1
        else:
            dictionary[single] = 1

    dictionarylist = sorted(
        dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'input': inputtext, 'count': len(wordlist), 'dictionary': dictionarylist})


def about(request):
    return render(request, 'about.html')
