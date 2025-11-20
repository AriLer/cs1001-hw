
# ?-- Question 4.a ---? #
def union_strings(st1, st2):
    st_comb = ""
    for ch in st1:
        if st_comb.find(ch) == -1:
            st_comb += ch
    for ch in st2:
        if st_comb.find(ch) == -1:
            st_comb += ch
    return st_comb

# ?-- Question 4.b ---? #
def format_str(text_to_format, st_to_insert):
    formated_string = ""
    for ch in text_to_format:
        val = st_to_insert if ch == "?" else ch
        formated_string += val
    return formated_string

# ?-- Question 4.c ---? #
def least_pal(text):
    count = 0
    # it's wasteful to go over the entire string because all the chars at the back end of the string will be checked already
    # if the string is of even length the for loop will cover over all the characters
    # if the string is of odd length the middle character can never ruin a palindrome
    for i in range(len(text) // 2):
        if text[i] != text[-(i + 1)]:
            count += 1
    return count

# ?-- Question 4.d ---? #
def least_frequent(text):
    if len(text) != 0:
        counter = {}
        # add up the occurances of characters in a dictionary
        for char in text:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
        # find the lowest number of occurances
        least_char = text[0]
        least_count = counter[least_char]
        for key, value in counter.items():
            if value < least_count:
                least_char = key
                least_count = value
        return least_char
    else:
        return "string is empty"

# ?-- Question 4.e ---? #
def longest_common_suffix(lst): 
    suffix = lst[0]; 
    for i in range(1, len(lst[0])+1):
        char = lst[0][-i] # counting from the end of the string.
        for str in lst:
            if i > len(str) or char != str[-i]:
                if i == 1: return ""
                return suffix[-i+1:]            
    return suffix

# ?-- Question 4.f ---? #
def is_int(text):
    if not text:
        return False

    digits = text 
    if text[0] == '-':
        if len(text) == 1 or text == "-0": # the string excplisitly cannot be "-" or "-0"
            return False
        digits = text[1:]

    if len(digits) > 1 and digits[0] == "0":
        return False

    for ch in digits:
        if ch < "0" or ch > "9":
            return False
    return True

# ? --- Question 4g (optional) ---? # 
def merge(text1, text2):
    print("optional merge not implemented")
    pass


# ?-- Question 5.a ---? #
def is_anagram(st1, st2):
    char_counter1 = {}
    char_counter2 = {}
    
    # add up the occurances of characters in dictionaries
    if(len(st1) != len(st2)):
        return False
    
    for i in range(len(st1)):
        if st1[i] in char_counter1:
            char_counter1[st1[i]] += 1
        else:
            char_counter1[st1[i]] = 1
            
        if st2[i] in char_counter2:
            char_counter2[st2[i]] += 1
        else:
            char_counter2[st2[i]] = 1
    
    
    for key in char_counter1.keys():
        if key not in char_counter2 or char_counter1[key] != char_counter2[key]:
            return False;
    return True

def is_anagram_v2(st1, st2):
    for ch in st1:
        if st1.count(ch)!= st2.count(ch):
            return False
    return True

# ?-- Question 5.c ---? #
def is_anagram_v3(st1, st2):
 return sorted(st1) == sorted(st2)

# ?-- Question 6.a ---? #
def eval_mon(monomial, val):
    coefficient = int(monomial.split("x^")[0])
    exponent = int(monomial.split("x^")[1])
    
    product = coefficient * val**exponent;
    return product

# ?-- Question 6.b ---? #
def eval_pol(polynomial, val):
    # we define a start a starting point and 
    # only when we reach another + / - sign or it's the end of the string, do we know we isolated a single monomial 
    # then we call the monomial and add the value to the sum 
    parts = []
    start = 0
    sum = 0 
    for i in range(len(polynomial)):
        if polynomial[i] == '+' or polynomial[i] == '-':
            part = polynomial[start:i]
            parts.append(part)
            if(part != ""):
                sum += eval_mon(part, val)    
            start = i
    sum += eval_mon(polynomial[start:], val) 
    return sum
    
def test():
    # Testing Q4
    if "".join(sorted(union_strings("aabcccdde", "bccay"))) != "abcdey":
        print("error in union_strings - 1")
    if "".join(sorted(union_strings("aabcccdde", ""))) != "abcde":
        print("error in union_strings - 2")

    if format_str("I2?", "CS") != "I2CS":
        print("error in format_str - 1")
    if format_str("???", "W") != "WWW":
        print("error in format_str - 2")
    if format_str("ABBC", "z") != "ABBC":
        print("error in format_str - 3")

    if least_pal("abcdefgh") != 4:
        print("error in least_pal - 1")
    if least_pal("radarr") != 2:
        print("error in least_pal - 2")
    if least_pal('race car') != 1:
        print("error in least_pal - 3")
    if least_pal('tenat') != 1:
        print("error in least_pal - 4")

    if least_frequent('aabcc') != 'b':
        print("error in least_frequent - 1")
    if least_frequent('aea.. e') != ' ':
        print("error in least_frequent - 2")
    if least_frequent('zzz') != 'z':
        print("error in least_frequent - 3")

    if longest_common_suffix(["abccdba", "cba", "zaba"]) != "ba":
        print("error in longest_common_suffix - 1")
    if longest_common_suffix(["hello", "world"]) != "":
        print("error in longest_common_suffix - 2")
    if longest_common_suffix(["intro", "maestro"]) != "tro":
        print("error in longest_common_suffix - 3")
    if longest_common_suffix(["intro"]) != "intro":
        print("error in longest_common_suffix - 4")

    if is_int("12x"):
        print("error in is_int - 1")
    if is_int("-0"):
        print("error in is_int - 2")
    if not is_int("42"):
        print("error in is_int - 3")

    if merge("abcd", "") != "abcd":
        print("error in merge - 1")
    if merge("aabbddfgk", "adkox") != "aaabbdddfgkkox":
        print("error in merge - 2")

    # Testing Q5
    if not is_anagram("tommarvoloriddle", "iamlordvoldemort"):
        print("error in is_anagram - 1")
    if is_anagram("abce", "abcd"):
        print("error in is_anagram - 2")
    if not is_anagram("listen", "silent"):
        print("error in is_anagram - 3")

    if not is_anagram_v2("tommarvoloriddle", "iamlordvoldemort"):
        print("error in is_anagram_v2 - 1")
    if is_anagram_v2("abce", "abcd"):
        print("error in is_anagram_v2 - 2")
    if not is_anagram_v2("listen", "silent"):
        print("error in is_anagram_v2 - 3")

    if not is_anagram_v3("tommarvoloriddle", "iamlordvoldemort"):
        print("error in is_anagram_v3 - 1")
    if is_anagram_v3("abce", "abcd"):
        print("error in is_anagram_v3 - 2")
    if not is_anagram_v3("listen", "silent"):
        print("error in is_anagram_v3 - 3")

    # Testing Q6
    if eval_mon("+5x^3", 4) != 320:
        print("error in eval_mon - 1")
    if eval_mon("-5x^0", 1000) != -5:
        print("error in eval_mon - 2")
    if eval_mon("+1x^10", 2) != 1024:
        print("error in eval_mon - 3")

    if eval_pol("+5x^3-4x^2+7x^1-5x^0+10x^11", 4) != 41943319:
        print("error in eval_pol - 1")
    if eval_pol("+1x^0+1x^1+1x^2+1x^3+1x^4+1x^5", 5) != 3906:
        print("error in eval_pol - 2")
    if eval_pol("+11x^0+1x^1+1x^2+1x^3+1x^4+1x^5", 2) != 73:
        print("error in eval_pol - 3")

    print("`test()` completed.")

test()