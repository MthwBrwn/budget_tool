from django.contrib.auth.models import User
from django.db import models


class Budget(models.Model):
    """ This is the class Budget
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    id = models.AutoField
    name = models.CharField(max_length=1028)
    total_budget = models.FloatField
    remaining_budget = models.FloatField

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
    id = models.AutoField
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='transactions')

    TRANSACTIONS = (
        ('withdrawal', 'Withdrawal'), ('deposit', 'Deposit'),
    )

    amount = models.FloatField(default='deposit', choices=TRANSACTIONS)
    description = models.CharField(max_length=2056)

    def __repr__(self):
        """ Repr returns the title and then the date added and last borrowed date
        """
        return f'{self.budget}, {self.amount}, {self.description}, {self.id},'

    def __str__(self):
        """ str gives back basic information about the class objects
        """
        return f'budget: {self.budget},  Amount: {self.amount}, Description: {self.description}'
