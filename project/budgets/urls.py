from django.urls import path
from .views import (
    BudgetListView,
    BudgetCreateView,
    BudgetUpdateView,
    BudgetDeleteView,
    IncomeSourceListView,
    IncomeSourceCreateView,
    IncomeSourceUpdateView,
    IncomeSourceDeleteView,
    ExpenseListView,
    ExpenseCreateView,
    ExpenseUpdateView,
    ExpenseDeleteView,
    TrackingListView,
    TrackingCreateView,
    TrackingUpdateView,
    TrackingDeleteView,
)

urlpatterns = [
    path('', BudgetListView.as_view(), name='budget_list'),
    path('budget/create/', BudgetCreateView.as_view(), name='budget_create'),
    path('budget/<int:pk>/update/', BudgetUpdateView.as_view(), name='budget_update'),
    path('budget/<int:pk>/delete/', BudgetDeleteView.as_view(), name='budget_delete'),
    
    path('budget/<int:budget_id>/income_sources/', IncomeSourceListView.as_view(), name='income_source_list'),
    path('budget/<int:budget_id>/income_sources/create/', IncomeSourceCreateView.as_view(), name='income_source_create'),
    path('income_source/<int:pk>/update/', IncomeSourceUpdateView.as_view(), name='income_source_update'),
    path('income_source/<int:pk>/delete/', IncomeSourceDeleteView.as_view(), name='income_source_delete'),

    path('budget/<int:budget_id>/expenses/', ExpenseListView.as_view(), name='expense_list'),
    path('budget/<int:budget_id>/expenses/create/', ExpenseCreateView.as_view(), name='expense_create'),
    path('expense/<int:pk>/update/', ExpenseUpdateView.as_view(), name='expense_update'),
    path('expense/<int:pk>/delete/', ExpenseDeleteView.as_view(), name='expense_delete'),

    path('budget/<int:budget_id>/trackings/', TrackingListView.as_view(), name='tracking_list'),
    path('budget/<int:budget_id>/trackings/create/', TrackingCreateView.as_view(), name='tracking_create'),
    path('tracking/<int:pk>/update/', TrackingUpdateView.as_view(), name='tracking_update'),
    path('tracking/<int:pk>/delete/', TrackingDeleteView.as_view(), name='tracking_delete'),
]