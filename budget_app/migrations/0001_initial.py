# Generated by Django 2.1.5 on 2019-01-25 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1028)),
                ('total_budget', models.FloatField(blank=True)),
                ('remaining_budget', models.FloatField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='budgets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('withdrawal', 'Withdrawal'), ('deposit', 'Deposit')], max_length=16)),
                ('amount', models.FloatField(default=0)),
                ('description', models.CharField(default=' details...', max_length=2056)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to=settings.AUTH_USER_MODEL)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='budget_app.Budget')),
            ],
        ),
    ]