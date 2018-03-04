from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Staff(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    choice = (("Front-end", "Front-end"), ("Back-end", "Back-end"), ("Android developer", "Android developer"))
    rank = models.CharField(max_length=100, choices=choice)
    joined = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name.username


class Salary_info(models.Model):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    monthly_salary = models.DecimalField(max_digits=15, decimal_places=2)
    total_salary = models.DecimalField(max_digits=15, decimal_places=2)
    paid = models.DecimalField(max_digits=15, decimal_places=2)
    unpaid = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.staff.name.username


class Bank_statement(models.Model):
    account_holder = models.OneToOneField(Salary_info, on_delete=models.CASCADE)
    ac_no = models.CharField(max_length=200)
    bank_name = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)

    def __str__(self):
        return self.account_holder.staff.name.username
