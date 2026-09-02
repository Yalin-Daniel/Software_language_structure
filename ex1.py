#yalin daniel 324291590

#question 1
#Section 1-A
def get_penta_num(n):
    return n*(3*n - 1)//2

# Section 1-B
def pentaNumRange(n1,n2):
    return list(map(get_penta_num, range(n1, n2)))

#question 2
#str- convert the number to string, map- apply int function to each character in the string, sum- sum the resulting integers
def sum_digit(n):
    if not isinstance(n, int):
        return "invalid input"
    return sum(map(int, str(abs(n))))

# Main script - question 2
user_input = input("enter number:\n")

try:
    number = int(user_input)
    print(sum_digit(number))
except ValueError:
    print("invalid input")


#question 3
#Section 3-A
# sorted return a sorted list, join- join the sorted characters back into a string
def normalize_text(text):
    text = text.lower().replace(" ", "")
    return ''.join(sorted(text))

#Section 3-B
def are_anagrams(str1, str2):
    return normalize_text(str1) == normalize_text(str2)

# Main script - question 3
str1 = input("enter first text:\n")
str2 = input("enter second text:\n")

if not str1.strip() or not str2.strip():
    print("invalid input")
else:
    print(are_anagrams(str1, str2))

#question 4
def gematria_val(text):
    if not isinstance(text, str):
        return "invalid input"

    gematria = { #not global variable, for Pure function
        'א': 1,
        'ב': 2,
        'ג': 3,
        'ד': 4,
        'ה': 5,
        'ו': 6,
        'ז': 7,
        'ח': 8,
        'ט': 9,
        'י': 10,
        'כ': 20,
        'ך': 20,
        'ל': 30,
        'מ': 40,
        'ם': 40,
        'נ': 50,
        'ן': 50,
        'ס': 60,
        'ע': 70,
        'פ': 80,
        'ף': 80,
        'צ': 90,
        'ץ': 90,
        'ק': 100,
        'ר': 200,
        'ש': 300,
        'ת': 400
    }

    return sum(gematria[char] for char in text)

#question 5
#Section 5-A

# n > 1 checks that the number can be prime.
# range(2, int(n**0.5) + 1) generates possible divisors only up to the square root of n.
# n % i != 0 checks that n is not divisible by each possible divisor.
# all(...) returns True only if none of the possible divisors divides n.
#For each i in the range, check the condition
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

#section 5-B
#According to the question, the input is assumed to be a prime number.
def find_twin_primes(prime):
    if is_prime(prime+2):
        return prime +2
    elif is_prime(prime-2):
        return prime -2
    return "no twin prime found"


# Main script - question 5
number = input("enter number:\n")
if not number.isdigit():
    print("invalid input")
else:
    number = int(number)

    if not is_prime(number):
        print("invalid input")
    else:
        twin = find_twin_primes(number)

        if twin == "no twin prime found":
            print("invalid input")
        else:
            print(twin)

#section 5-C
# Section 5-C
def twin_primes_dict(n):
    return {
        prime: find_twin_primes(prime)
        for prime in range(2, n + 1)
        if is_prime(prime) and find_twin_primes(prime) != "no twin prime found"
    }


##question 6

# def add_3_dicts(d1, d2, d3): Still not removing duplicates well
#     result = {}
#     # | is union
#     all_keys = set(d1.keys()) | set(d2.keys()) | set(d3.keys())
#
#     for key in all_keys:
#         #For each dictionary d from d1, d2, d3, if key is in it — take d[key] which is actually the value
#         values = [d[key] for d in (d1, d2, d3) if key in d]
#         # remove duplicates
#         values = list(dict.fromkeys(values))
#         result[key] = tuple(values)
#     return result

#There is a change of result and values here, but only within the function, so it's okay.
def add_3_dicts(d1, d2, d3):
    result = {}
    all_keys = set(d1.keys()) | set(d2.keys()) | set(d3.keys())
    for key in all_keys:
        values = []
        for d in (d1, d2, d3):
            if key in d and d[key] not in values:
                values.append(d[key])
        result[key] = tuple(values)
    return result

#question 7
#section 7-A
def multiply_by_2(x):
    return x * 2

def square(x):
    return x ** 2

def reciprocal(x):
    return 1 / x

functions = [multiply_by_2, square, reciprocal]

#section 7-B
def apply_functions(num_list, func_list):
    return {
       func.__name__: [func(num) for num in num_list]
        # func.__name__ - Atbatrib  suitable
        # the key is the function name, the value is a list of results of applying the function to each number in num_list
       for func in func_list # for each function in the list
    }


