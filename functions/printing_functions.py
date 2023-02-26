#1 Put some  functions in a seperate file called printing_functions.py
#    Write an import statement at the top of printing_functions.py, and  modify  the file to use imported functions

#2 Using program you wrote that has one function in it, store that function in a seperate file.
# Import that function into your main program file, and call the function using the aprroached we saw last class
# for example: import module_name
# from module_name import function_name
# import module_name as mn
# from module_name import *

def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until there are none left"""
    """Move each design to completed_models after printing  """

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating the 3d print from desing
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("The following models have been printed") 
    for completed_model in completed_models:
        print(f"{completed_model}")

