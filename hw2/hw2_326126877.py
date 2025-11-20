import random  # loads python's `random` module in order to use `random.random()` in question 2.


##############
# QUESTION 1 #
##############
# Q1.2
def char_count(text):
    d = {}
    for ch in text:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    return d


##############
# QUESTION 2 #
##############
# Q2a
def coin():
    # not quite 50 / 50. if lands on 0.5 (exact middle), still returns true
    rand = random.random()
    return rand < 0.5


# Q2b
def sample(v, p):
    rand = random.random();
    value = v[0]
    for i in range(len(p)):
        if i > 0:
            p[i] = p[i] + p[i-1]
            if rand > p[i-1] and rand <= p[i]:
                val = v[i]
                break
        else:
            if rand <= p[i]:
                val = v[i]
                break
        return value

# ) Q2c
# ! DO NOT FORGET
def monty_hall(switch, times):
    pass  # TODO replace with your code


# Q2d

def sample_anagram(st):
    pass  # TODO replace with your code


##############
# QUESTION 3 #
##############
# Q3a
def inc(binary):
    pass  # TODO replace with your code


# Q3b
def add(bin1, bin2):
    pass  # TODO replace with your code


# Q3c
def mod_two(binary, power):
    pass  # TODO replace with your code


# Q3d
def max_bin(lst):
    pass  # TODO replace with your code


##############
# QUESTION 4 #
##############


# Q4a1
def is_student_available(office_hour, student_schedule):
    pass  # TODO replace with your code


# Q4a2
def assess_office_hour(office_hour, student_schedules_dict):
    pass  # TODO replace with your code


# Q4b1
def merge_intervals(intervals):
    pass  # TODO replace with your code


# Q4b2
def find_perfect_slots(student_schedules_dict):
    pass  # TODO replace with your code


##########
# Tester #
##########


def test():
    # Testing Question 2:
    for i in range(10):
        if coin() not in {True, False}:
            print("Error in Q2a")
            break

    for i in range(10):
        sampled_elem = sample(list("abc"), [0.4, 0.6, 0.0])
        if sampled_elem not in set("ab"):
            print("Error in Q2b")
            break

    for i in range(10):
        if monty_hall(True, 4) not in {0.0, 0.25, 0.5, 0.75, 1.0}:
            print("Error in Q2c")
            break

    for i in range(10):
        st = "SILENT_PAR"
        if sorted(sample_anagram(st)) != sorted(st):
            print("Error in Q2d")
            break

    # Testing Question 3:
    if (
        inc("0") != "1"
        or inc("1") != "10"
        or inc("101") != "110"
        or inc("111") != "1000"
        or inc(inc("111")) != "1001"
    ):
        print("Error in Q3a")

    if (
        add("0", "1") != "1"
        or add("1", "1") != "10"
        or add("110", "11") != "1001"
        or add("111", "111") != "1110"
    ):
        print("Error in Q3b")

    if (
        mod_two("110", 2) != "10"
        or mod_two("101", 2) != "1"
        or mod_two("111", 4) != "111"
    ):
        print("Error in Q3c")

    if max_bin(["1010", "1011"]) != "1011":
        print("Error in Q3d - 1")

    if max_bin(["10", "0", "1"]) != "10":
        print("Error in Q3d - 2")

    # Testing Question 4:
    office_hour = (11, 12)
    student_schedules_dict = {
        "noam": [(8, 10), (10, 12), (15, 18)],
        "larry": [(10, 11), (14, 16)],
        "jeff": [(10, 11), (14, 16)],
    }
    if set(assess_office_hour(office_hour, student_schedules_dict)[0]) != set(
        ["larry", "jeff"]
    ):
        print("Error in Q4a - 1")
    if assess_office_hour(office_hour, student_schedules_dict)[1] != (2 / 3):
        print("Error in Q4a - 2")

    if merge_intervals([(-2, 43), (-700, -9), (20, 52), (52, 60)]) != [
        (-700, -9),
        (-2, 60),
    ]:
        print("Error in Q4b1 - 1")
    if merge_intervals([(-2, 43), (-700, -9)]) != [(-700, -9), (-2, 43)]:
        print("Error in Q4b1 - 2")
    if merge_intervals([(8, 10), (10, 12), (10, 11), (15, 18), (14, 16)]) != [
        (8, 12),
        (14, 18),
    ]:
        print("Error in Q4b1 - 3")

    if find_perfect_slots(student_schedules_dict) != [
        (7, 8),
        (12, 13),
        (13, 14),
        (18, 19),
        (19, 20),
    ]:
        print("Error Q4b2 - 1")


test()
