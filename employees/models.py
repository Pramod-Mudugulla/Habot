from django.db import models

class Employee(models.Model):
    DEPARTMENT_CHOICES = (
        ("HR", "HR"),
        ("Engineering", "Engineering"),
        ("Sales", "Sales"),
        ("Marketing", "Marketing"),
        ("Finance", "Finance"),
        ("IT", "IT"),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(
        max_length=50,
        choices=DEPARTMENT_CHOICES,
        blank=True,
        null=True,
    )
    role = models.CharField(max_length=50, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"