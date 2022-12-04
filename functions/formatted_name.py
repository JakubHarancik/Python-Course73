def get_formatted_name(first_name, last_name):
    """ Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
#This is a infinite loop

while True:
    print("\nPlease tell me your name:")
    print("Enter 'q' or 'Q' at any time to quit")
    f_name = input("First name: ")
    if f_name =='q':
        break
    if f_name =='Q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    if l_name == 'Q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


#musician = get_formatted_name('shakira', 'merabak')
#print(musician)