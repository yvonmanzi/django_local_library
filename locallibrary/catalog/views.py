from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # genres_with_word_count = Genre.objects.filter(name__contains='love').count()
    # books_with_word_count = Book.objects.filter(title__contains='future').count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1


    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    # Context variable. interesting. 
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    # You can customize this listview thing. For example::
    # context_object_name = 'book_list'   # your own name for the list as a template variable
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location
    # def get_queryset(self) -> QuerySet[Any]:
    #     return Book.objects.filter(title__icontains='war')[:5]
    # you can also return more data than just the default list of books: like the following:
  
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context

class BookDetailView(generic.DetailView):
    model = Book
    # this view can be implemented like this:
    # def book_detail_view(request, primary_key):
    # try:
    #     book = Book.objects.get(pk=primary_key)
    # except Book.DoesNotExist:
    #     raise Http404('Book does not exist')

    # return render(request, 'catalog/book_detail.html', context={'book': book})

    # or this way:
    # from django.shortcuts import get_object_or_404

    # def book_detail_view(request, primary_key):
    #     book = get_object_or_404(Book, pk=primary_key)
    #     return render(request, 'catalog/book_detail.html', context={'book': book})


