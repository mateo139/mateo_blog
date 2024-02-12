from django.shortcuts import render

def post_list(request): #stworzenie funkcji post_list, która przyjmuje request i zwraca funkcję render, która zwraca szablon blog/post_list.html
    return render (request, 'blog/post_list.html',{})
