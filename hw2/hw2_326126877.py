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
    rand = random.random()
    value = v[0]
    for i in range(1, len(p)):
        p[i] = p[i] + p[i - 1]
        if rand > p[i - 1] and rand <= p[i]:
            value = v[i]
            break
    return value

# Q2c
def monty_hall(switch, times):
    counter = 0
    for t in range(times):
        doors = [False, False, False]  # false is rock, true if car
        car_door = random.randint(0, 2)  # the presentor's choise
        for i in range(len(doors)):
            if i == car_door:
                doors[i] = True
                break

        first_choice = random.randint(0, 2)  # player's first choice
        if not switch and first_choice == car_door:
            counter += 1
        # no need to write any code for the opening of the rock door.
        # assuming player wants to win, he will switch to the other closed door.
        # meaning we can use !first_choice as an expression for the second unopened door.
        elif switch and first_choice != car_door:
            counter += 1

    return counter / times

# Q2d
def sample_anagram(st):
    chars = list(st)
    anagram = ""
    for ch in st:
        char = chars[random.randint(0, len(chars) - 1)]
        anagram += char
        chars.remove(char)
    return anagram

##############
# QUESTION 3 #
##############
# Q3a
def inc(binary):
    binary = "0" + binary
    binary = list(binary)
    for i in range(len(binary), 0, -1):
        if binary[i - 1] == "0":
            binary[i - 1] = "1"
            break
        else:
            binary[i - 1] = "0"
    if binary[0] == "0":
        return "".join(binary[1:])
    return "".join(binary)

# Q3b
def add(bin1, bin2):
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)
    result = []
    carry = "0"
    for i in range(max_len - 1, -1, -1):
        if bin1[i] == "0" and bin2[i] == "0":
            result.append(carry)
            carry = "0"
        elif bin1[i] == "1" and bin2[i] == "1":
            result.append(carry)
            carry = "1"
        else:
            result.append("1" if carry == "0" else "0")
    if carry == "1":
        result.append("1")
    return "".join(reversed(result)).lstrip("0") or "0"

# Q3c
def mod_two(binary, power):
    if power <= 0:
        return binary
    if len(binary) <= power:
        return binary
    return binary[-power:].lstrip("0")

# Q3d
def max_bin(lst):
    return max(lst, key=lambda x: (len(x), x))


##############
# QUESTION 4 #
##############

# Q4a1
def is_student_available(office_hour, student_schedule):
    for period in student_schedule:
        if office_hour[0] < period[1] and office_hour[1] > period[0]:
            return False
    return True


# Q4a2
def assess_office_hour(office_hour, student_schedules_dict):
    available_students = []
    for student, schedule in student_schedules_dict.items():
        if is_student_available(office_hour, schedule):
            available_students.append(student)
    return (available_students, len(available_students) / len(student_schedules_dict))

# Q4b1
def merge_intervals(intervals):
    # sort intervals by start time
    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            if intervals[i][0] > intervals[j][0]:
                intervals[i], intervals[j] = intervals[j], intervals[i]

    merged = [intervals[0]]
    # merge overlapping intervals
    for i in range(len(intervals)):
        if intervals[i][0] <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], intervals[i][1]))
        else:
            merged.append(intervals[i])
    return merged

# Q4b2
def find_perfect_slots(student_schedules_dict):
    merged_schedules = []
    # concentrating all schedules into one list
    for schedule in student_schedules_dict.values():
        merged_schedules = [*merged_schedules, *schedule]

    # merging all schedules into one list of merged intervals
    merged_schedules = merge_intervals(merged_schedules)
    perfect_slots = []
    curr_hour = 7

    # finding perfect slots between merged intervals
    for i in range(len(merged_schedules)):
        while curr_hour <= merged_schedules[i][0] - 1:
            perfect_slots.append((curr_hour, curr_hour + 1))
            curr_hour += 1
        curr_hour = merged_schedules[i][1]

    # filling in the remaining slots till 8pm
    while curr_hour <= 19:
        perfect_slots.append((curr_hour, curr_hour + 1))
        curr_hour += 1

    return perfect_slots


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
        print("sampled_elem: ", sampled_elem)
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
