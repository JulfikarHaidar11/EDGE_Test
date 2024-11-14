from django.urls import path

from books.views import MyView

urlpatterns = [
    path('initial_class/', MyView.as_view()),

]