from django.db import models

class PersonType(models.Model):
    TYPE_CHOICES = [
        ('CPF', 'Pessoa Física'),
        ('CNPJ', 'Pessoa Jurídica'),
    ]
    type = models.CharField(max_length=45, choices=TYPE_CHOICES, verbose_name="Type", unique=True)

    def __str__(self):
        return self.get_type_display()

class Person(models.Model):
    name = models.CharField(max_length=30, verbose_name="Name")
    email = models.EmailField(max_length=30, unique=True, verbose_name="Email")
    age = models.PositiveIntegerField(verbose_name="Age")
    person_type = models.ForeignKey('PersonType', on_delete=models.PROTECT, verbose_name="Person Type")
    document_number = models.CharField(max_length=14, blank=True, null=True, verbose_name="Document Number")

    class Meta:
        verbose_name = "person"
        verbose_name_plural = "people"
        ordering = ['name']

    def __str__(self):
        return self.name