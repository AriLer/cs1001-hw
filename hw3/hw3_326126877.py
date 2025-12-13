# Skeleton file for HW3 - Spring 2025 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.
# you can add new functions if needed.

# Change the name of the file to include your ID number (hw3_ID.py).

import random  # loads python's random module to use in Q5

##############
# QUESTION 2 #
##############

# Q2_a


def find_root(f, L, U, eps=10**-1000):
    """Find root of f using intermediate value theorem.
    Assume f is continuous, L<U and f(L) < 0 < f(U).
    eps is how far you allow f to be from 0.0
    """
    assert L < U and f(L) < 0 and f(U) > 0

    M = (L + U) / 2
    while L < M and M < U:
        fM = f(M)
        print("searching in (", L, ",", U, ")")
        if abs(fM) < eps:
            print("Found an approximated root")
            return M
        elif fM < 0:
            L = M  # continue search in upper half
        else:  # fM > 0
            U = M  # continue search in lower half
        M = (L + U) / 2

    # if we got here no root was found (try increasing eps)
    return None


# Q2_f


def find_log(m, eps=10**-10):
    log = find_root(lambda x: 2**x - m, 0, m, eps)
    return log


##############
# QUESTION 3 #
##############
# Q3_a
def string_to_int(s):
    char_dict = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4}
    total_value = 0
    for i in range(len(s)):
        total_value = (total_value * 5) + char_dict[s[i]]
    return total_value


# Q3_b
def int_to_string(k, n):
    char_dict = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4}
    str = ["a"] * k

    for i in range(k - 1, -1, -1):
        remainder = n % 5
        for key, value in char_dict.items():
            if value == remainder:
                str[i] = key
                break
        n = n // 5

    return "".join(str)


# Q3_c
def sort_strings1(lst, k):
    help_lst = [""] * (5**k)
    for s in lst:
        index = string_to_int(s)
        if help_lst[index] == "":
            help_lst[index] = s
        else:
            help_lst.insert(index, s)
    sorted_lst = []
    for s in help_lst:
        if s != "":
            sorted_lst.append(s)

    return sorted_lst


# Q3_e
def sort_strings2(lst, k):
    sorted_lst = []
    for i in range(5**k):
        for s in lst:
            index = string_to_int(s)
            if index == i:
                sorted_lst.append(s)
    return sorted_lst


##############
# QUESTION 4 #
##############


# Q4_2c
def find_almost_1(lst, s):
    low, high = 0, len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == s:
            return mid
        if mid - 1 >= 0 and lst[mid - 1] == s:
            return mid - 1
        if mid + 1 < len(lst) and lst[mid + 1] == s:
            return mid + 1
        if s < lst[mid]:
            high = mid - 2
        else:
            low = mid + 2
    return None


# Q4_3a
def find_percentile_almost_k(lst, k, m):
    global_smaller_count = m - 1
    sub_lst_start = max(0, global_smaller_count - k)
    sub_lst_end = min(len(lst) - 1, global_smaller_count + k)
    
    sub_lst = lst[sub_lst_start : sub_lst_end + 1]
    local_smaller_count = global_smaller_count - sub_lst_start

    left = 0
    right = len(sub_lst) - 1

    while True:
        if left == right:
            return sub_lst[left]

        mid = sub_lst[(left + right) // 2]

        i, j = left, right
        while i <= j:
            while sub_lst[i] < mid:
                i += 1
            while sub_lst[j] > mid:
                j -= 1
            if i <= j:
                sub_lst[i], sub_lst[j] = sub_lst[j], sub_lst[i]
                i += 1
                j -= 1
                
        if local_smaller_count <= j:
            right = j
        elif local_smaller_count >= i:
            left = i
        else:
            return sub_lst[local_smaller_count]


##############
# QUESTION 5 #
##############
# Q5_a
def edit_distance(st1, st2):
    if len(st1) == 0:
        return len(st2)
    if len(st2) == 0:
        return len(st1)
    if st1[0] == st2[0]:
        return edit_distance(st1[1:], st2[1:])
    op1 = edit_distance(st1[1:], st2)
    op2 = edit_distance(st1, st2[1:])
    op3 = edit_distance(st1[1:], st2[1:])
    return min(op1, op2, op3) + 1


# Q5_a
def relevancy_score(text, promote, L):
    score = 1
    if promote:
        score = 2

    min_distance = edit_distance(text, L[0])
    for keyword in L:
        distance = edit_distance(text, keyword)
        if distance < min_distance:
            min_distance = distance

    score = score * (1 / (1 + (min_distance**2)))
    return score


# Q5_b
import random


def PageRank_search(G, t, p, text, pages_desc, pages_promote):
    relevancies = [
        relevancy_score(text, pages_promote[i], pages_desc[i]) for i in range(len(G))
    ]
    counter = [0] * len(G)
    curr = 0

    for turn in range(t):
        counter[curr] += 1

        if G[curr] and random.random() < p:
            neighbors = G[curr]
            weights = [relevancies[v] for v in neighbors]
            curr = random.choices(neighbors, weights=weights)[0]
        else:
            curr = random.choices(range(len(G)), weights=relevancies)[0]

    # נרמול הביקורים
    total_visits = sum(counter)
    return [v / total_visits for v in counter]

##########
# Tester #
##########


def test():
    # Q3
    if string_to_int("aa") != 0 or string_to_int("aba") != 5:
        print("error in string_to_int")
    lst_num = [random.choice(range(5**4)) for i in range(15)]
    for i in lst_num:
        s = int_to_string(4, i)
        if s is None or len(s) != 4:
            print("error in int_to_string")
        if string_to_int(s) != i:
            print("error in int_to_string and/or in string_to_int")

    lst1 = [
        "aede",
        "adae",
        "dded",
        "deea",
        "cccc",
        "aacc",
        "edea",
        "becb",
        "daea",
        "ccea",
        "aacc",
    ]
    if sort_strings1(lst1, 4) != [
        "aacc",
        "aacc",
        "adae",
        "aede",
        "becb",
        "cccc",
        "ccea",
        "daea",
        "dded",
        "deea",
        "edea",
    ]:
        print("error in sort_strings1")
    if sort_strings2(lst1, 4) != [
        "aacc",
        "aacc",
        "adae",
        "aede",
        "becb",
        "cccc",
        "ccea",
        "daea",
        "dded",
        "deea",
        "edea",
    ]:
        print("error in sort_strings2")

    # Q4
    almost_sorted_lst_3 = [10, 7, 7, 1]
    if find_percentile_almost_k(almost_sorted_lst_3, 3, 1) != 1:
        print("error in find_percentile_almost_k")
    if find_percentile_almost_k(almost_sorted_lst_3, 3, 2) != 7:
        print("error in find_percentile_almost_k")
    if find_percentile_almost_k(almost_sorted_lst_3, 3, 3) != 7:
        print("error in find_percentile_almost_k")

    # Q5
    if edit_distance("sport", "spotr") != 2 or edit_distance("workout", "wrkout") != 1:
        print("error in edit_distance")

    if relevancy_score("spotr", True, ["sport", "gym", "workout"]) != 0.4:
        print("error in relevancy_score")


test()


# השאלה הבאה נתנה לי בעבודה. תממש את הפונקציה הנדרשת בסעיף ב' תוך כדי שימוש בפונקציה
