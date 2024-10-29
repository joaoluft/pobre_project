from django.db import models

class Budget(models.Model):
    name = models.CharField(max_length=255)
    goal = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    emergency_fund = models.DecimalField(max_digits=10, decimal_places=2)
    total_income = models.DecimalField(max_digits=10, decimal_places=2)
    total_expense = models.DecimalField(max_digits=10, decimal_places=2)
    financial_goal = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class IncomeSource(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="income_sources")
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.description} - {self.amount}"

class Expense(models.Model):
    EXPENSE_TYPE = [
        ('fixed', 'Fixed'),
        ('variable', 'Variable'),
    ]

    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="expenses")
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=EXPENSE_TYPE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.description} - {self.amount}"

class Cost(models.Model):
    COST_TYPE = [
        ('direct', 'Direct'),
        ('indirect', 'Indirect'),
    ]

    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="costs")
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=COST_TYPE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.description} - {self.amount}"

class Tracking(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="trackings")
    date = models.DateField()
    actual_income = models.DecimalField(max_digits=10, decimal_places=2)
    actual_expense = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField()

    def __str__(self):
        return f"Tracking - {self.date}"
