from django.urls import path
from .views import (ExpenseCreateView, ExpenseListView, ExpenseUpdateView, ExpenseDeleteView)
from . import views
from .restViews import (DashboardApiView)

urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('api', DashboardApiView.as_view(), name="dashboardApi"),
    path('', views.resume, name="resume"),
    path('home', ExpenseListView.as_view(), name="home"),
    path('resume', views.resume, name='resume'),
    path('create', ExpenseCreateView.as_view(), name="create"),
    path('deleteall', views.deleteAll, name="delete"),
    path('savings', views.savings, name="savings"),
    path('rajju', views.birthday, name="rajju"),
    path('<int:pk>/update', ExpenseUpdateView.as_view(), name="update"),
    path('<int:pk>/delete', ExpenseDeleteView.as_view(), name="delete"),
]
