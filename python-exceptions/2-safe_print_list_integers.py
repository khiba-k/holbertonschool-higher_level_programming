#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    print_int = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
        except IndexError:
            break
        except (ValueError, TypeError):
            continue
        else:
            print_int += 1
    print()
    return print_int

#!/usr/bin/python3
safe_print_list_integers = \
    __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
