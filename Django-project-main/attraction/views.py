from django.shortcuts import render
from .models import book


def get_books(request):
    context = {'books': book.objects.all()}
    return render(request, 'attraction/get_books.html' , context)

def add_book(request):
    if request.method == "GET":
        return render(request, 'attraction/form.html')
    if request.method == "POST":
        data = request.POST
        book.objects.create(onvan=data['onvan'], nevisande=data['nevisande'], tedade_safahat=data['tedade_safahat'], tozih=data['tozih'] , image=data['image'])
        return render(request, 'attraction/finished.html')
       

