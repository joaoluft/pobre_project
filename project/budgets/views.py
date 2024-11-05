from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Budget, IncomeSource, Expense, Tracking
from .forms import BudgetForm, IncomeSourceForm, ExpenseForm, TrackingForm

class BudgetListView(View):
    def get(self, request):
        budgets = Budget.objects.all()
        return render(request, 'budget/budget_list.html', {'budgets': budgets})

class BudgetCreateView(View):
    def get(self, request):
        form = BudgetForm()
        return render(request, 'budget/budget_form.html', {'form': form})

    def post(self, request):
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('budget_list')
        return render(request, 'budget/budget_form.html', {'form': form})

class BudgetUpdateView(View):
    def get(self, request, pk):
        budget = get_object_or_404(Budget, pk=pk)
        form = BudgetForm(instance=budget)
        return render(request, 'budget/budget_form.html', {'form': form})

    def post(self, request, pk):
        budget = get_object_or_404(Budget, pk=pk)
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            return redirect('budget_list')
        return render(request, 'budget/budget_form.html', {'form': form})

class BudgetDeleteView(View):
    def get(self, request, pk):
        budget = get_object_or_404(Budget, pk=pk)
        return render(request, 'budget/budget_confirm_delete.html', {'budget': budget})

    def post(self, request, pk):
        budget = get_object_or_404(Budget, pk=pk)
        budget.delete()
        return redirect('budget_list')

class IncomeSourceListView(View):
    def get(self, request, budget_id):
        income_sources = IncomeSource.objects.filter(budget_id=budget_id)
        return render(request, 'budget/income_source_list.html', {'income_sources': income_sources, 'budget_id': budget_id})

class IncomeSourceCreateView(View):
    def get(self, request, budget_id):
        form = IncomeSourceForm()
        return render(request, 'budget/income_source_form.html', {'form': form, 'budget_id': budget_id})

    def post(self, request, budget_id):
        form = IncomeSourceForm(request.POST)
        if form.is_valid():
            income_source = form.save(commit=False)
            income_source.budget_id = budget_id
            income_source.save()
            return redirect('income_source_list', budget_id=budget_id)
        return render(request, 'budget/income_source_form.html', {'form': form, 'budget_id': budget_id})

class IncomeSourceUpdateView(View):
    def get(self, request, pk):
        income_source = get_object_or_404(IncomeSource, pk=pk)
        form = IncomeSourceForm(instance=income_source)
        return render(request, 'budget/income_source_form.html', {'form': form, 'budget_id': income_source.budget_id})

    def post(self, request, pk):
        income_source = get_object_or_404(IncomeSource, pk=pk)
        form = IncomeSourceForm(request.POST, instance=income_source)
        if form.is_valid():
            form.save()
            return redirect('income_source_list', budget_id=income_source.budget_id)
        return render(request, 'budget/income_source_form.html', {'form': form, 'budget_id': income_source.budget_id})


class IncomeSourceDeleteView(View):
    def get(self, request, pk):
        income_source = get_object_or_404(IncomeSource, pk=pk)
        budget_id = income_source.budget_id
        return render(request, 'budget/income_source_confirm_delete.html', {'income_source': income_source, 'budget_id': budget_id})

    def post(self, request, pk):
        income_source = get_object_or_404(IncomeSource, pk=pk)
        budget_id = income_source.budget_id
        income_source.delete()
        return redirect('income_source_list', budget_id=budget_id)

class ExpenseListView(View):
    def get(self, request, budget_id):
        expenses = Expense.objects.filter(budget_id=budget_id)
        return render(request, 'budget/expense_list.html', {'expenses': expenses, 'budget_id': budget_id})

class ExpenseCreateView(View):
    def get(self, request, budget_id):
        form = ExpenseForm()
        return render(request, 'budget/expense_form.html', {'form': form, 'budget_id': budget_id})

    def post(self, request, budget_id):
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.budget_id = budget_id
            expense.save()
            return redirect('expense_list', budget_id=budget_id)
        return render(request, 'budget/expense_form.html', {'form': form, 'budget_id': budget_id})

class ExpenseUpdateView(View):
    def get(self, request, pk):
        expense = get_object_or_404(Expense, pk=pk)
        form = ExpenseForm(instance=expense)
        budget_id = expense.budget_id
        return render(request, 'budget/expense_form.html', {'form': form, 'budget_id': budget_id})

    def post(self, request, pk):
        expense = get_object_or_404(Expense, pk=pk)
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list', budget_id=expense.budget_id)
        budget_id = expense.budget_id
        return render(request, 'budget/expense_form.html', {'form': form, 'budget_id': budget_id})

class ExpenseDeleteView(View):
    def get(self, request, pk):
        expense = get_object_or_404(Expense, pk=pk)
        budget_id = expense.budget_id 
        return render(request, 'budget/expense_confirm_delete.html', {'expense': expense, 'budget_id': budget_id})

    def post(self, request, pk):
        expense = get_object_or_404(Expense, pk=pk)
        budget_id = expense.budget_id 
        expense.delete()
        return redirect('expense_list', budget_id=budget_id)


class TrackingListView(View):
    def get(self, request, budget_id):
        trackings = Tracking.objects.filter(budget_id=budget_id)
        return render(request, 'budget/tracking_list.html', {'trackings': trackings, 'budget_id': budget_id})

class TrackingCreateView(View):
    def get(self, request, budget_id):
        form = TrackingForm()
        return render(request, 'budget/tracking_form.html', {'form': form, 'budget_id': budget_id})

    def post(self, request, budget_id):
        form = TrackingForm(request.POST)
        if form.is_valid():
            tracking = form.save(commit=False)
            tracking.budget_id = budget_id
            tracking.save()
            return redirect('tracking_list', budget_id=budget_id)
        return render(request, 'budget/tracking_form.html', {'form': form, 'budget_id': budget_id})
    
class TrackingUpdateView(View):
    def get(self, request, pk):
        tracking = get_object_or_404(Tracking, pk=pk)
        form = TrackingForm(instance=tracking)
        return render(request, 'budget/tracking_form.html', {'form': form, 'budget_id': tracking.budget_id})

    def post(self, request, pk):
        tracking = get_object_or_404(Tracking, pk=pk)
        form = TrackingForm(request.POST, instance=tracking)
        if form.is_valid():
            form.save()
            return redirect('tracking_list', budget_id=tracking.budget_id)
        return render(request, 'budget/tracking_form.html', {'form': form, 'budget_id': tracking.budget_id})

class TrackingDeleteView(View):
    def get(self, request, pk):
        tracking = get_object_or_404(Tracking, pk=pk)
        budget_id = tracking.budget_id 
        return render(request, 'budget/tracking_confirm_delete.html', {'tracking': tracking, 'budget_id': budget_id})

    def post(self, request, pk):
        tracking = get_object_or_404(Tracking, pk=pk)
        budget_id = tracking.budget_id
        tracking.delete()
        return redirect('tracking_list', budget_id=budget_id)
