
def make_sandwich(*items):
    """ Summarize the sandwich we are about to make."""
    print("Dear costumer this is the sandwich making for you")

    for item in items:
        print(f" {item}")


make_sandwich('cheese')
make_sandwich('ketchup')
make_sandwich('salami')