from django.db import models

class Budget(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")
    goal = models.TextField(verbose_name="Objetivo")
    start_date = models.DateField(verbose_name="Data de Início")
    end_date = models.DateField(verbose_name="Data de Término")
    emergency_fund = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Fundo de Emergência")
    total_income = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Renda Total")
    total_expense = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Despesa Total")

    def __str__(self):
        return self.name

class IncomeSource(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Diário'),
        ('weekly', 'Semanal'),
        ('monthly', 'Mensal'),
        ('semiannual', 'Semestral'),
        ('annual', 'Anual'),
    ]

    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="income_sources", verbose_name="Orçamento")
    description = models.CharField(max_length=255, verbose_name="Descrição")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Quantidade")
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, verbose_name="Frequência")

    def __str__(self):
        return f"{self.description} - {self.amount}"

class Expense(models.Model):
    EXPENSE_TYPE = [
        ('fixed', 'Fixo'),
        ('variable', 'Variável'),
    ]

    FREQUENCY_CHOICES = [
        ('daily', 'Diário'),
        ('weekly', 'Semanal'),
        ('monthly', 'Mensal'),
        ('semiannual', 'Semestral'),
        ('annual', 'Anual'),
    ]

    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="expenses", verbose_name="Orçamento")
    description = models.CharField(max_length=255, verbose_name="Descrição")
    type = models.CharField(max_length=10, choices=EXPENSE_TYPE, verbose_name="Tipo")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Quantidade")
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, verbose_name="Frequência")
    # Juntar com categorias feitas por outro grupo depois

    def get_frequency_display(self):
        return dict(self.FREQUENCY_CHOICES).get(self.frequency, self.frequency)

    def __str__(self):
        return f"{self.description} - {self.amount}"

class Tracking(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="trackings", verbose_name="Orçamento")
    date = models.DateField(verbose_name="Data")
    actual_income = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Renda Real")
    actual_expense = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Despesa Real")
    notes = models.TextField(verbose_name="Notas")

    def __str__(self):
        return f"Tracking - {self.date}"