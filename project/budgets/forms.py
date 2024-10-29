from django import forms
from .models import Budget, IncomeSource, Expense, Cost, Tracking

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = '__all__'

class IncomeSourceForm(forms.ModelForm):
    class Meta:
        model = IncomeSource
        fields = '__all__'

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'

class CostForm(forms.ModelForm):
    class Meta:
        model = Cost
        fields = '__all__'

class TrackingForm(forms.ModelForm):
    class Meta:
        model = Tracking
        fields = '__all__'