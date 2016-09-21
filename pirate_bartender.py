import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

#Create new dictionary
order = {}

def drink_order():
    """
    Ask each of the questions in the questions dictionary.
    Gather the responses in a new dictionary.
    """
 
    #Create For loop to fill in k,y which is mapped to boolean value"""
    for k,v in questions.items():
        print v #Prints question
        response = raw_input().lower()
        if response == "y" or response == "yes":
            order[k] = True
        else: 
            order[k] = False
    return order 
    
def drink_constructor(order):
    """
    Take preferences from "order" dictionary as parameter
    Append corresponding ingredient
    """
    #List inside function
    menu = []
    for k,v in order.items():
        if v == True:
            print ingredients[v]
    return 
        
if __name__ == '__main__':
    drink_order()
    drink_constructor(order)
    
    