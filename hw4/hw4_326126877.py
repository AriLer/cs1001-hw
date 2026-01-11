# Skeleton file for HW4 - winter 2025-2026 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw4_<ID>.py).
import math, random, time

##############
# Question 1 #
##############


def quicksort(lst, rand=True):
    """quick sort of lst"""
    if len(lst) <= 1:
        return lst
    else:
        pivot = random.choice(lst) if rand else lst[0]
        smaller = [elem for elem in lst if elem < pivot]
        equal = [elem for elem in lst if elem == pivot]
        greater = [elem for elem in lst if elem > pivot]

        return quicksort(smaller, rand) + equal + quicksort(greater, rand)


def quick_comparison_random_input(n, t):
    deterministic_time = 0
    random_time = 0

    for _ in range(t):
        random_list = list(range(1, n + 1))
        random.shuffle(random_list)

        start_time = time.perf_counter()
        quicksort(random_list, rand=False)
        end_time = time.perf_counter()
        deterministic_time += end_time - start_time

        start_time = time.perf_counter()
        quicksort(random_list, rand=True)
        end_time = time.perf_counter()
        random_time += end_time - start_time

    return (random_time / t, deterministic_time / t)


def quick_comparison_ordered_input(n, t):
    deterministic_time = 0
    random_time = 0

    for _ in range(t):
        ordered_list = list(range(1, n + 1))
        start_time = time.perf_counter()

        quicksort(ordered_list, rand=False)
        end_time = time.perf_counter()
        deterministic_time += end_time - start_time

        start_time = time.perf_counter()
        quicksort(ordered_list, rand=True)
        end_time = time.perf_counter()
        random_time += end_time - start_time

    return (random_time / t, deterministic_time / t)


##############
# Question 2 #
##############


# TODO: Question 2 - a (drawing the binary recursion tree)
# 2b
def max_v1_improved(L):
    def step(start, end):
        if start == end:
            return L[start]

        mid = (start + end) // 2
        first_half = step(start, mid)
        second_half = step(mid + 1, end)

        return max(first_half, second_half)

    return step(0, len(L) - 1)


def max_v2_improved(L):

    def step(start):
        if start == len(L) - 1:
            return L[start]

        without_left = step(start + 1)
        return max(without_left, L[start])

    return step(0)


# 2c
def reverse(L):
    reversed = []
    for i in range(len(L) - 1, -1, -1):
        reversed.append(L[i])
    return reversed


##############
# Question 3 #
##############


def cnt_paths(L):
    if all([elem == 0 for elem in L]):
        return 1

    result = 0
    for i in range(len(L)):
        if L[i] != 0:
            L[i] -= 1
            result += cnt_paths(L)
            L[i] += 1
    return result


def cnt_paths_mem(L, memo={}):

    state = tuple(L)

    if state in memo:
        return memo[state]

    if all(elem == 0 for elem in L):
        return 1

    result = 0
    for i in range(len(L)):
        if L[i] != 0:
            L[i] -= 1
            result += cnt_paths_mem(L, memo)
            L[i] += 1

    memo[state] = result
    return result


import timeit


def cnt_paths_iter(L):
    d = len(L)
    # dctionary there each entry is a tuple of the coordinates and the number of paths to reach it
    path_counts = {tuple([0] * d): 1}

    curr_loc = [0] * d

    while True:

        if any(x > 0 for x in curr_loc):
            total = 0
            for i in range(d):
                if curr_loc[i] > 0:
                    curr_loc[i] -= 1
                    total += path_counts[tuple(curr_loc)]
                    curr_loc[i] += 1
            path_counts[tuple(curr_loc)] = total

        for i in range(d - 1, -1, -1):
            if curr_loc[i] < L[i]:
                curr_loc[i] += 1
                for j in range(i + 1, d):
                    curr_loc[j] = 0
                break
        else:
            break

    return path_counts[tuple(L)]


##############
# Question 4 #
##############
# 4a
def legal_path(A, vertices):
    for i in range(len(vertices) - 1):
        if A[vertices[i]][vertices[i + 1]] == 0:
            return False
    return True


# 4c
def path_v2(A, s, t, k):
    if k == 0:
        return s == t

    if k == 1:
        return A[s][t] == 1

    for i in range(len(A)):
        mid = k // 2
        if path_v2(A, s, i, mid) and path_v2(A, i, t, k - mid):
            return True
    return False


# 4d # Fix this code without deleting any existing code #
def path_v4(A, s, t):
    L = [False for i in range(len(A))]
    return path_rec(A, s, t, L)


def path_rec(A, s, t, L):
    if s == t:
        return True

    for i in range(len(A)):
        if A[s][i] == 1:
            if path_rec(A, i, t, L):
                return True
    return False


##############

# Question 5 #

##############


# 5a
def can_create_once(s, lst):
    def solve(cur_sum, idx):
        if idx == len(lst):
            return cur_sum == s

        add = solve(cur_sum + lst[idx], idx + 1)
        sub = solve(cur_sum - lst[idx], idx + 1)
        return add or sub

    return solve(0, 0)


# 5b


def can_create_twice(s, lst):
    if not lst:
        return s == 0

    val, *rest = lst

    return any(can_create_twice(s - k * val, rest) for k in [0, 1, -1, 2, -2])


# 5c


def valid_brackets_placement(s, lst):
    pass  # replace this with your code


##########
# Tester #
##########
def test():

    # 2b
    if max_v1_improved([1, 5, 3, 4, -1]) != 5 or max_v1_improved([1]) != 1:
        print("error in max_v1_improved")

    if max_v2_improved([1, 5, 3, 4, -1]) != 5 or max_v2_improved([1]) != 1:
        print("error in max_v2_improved")

    # 2c
    if reverse([1, 5, "hello"]) != ["hello", 5, 1] or reverse([1]) != [1]:
        print("error in reverse")

    # 3b
    if cnt_paths([3, 4, 3]) != cnt_paths_mem([3, 4, 3]):
        print("error in cnt_pths_mem")

    # 3d
    if cnt_paths([3, 4, 3]) != cnt_paths_iter([3, 4, 3]):
        print("error in cnt_pths_mem")

    # 4a
    A = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    if (
        not legal_path(A.copy(), [0, 1, 2, 3])
        or not legal_path(A.copy(), [0, 1, 2, 3, 0, 1])
        or legal_path(A.copy(), [1, 2, 3, 4])
    ):
        print("error in legal_path")

    # 5a
    if (
        not can_create_once(6, [5, 2, 3])
        or not can_create_once(-10, [5, 2, 3])
        or can_create_once(9, [5, 2, 3])
        or can_create_once(7, [5, 2, 3])
    ):
        print("error in can_create_once")

    # 5b
    if (
        not can_create_twice(6, [5, 2, 3])
        or not can_create_twice(9, [5, 2, 3])
        or not can_create_twice(7, [5, 2, 3])
        or can_create_once(19, [5, 2, 3])
    ):
        print("error in can_create_twice")

    # 5c
    lst = ["6", "-", "4", "*", "2", "+", "3"]
    if (
        not valid_brackets_placement(10, lst.copy())
        or not valid_brackets_placement(1, lst.copy())
        or valid_brackets_placement(5, lst.copy())
    ):
        print("error in valid_brackets_placement")


test()
