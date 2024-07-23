from django.urls import path
from .views import BookListView, AddReviewView, UpdateReviewView, DeleteReviewView, SuggestBooksView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('book/list/', BookListView.as_view(), name='book-list'),
    path('book/', BookListView.as_view(), name='book-list-genre'),
    path('review/add/', AddReviewView.as_view(), name='add-review'),
    path('review/update/<int:pk>/', UpdateReviewView.as_view(), name='update-review'),
    path('review/delete/<int:pk>/', DeleteReviewView.as_view(), name='delete-review'),
    path('suggest/', SuggestBooksView.as_view(), name='suggest-books'),
]