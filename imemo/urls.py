from django.urls import path
from .views import entry_memo

app_name = 'imemo'

urlpatterns = [
    path('entry_memo', entry_memo, name='memo')
]