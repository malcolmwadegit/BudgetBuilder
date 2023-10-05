

class budget:
    def __init__(self, income):
        self.income = int(income)
    # listen for an Add Category Click then add category to budget
        # def __init__(self, NewCategory[]):
        #      self.categories = [NewCategory]
    
    categories = []
    
    
    
    
class Spending:
    items = []


class NewCategory:
    def __init__(self, name, category_budget):
        self.name = int(name)
        self.category_budget = int(category_budget)
        
        budget.categories.append = (name , category_budget)
        
class NewLineItem:
    def __init__(self, description, cost, category):
        self.description = str(description)
        self.cost = int(cost)
        self.category = str(category)
        
        Spending.items.append = (description, cost, category)
        
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
    
    
    

    
    
    
     
    
    
    