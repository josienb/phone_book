from sys import argv


def create_phonebook(phonebook_name):
    """Create a new phone book file if it does not exist already."""
    # pass
    print "Create a phonebook called %s" % phonebook_name


def add_entry(name, number, phonebook_name):
    """Add a new name and number to the given phonebook"""
    # pass
    print "Added %s with number %s to %s" % (name, number, phonebook_name)


def update(name, number, phonebook_name):
    # pass
    print "Updated %s with number %s in %s" % (name, number, phonebook_name)


def lookup(name, phonebook_name):
    # pass
    print "Looking up %s in %s" % (name, phonebook_name)


def reverse_lookup(number, phonebook_name):
    # pass
    print "Looking up %s in %s" % (number, phonebook_name)


def delete(name, phonebook_name):
    # pass
    print "Deleting %s from %s" % (name, phonebook_name)


if __name__ == "__main__":
    try:
        # Some argument checking should be done here (?)
        # Does the number of arguments provided match the given command?
        # arg1 = argv[1]

        args = argv[:]
        script = args.pop(0)
        command = args.pop(0)

        if command == 'create':
            phonebook_name = args.pop(0)
            if args == []:
                create_phonebook(phonebook_name)
            else:
                print("Too many arguments given")

        elif command == 'add':
            name = args.pop(0)
            number = args.pop(0)
            phonebook_name = args.pop(0)
            if args == []:
                add_entry(name, number, phonebook_name)
            else:
                print("Too many arguments given")

        elif command == 'update':
            name = args.pop(0)
            number = args.pop(0)
            phonebook_name = args.pop(0)
            if args == []:
                update(name, number, phonebook_name)
            else:
                print("Too many arguments given")

        elif command == 'lookup':
            name = args.pop(0)
            phonebook_name = args.pop(0)
            if args == []:
                lookup(name, phonebook_name)
            else:
                print("Too many arguments given")

        elif command == 'reverse_lookup':
            number = args.pop(0)
            phonebook_name = args.pop(0)
            if args == []:
                reverse_lookup(number, phonebook_name)
            else:
                print("Too many arguments given")

        elif command == 'delete':
            name = args.pop(0)
            phonebook_name = args.pop(0)
            if args == []:
                delete(name, phonebook_name)
            else:
                print("Too many arguments given")

    except IndexError:
        # Not enough parameters! User might need some guidance!
        print("PLACEHOLDER: help text with commands and parameters.")
        exit(1)
