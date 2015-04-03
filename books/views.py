from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import *

class PublisherList(generic.ListView):
    model = Publisher

class PublisherDetail(generic.DetailView):
    model = Publisher
    context_object_name = 'publisher'

class PublisherBookList(generic.ListView):
    template_name = 'books/books_by_pub.html'
    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.args[0])
        return Book.objects.filter(publisher=self.publisher)
    def get_context_data(self, **kwargs):
        context = super(PublisherBookList,self).get_context_data(**kwargs)
        context['publisher'] = self.publisher
        return context

class BookList(generic.ListView):
    model = Book
    context_object_name = 'book_list'