# accounts/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]
from django.urls import path

from . import views




urlpatterns += [   
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'), #Added for challenge
]


# Add URLConf for librarian to renew a book.
urlpatterns += [    
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]


# Add URLConf to create, update, and delete authors
