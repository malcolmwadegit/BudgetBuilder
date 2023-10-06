from django.shortcuts import render
from .models import NewCategory, NewLineItem, budget

# Create your views here.
def CreateCategory(): 
    # listen for new category button click
    # -> ask for inputs 
    # -> listen for submit button click
    # -> submit inputs for category name and budget 
    # -> add category to budget
    category_name = str(input())
    category_budget = int(input())
    category = NewCategory
    if budget.categories[category_name] == True:
        return print("Category already exists")
    else:
        category.__init__(category_name, category_budget)
    
    
def CreateLineItem(): 
    # listen for new line item click
    # -> ask for input 
    # -> listen for submit button click
    # -> add line item to spending
    item_decription = str(input())
    item_cost = int(input())
    item_category = str(input())
    new_item = NewLineItem
    new_item.__init__(item_decription,item_cost, item_category)
    

def home(request):
    return render(request, 'BudgetApp/budget_view.html')

def new_budget(request):
    return render(request, 'BudgetApp/new_budget.html')

def new_category(request):
    return render(request, 'BudgetApp/new_category.html')
def new_line_item(request):
    return render(request, 'BudgetApp/new_line_item.html')