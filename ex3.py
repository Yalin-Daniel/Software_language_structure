import sys
import time
from math import factorial
from functools import reduce

sys.setrecursionlimit(3000) # increase the recursion limit to 3000

# yalin daniel 324291590
#ex3- recursive

#question 1
#Regular recursion
def create_tuple(n):
    if n == 0:
        return () # empty tuple
    return create_tuple(n - 1) + (n,)
#Tail recursion
def create_tuple_tail(n, acc=()):
    if n == 0:
        return acc
    return create_tuple_tail(n - 1, (n,) + acc)

#question2
#Regular recursion
def sum_arr(n):
    if len(n) == 0:
        return 0
    return n[0] + sum_arr(n[1:])
#Tail recursion
def sum_arr_tail(n, acc=0):
    if len(n) == 0:
        return acc
    return sum_arr_tail(n[1:], acc + n[0])

#Run it on the tupl you created in the previous section.
numbers = create_tuple(1000)
print(sum_arr(numbers))
print(sum_arr_tail(numbers))


#question 3- A function that accepts two numbers and returns their LCM — the least common multiple.
#Regular recursion
def lcm_regular(a, b, k=1):
    if (a * k) % b == 0:
        return a
    return a + lcm_regular(a, b, k + 1)

#Tail recursion
def lcm_tail(a, b):
    def helper(candidate):
        if candidate % a == 0 and candidate % b == 0:
            return candidate
        return helper(candidate + b)  # Multiplication of one digit

    return helper(b)

#question  4
# Regular recursion
# Regular recursion
def is_palindrome_number(num):
    def is_palindrome(s):
        if len(s) <= 1:
            return True

        return s[0] == s[-1] and is_palindrome(s[1:-1])

    return is_palindrome(str(num))

#Tail recursion
def is_palindrome_number_tail(num):
    def is_palindrome_tail(s, acc=True):
        if len(s) <= 1:
            return acc

        return is_palindrome_tail(
            s[1:-1],
            acc and (s[0] == s[-1])
        )

    return is_palindrome_tail(str(num))

#question 5
#Regular recursion
def is_palindrome_alphanumeric(text):
    def clean_text(s):
        if len(s) == 0:
            return ""
        if s[0].isalnum(): # number or letter
            return s[0].lower() + clean_text(s[1:])
        return clean_text(s[1:])

    def is_palindrome(s):
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return is_palindrome(s[1:-1])
    return is_palindrome(clean_text(text))
#Tail recursion
def is_palindrome_alphanumeric_tail(text):
    def clean_text(s, acc=""):
        if len(s) == 0:
            return acc
        if s[0].isalnum():
            return clean_text(s[1:], acc + s[0].lower())
        return clean_text(s[1:], acc)

    def is_palindrome(s):
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return is_palindrome(s[1:-1])

    return is_palindrome(clean_text(text))

# Main script question 5
text = input("enter text:\n")
if not text.strip():
    print("invalid input")
else:
    print(is_palindrome_alphanumeric(text))


#question  6
#Regular recursion
def sortedzip(list_of_lists):
    def sort_lists(l):
        if not l:
            return ()
        return (sorted(l[0]),) + sort_lists(l[1:])
    return zip(*sort_lists(list_of_lists)) # * Breaks the tuple into separate arguments.
#for example:
# sort_lists([[3,1,2],[5,6,4],['a','b','c']])
#([1,2,3],) + sort_lists([[5,6,4],['a','b','c']])
#([1,2,3],) + ([4,5,6],) + sort_lists([['a','b','c']])
#([1,2,3], [4,5,6], ['a','b','c'])

#Tail recursion
def sortedzip_tail(list_of_lists):
    def sort_lists(l, acc=()):
        if not l:
            return acc
        #return (sorted(l[0]), acc + sort_lists(l[1:]))
        return sort_lists(
            l[1:],
            acc + (sorted(l[0]),)
        )
    return zip(*sort_lists(list_of_lists)) # * Breaks the tuple into separate arguments.

#question 7
#Regular recursion
def encode_rle(text):
    def count_same(text, char, count=0):
        if count < len(text) and text[count] == char:
            return count_same(text, char, count + 1)
        return count
    if len(text) == 0:
        return ""
    # count = 1
    # while count < len(text) and text[count] == text[0]:
    #     count += 1
    count = count_same(text, text[0])
    return  text[0]+ str(count) + encode_rle(text[count:])

#Tail recursion
def encode_rle_tail(text, acc=""):
    def count_same(text, char, count=0):
        if count < len(text) and text[count] == char:
            return count_same(text, char, count + 1)
        return count
    if len(text) == 0:
        return acc
    count = count_same(text, text[0])
    return encode_rle_tail(text[count:], acc + text[0] + str(count))

#main script question 7
text = input("enter text:\n")
if not text.strip():
    print("invalid input")
else:
    print(encode_rle(text))


# Lazy Evaluation, Generators

#question 1.a
# Without using lazy evaluation
def range_10000():
    return list(range(10001))

# Using lazy evaluation
def range_10000_lazy():
    # for i in range(10000):
    #     yield i

    #return (i for i in range(10001))   # Lazy range object from 0 to 10000
    return range(10001)   # Lazy range object from 0 to 10000

# Measure regular version
start = time.perf_counter()
numbers = range_10000()
end = time.perf_counter()

print("question 1.a Without lazy evaluation:")
print("Time:", end - start)
print("Memory:", sys.getsizeof(numbers), "bytes")


# Measure lazy version
start = time.perf_counter()
numbers_lazy = range_10000_lazy()
end = time.perf_counter()

print("\nquestion 1.a With lazy evaluation:")
print("Time:", end - start)
print("Memory:", sys.getsizeof(numbers_lazy), "bytes")

# question 1.b

# Without lazy evaluation
start = time.perf_counter()
arr_without_lazy_5000 = numbers[:5000]
end = time.perf_counter()

print("\nquestion 1.b Without lazy evaluation:")
print("Time:", end - start)
print("Memory:", sys.getsizeof(arr_without_lazy_5000), "bytes")
print("Full type:", type(numbers))
print("New type:", type(arr_without_lazy_5000))


# Using lazy evaluation
start = time.perf_counter()
arr_lazy_5000 = numbers_lazy[:5000]
end = time.perf_counter()

print("\nquestion 1.b With lazy evaluation:")
print("Time:", end - start)
print("Memory:", sys.getsizeof(arr_lazy_5000), "bytes")
print("Full type:", type(numbers_lazy))
print("New type:", type(arr_lazy_5000))

# question 2
def prime_generator():
    num = 2
    while True:
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num
        num += 1

#question 3
#power_function(i) returns a different function each time based on the value of i and then sends it the base X.
def taylor_exp_yield(x):
    result = 0
    i = 0
    while True:
        result += power_function(i)(x) / factorial(i)
        yield result
        i += 1


def power_function(power):
    def power_of(base):
        return base ** power
    return power_of


