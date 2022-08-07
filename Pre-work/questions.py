# Pre-work Question 1
def hello_name(user_name):
    return f"Hello {user_name}!"


print(hello_name("Ashley"))


# Pre-work Question 2
def first_odds(number):
    for x in range(number):
        if number % 2 != 0:
            print(x)
        return None


print(first_odds(100))


# Pre-Work Question 3
def max_num_in_list(a_list):
    x = sorted(a_list, reverse=True)
    return x[0]


print(max_num_in_list([10,1,32,63,46,100]))


# Pre-Work Question 4
def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


print(is_leap_year(2028))


# Pre-work Question 5
def is_consecutive(a_list):
    prior = 0
    for i in a_list:
        if i-prior ==1:
            print("worked")

        else:
            print("nope")
        prior = i



is_consecutive([1, 2, 4, 5, 6])