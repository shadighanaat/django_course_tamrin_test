from django.urls import path
from . import views

urlpatterns = [
    path('', views.MembersListView.as_view(), name='members_list'),
    path('<int:pk>', views.MembersDetailView.as_view(), name='members_detail'),
    path('create/', views.MembersCreateView.as_view(), name='create'),
    path('<int:pk>/update', views.MembersUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.MembersDeleteView.as_view(), name='delete'),
]
