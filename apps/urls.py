from django.urls import path

from .user_auth import views
from .incidents import views as incident_views


urlpatterns = [
    path('auth/signup/', views.UserSignupView.as_view(), name='user-signup'),
    path('auth/login/', views.UserLoginView.as_view(), name='user-login'),
    path('incidents/', incident_views.IncidentListCreateView.as_view(), name='incident-list-create'),
    path('incidents/<str:incident_id>/', incident_views.IncidentDetailView.as_view(), name='incident-detail'),
    path('incidents/search/', incident_views.IncidentSearchView.as_view(), name='incident-search'),
]
