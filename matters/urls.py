from django.urls import path
from .views import (
    home_page, DashboardView, MyMatterListView, TeamMatterListView, 
    DisputeCreateView, DisputeDetailView, DisputeUpdateView, DisputeDeleteView, 
    AdviceCreateView, AdviceDetailView, AdviceUpdateView, AdviceDeleteView,
    DealCreateView, DealDetailView, DealUpdateView, DealDeleteView,
    load_courts, my_matters_pie,
)

app_name = "matters"

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    # path('matters', MatterListView.as_view(), name='matter-list'),
    path('my-matters', MyMatterListView.as_view(), name='my-matters'),
    path('team-matters', TeamMatterListView.as_view(), name='team-matters'),
    
    # path('create', MatterCreateView.as_view(), name='matter-create'),
    # path('<int:pk>/', MatterDetailView.as_view(), name='matter-detail'),
    # path('<int:pk>/matter-update/', MatterUpdateView.as_view(), name='matter-update'),
    # path('<int:pk>/matter-delete/', MatterDeleteView.as_view(), name='matter-delete'),
    
    path('dispute_create', DisputeCreateView.as_view(), name='dispute-create'),
    path('<int:pk>/dispute-detail/', DisputeDetailView.as_view(), name='dispute-detail'),
    path('<int:pk>/dispute-update/', DisputeUpdateView.as_view(), name='dispute-update'),
    path('<int:pk>/dispute-delete/', DisputeDeleteView.as_view(), name='dispute-delete'),

    path('advice_create', AdviceCreateView.as_view(), name='advice-create'),
    path('<int:pk>/advice-detail/', AdviceDetailView.as_view(), name='advice-detail'),
    path('<int:pk>/advice-update/', AdviceUpdateView.as_view(), name='advice-update'),
    path('<int:pk>/advice-delete/', AdviceDeleteView.as_view(), name='advice-delete'),

    path('deal_create', DealCreateView.as_view(), name='deal-create'),
    path('<int:pk>/deal-detail/', DealDetailView.as_view(), name='deal-detail'),
    path('<int:pk>/deal-update/', DealUpdateView.as_view(), name='deal-update'),
    path('<int:pk>/deal-delete/', DealDeleteView.as_view(), name='deal-delete'),

    path('ajax/load-courts/', load_courts, name='ajax_load_courts'),
    path('my-matters-pie/', my_matters_pie, name='my-matters-pie'),
]