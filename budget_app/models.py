from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver


class Budget(models.Model):
    """ This is the class Budget
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1028)
    total_budget = models.FloatField(blank=True)
    remaining_budget = models.FloatField(blank=True)

    def __repr__(self):
        """ Repr returns the title and then the date added and last borrowed date
        """
        return f'{self.name}, {self.total_budget}, {self.remaining_budget}, {self.id},'

    def __str__(self):
        """ str gives back basic information about the class objects
        """
        return f'name:  {self.name},  Total budget{self.total_budget}, Remaining budget{self.remaining_budget}'


class Transaction(models.Model):
    """ This is the class Transaction
    """
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions', null=True, blank=True)
    # id = models.AutoField
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='transactions')

    TRANSACTIONS = (
        ('withdrawal', 'Withdrawal'), ('deposit', 'Deposit'),
    )
    transaction_type = models.CharField(max_length=16, choices=TRANSACTIONS)
    amount = models.FloatField(default=0)
    description = models.CharField(max_length=2056, default=' details...')

    def __repr__(self):
        """ Repr returns the title and then the date added and last borrowed date
        """
        return f'{self.budget}, {self.amount}, {self.description}, {self.id},'

    def __str__(self):
        """ str gives back basic information about the class objects
        """
        return f'budget: {self.budget},  Amount: {self.amount}, Description: {self.description}'


@receiver(models.signals.post_save, sender=Transaction)
def calc_budget_balance(sender, instance, **kwargs):
    """Update budget balance."""
    # To add/subtract the transaction amount:
    if instance.transaction_type == 'deposit':
        instance.budget.remaining_budget += instance.amount
    else:
        instance.budget.remaining_budget -= instance.amount

    # To Save:
    instance.budget.save()
