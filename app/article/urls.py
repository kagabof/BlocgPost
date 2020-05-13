
from django.urls import path

from .views import ArticleView


app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', ArticleView.as_view()),
    path('<int:pk>', ArticleView.as_view())
]
