def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    
    if age:
        person['age'] = age
    return person

teacher = build_person('ximena','rogers', age=30)
print(teacher)