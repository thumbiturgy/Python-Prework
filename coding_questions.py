
def hello_name(user_name):
    """Question 1"""
    print(f"hello_{user_name.upper()}")
hello_name('username')

def first_odds():
    """Question 2"""
    for odd in range(1, 101, 2):
        print(odd)

first_odds()

def max_num_in_list(a_list):
    """Question 3"""
    highest = max(a_list)
    return highest
print(max_num_in_list([5, 7, 33, 56]))


def is_leap_year(a_year):
    """Question 4"""
    if a_year % 4 == 0 and a_year % 100 != 0 or a_year % 400 == 0:
        leap_year = True
    else:
        leap_year = False
    return leap_year
print(is_leap_year(308))
print(is_leap_year(200))


def is_consecutive(a_list):
    """Question 5"""
    if sorted(a_list) == list(range(min(a_list), max(a_list)+1)):
        if len(a_list) == max(a_list) - min(a_list) + 1:
            return True

    return False

my_list = [5, 6, 7, 8]
my_new_list = [17, 5, 89]

print(is_consecutive(my_list))
print(is_consecutive(my_new_list))