# Generated by Django 2.0 on 2018-03-04 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ac_no', models.CharField(max_length=200)),
                ('bank_name', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Salary_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthly_salary', models.DecimalField(decimal_places=2, max_digits=15)),
                ('total_salary', models.DecimalField(decimal_places=2, max_digits=15)),
                ('paid', models.DecimalField(decimal_places=2, max_digits=15)),
                ('unpaid', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.RenameModel(
            old_name='Stuff',
            new_name='Staff',
        ),
        migrations.AddField(
            model_name='salary_info',
            name='staff',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Staff'),
        ),
        migrations.AddField(
            model_name='bank_statement',
            name='account_holder',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Salary_info'),
        ),
    ]