# print("\n========== START TESTS ==========\n")
#
#
# # --------------------
# # Question 1
# # --------------------
# print("Testing Question 1...")
#
# assert get_penta_num(1) == 1
# assert get_penta_num(2) == 5
# assert get_penta_num(3) == 12
# assert get_penta_num(4) == 22
#
# assert pentaNumRange(1, 5) == [1, 5, 12, 22]
# assert pentaNumRange(2, 4) == [5, 12]
#
# print("Question 1 PASSED")
#
#
# # --------------------
# # Question 2
# # --------------------
# print("\nTesting Question 2...")
#
# assert sum_digit(123) == 6
# assert sum_digit(905) == 14
# assert sum_digit(0) == 0
# assert sum_digit(-123) == 6
# assert sum_digit("123") == "invalid input"
# assert sum_digit(12.5) == "invalid input"
#
# print("Question 2 PASSED")
#
#
# # --------------------
# # Question 3
# # --------------------
# print("\nTesting Question 3...")
#
# assert normalize_text("Silent") == "eilnst"
# assert normalize_text("Hello World") == "dehllloorw"
#
# assert are_anagrams("Silent", "Listen") == True
# assert are_anagrams("hello", "olleh") == True
# assert are_anagrams("Hello", "World") == False
# assert are_anagrams("Dormitory", "Dirty room") == True
#
# print("Question 3 PASSED")
#
#
# # --------------------
# # Question 4
# # --------------------
# print("\nTesting Question 4...")
#
# assert gematria_val("אבג") == 6
# assert gematria_val("י") == 10
# assert gematria_val("שלום") == 376
# assert gematria_val("כך") == 40
# assert gematria_val(123) == "invalid input"
#
# print("Question 4 PASSED")
#
#
# # --------------------
# # Question 5-A
# # --------------------
# print("\nTesting Question 5-A...")
#
# assert is_prime(2) == True
# assert is_prime(3) == True
# assert is_prime(11) == True
# assert is_prime(23) == True
#
# assert is_prime(1) == False
# assert is_prime(0) == False
# assert is_prime(4) == False
# assert is_prime(25) == False
# assert is_prime(100) == False
#
# print("Question 5-A PASSED")
#
#
# # --------------------
# # Question 5-B
# # --------------------
# print("\nTesting Question 5-B...")
#
# assert find_twin_primes(3) == 5
# assert find_twin_primes(5) == 7
# assert find_twin_primes(11) == 13
# assert find_twin_primes(13) == 11
# assert find_twin_primes(17) == 19
# assert find_twin_primes(23) == "no twin prime found"
#
# print("Question 5-B PASSED")
#
#
# # --------------------
# # Question 5-C
# # --------------------
# print("\nTesting Question 5-C...")
#
# expected_twins = {
#     3: 5,
#     5: 7,
#     7: 5,
#     11: 13,
#     13: 11,
#     17: 19,
#     19: 17
# }
#
# assert twin_primes_dict(20) == expected_twins
#
# print("Question 5-C PASSED")
#
#
# # --------------------
# # Question 6
# # --------------------
# print("\nTesting Question 6...")
#
# d1 = {
#     'a': 1,
#     'b': 2,
#     'c': 10
# }
#
# d2 = {
#     'a': 3,
#     'b': 2,
#     'd': 4
# }
#
# d3 = {
#     'a': 1,
#     'b': 5,
#     'e': 7
# }
#
# result = add_3_dicts(d1, d2, d3)
#
# assert result['a'] == (1, 3)
# assert result['b'] == (2, 5)
# assert result['c'] == (10,)
# assert result['d'] == (4,)
# assert result['e'] == (7,)
#
# # Check that original dictionaries did not change
# assert d1 == {'a': 1, 'b': 2, 'c': 10}
# assert d2 == {'a': 3, 'b': 2, 'd': 4}
# assert d3 == {'a': 1, 'b': 5, 'e': 7}
#
# print("Question 6 PASSED")
#
#
# # --------------------
# # Question 7-A
# # --------------------
# print("\nTesting Question 7-A...")
#
# assert multiply_by_2(5) == 10
# assert square(5) == 25
# assert reciprocal(4) == 0.25
#
# assert functions == [multiply_by_2, square, reciprocal]
#
# print("Question 7-A PASSED")
#
#
# # --------------------
# # Question 7-B
# # --------------------
# print("\nTesting Question 7-B...")
#
# numbers = [1, 2, 4]
#
# expected = {
#     'multiply_by_2': [2, 4, 8],
#     'square': [1, 4, 16],
#     'reciprocal': [1.0, 0.5, 0.25]
# }
#
# assert apply_functions(numbers, functions) == expected
#
# print("Question 7-B PASSED")
#
#
# print("\n========== ALL TESTS PASSED ==========")