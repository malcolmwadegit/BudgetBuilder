from django.db import models

# Create your models here.

class budget(models.Model):
    income = models.IntegerField(default = 0, null=False)
    # listen for an Add Category Click then add category to budget
        # def __init__(self, NewCategory[]):
        #      self.categories = [NewCategory]
    
    # categories = models.ForeignKey(to=NewCategory, )
    
    
    
class Spending:
    items = []


class NewCategory(models.Model):
    name = models.CharField(null=False, default='None', max_length=255)
    category_budget = models.IntegerField(default=0, null=True)
        
    budget.categories = (name, category_budget)
        
class NewLineItem(models.Model):
    description = models.CharField(default='', null=True, max_length=255)
    cost = models.IntegerField(default = 0)
    category = models.CharField(default='', null=True, max_length=255)
        
    Spending.items.append((description, cost, category))
        