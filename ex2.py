import time
from functools import reduce
from datetime import datetime, timedelta
from math import factorial


#yalin324291590
#question 1
linear_func = lambda x: x / 2 + 2

#section 1-1
numbers = tuple(range(0, 10001))
new_list = tuple(map(linear_func, numbers))

#section 1-2
#sum_new_list = sum(new_list)
# reduce-Super function- like map but it reduces the list to a single value by applying a function cumulatively to the items of the iterable
sum_new_list = reduce(
    lambda x, y: x + y,
    new_list
)

# Section 1-3
start = time.time()
sum_functional = reduce(lambda x, y: x + y, new_list)
functional_time = time.time() - start

start = time.time()
sum_imperative = 0
for num in new_list:
    sum_imperative += num
imperative_time = time.time() - start

print("Functional time:", functional_time)
print("Imperative time:", imperative_time)

# Section 1-4
#reduce(function, collection, initial_value)
sum_direct = reduce(
    lambda total, num: total + linear_func(num),
    numbers,
    0
)

# question 2
numbers = tuple(range(1, 1001))
even_numbers = tuple(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = tuple(filter(lambda x: x % 2 != 0, numbers))

# Section 2-1
multiply = lambda total, next_num: total * next_num
odd_func = lambda total, next_num: total // 2 + 2 + next_num

# Section 2-2
even_result = reduce(multiply, even_numbers, 1)
odd_result = reduce(odd_func, odd_numbers)

# Section 2-3
total_result = reduce(
    lambda x, y: x + y,
    (even_result, odd_result)
)

# question 3
def is_armstrong(n):
    return n==sum(map(lambda x: int(x)**len(str(n)), str(n)))

# Section 3.2
def armstrong_range(n1, n2):
    return tuple(filter(is_armstrong, range(n1, n2 + 1)))

# Section 3-C - Main script
user_input = input("enter number:\n")
if not user_input.isdigit() or int(user_input) <= 0:
    print("invalid input")
else:
    #n = int(user_input)
    print(armstrong_range(1, int(user_input)))


# question 4
def create_dates(date_str, count, skip):
    start_date = datetime.strptime(date_str, "%d/%m/%Y")
    return tuple(
        map(
            lambda i: (start_date + timedelta(days=i * skip)).strftime("%d/%m/%Y"),
            range(count)
        )
    )

# question 5
#section 5-A
def power_function(power):
    def power_of(base):
        return base ** power
    return power_of

#section 5-B
def power_map(n):
    return map(power_function, range(n))

#section 5- Main script
n = int(input("Enter number of powers: "))
result = power_map(n)
print(type(result))
base = int(input("Enter base: "))
#answer = tuple(map(lambda func: func(base), result))
#print(answer)
print(tuple(map(lambda func: func(base), result))) #Runs each of the functions on the result on base.

#section 5-C
# reduce(function, collection, initial_value)-
# The first receives the cumulative result, and the second receives the next element from the collection each time.

#power_function(i) returns a different function each time based on the value of i and then sends it the base X.
def taylor_exp(x, n):
    return reduce(
        lambda total, i: total + power_function(i)(x) / factorial(i),
        range(n+1),
        0
    )

# question 6
def task_manager():
    tasks = {}

    def add_task(task_name, status="incomplete"):
        tasks[task_name] = status

    def get_tasks():
        return tasks

    def complete_task(task_name):
        if task_name in tasks:
            tasks[task_name] = "complete"

    return {
        "add_task": add_task,  # add_task- return the function itself
        "get_tasks": get_tasks,
        "complete_task": complete_task
    }

# question 7
# section 7-A
def clean_spaces(text):
    return text.strip()

def capitalize_text(text):
    return text.title()

def add_stars(text):
    return "***" + text + "***"

# section 7-B

def create_pipeline():# Identity function returns the input exactly as it was received
    return lambda x: x

def add_to_pipeline(pipeline_fn, new_fn):
    # Create and return a new function.
    # First, the existing pipeline is executed on x.
    # Then, new_fn is executed on the result of the existing pipeline.
    return lambda x: new_fn(pipeline_fn(x))

# Section 7-C - Main script
pipeline = create_pipeline()
pipeline = add_to_pipeline(pipeline, clean_spaces)
pipeline = add_to_pipeline(pipeline, capitalize_text)
pipeline = add_to_pipeline(pipeline, add_stars)

text = input("enter text:\n")
if text.strip() == "":
    print("input invalid")
else:
    print(pipeline(text))



