from sys import argv


def create_phonebook(phonebook_name):
    """Create a new phone book file if it does not exist already."""
    pass

def add_entry(name, number, phonebook_name):
    # add a new name and number to the given phonebook
    pass

def update(name, number, phonebook_name):
    pass

def lookup(name, phonebook_name):
    pass

def reverse_loopup(number, phonebook_name):
    pass 

def delete(name, phonebook_name):
    pass    


if __name__ == "__main__":
    try:
        # Some argument checking should be done here (?)
        # Does the number of arguments provided match the given command?
        arg1 = argv[1]
    except IndexError:
        # Not enough parameters! User might need some guidance!
        print("PLACEHOLDER: help text with commands and parameters.")
        exit(1)
