from django.shortcuts import render, redirect, get_object_or_404
from .models import Budget, IncomeSource, Expense, Cost, Tracking
from .forms import BudgetForm, IncomeSourceForm, ExpenseForm, CostForm, TrackingForm

def budget_list(request):
    budgets = Budget.objects.all()
    return render(request, 'budget/budget_list.html', {'budgets': budgets})

def budget_create(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('budget_list')
    else:
        form = BudgetForm()
    return render(request, 'budget/budget_form.html', {'form': form})

def budget_update(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            return redirect('budget_list')
    else:
        form = BudgetForm(instance=budget)
    return render(request, 'budget/budget_form.html', {'form': form})

def budget_delete(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    if request.method == 'POST':
        budget.delete()
        return redirect('budget_list')
    return render(request, 'budget/budget_confirm_delete.html', {'budget': budget})