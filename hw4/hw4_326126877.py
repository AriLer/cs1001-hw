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
def init_max_v1_improved(L):
    def max_v1_improved(start, end):
        if start == end:
            return L[start]

        mid = (start + end) // 2
        first_half = max_v1_improved(start, mid)
        second_half = max_v1_improved(mid + 1, end)

        return max(first_half, second_half)

    return max_v1_improved(0, len(L) - 1)


def init_max_v2_improved(L):

    def max_v2_improved(start):
        if start == len(L) - 1:
            return L[start]
       
        without_left = max_v2_improved(start + 1) 
        return max(without_left, L[start])

    return max_v2_improved(0)

# 2c
def reverse(L):
    reversed = []
    for i in range(len(L) - 1, -1 ,-1):
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
    if tuple(L) in memo:
        return memo[tuple(L)]
    
    if all([elem == 0 for elem in L]):
        return 1
    
    result = 0
    for i in range(len(L)):
        if L[i] != 0:
            L[i] -= 1
            memo[tuple(L)] = cnt_paths_mem(L, memo)
            L[i] += 1
    return result

def test_cnt_paths():
    # Base Case: Already at the origin
    assert cnt_paths_mem([0, 0]) == 1
    
    # Single Dimension: Only 1 path possible (straight line)
    print("cnt_paths_mem([5]): ", cnt_paths_mem([5]))
    assert cnt_paths_mem([5]) == 1

    # 2D Grid (2x2): Should be 6 paths (4 choose 2)
    # Paths: (1,1,0,0) permutations: RRYY, RYRY, RYYR, YRYR, YRRY, YYRR
    assert cnt_paths_mem([2, 2]) == 6
test_cnt_paths()


def cnt_paths_iter(L):
    pass  # replace this with your code


##############
# Question 4 #
##############
# 4a
def legal_path(A, vertices):
    pass  # replace this with your code


# 4c
def path_v2(A, s, t, k):
    if k == 0:
        return s == t

    # ADD YOUR CODE HERE #

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

    pass  # replace this with your code


# 5b


def can_create_twice(s, lst):

    pass  # replace this with your code


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
