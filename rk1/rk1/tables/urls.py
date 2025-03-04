from django.urls import path
from .views import TableListCreateView, AvailableTablesView

urlpatterns = [
    path('', TableListCreateView.as_view(), name='table-list'),
    path('available/', AvailableTablesView.as_view(), name='available-tables'),
]
