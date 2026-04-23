from data_clean import *

def test_two_digits(a):
    if two_digits(a) is True:
        print("test passed")
    else: print("failed two")

def test_make_four(a):
    if make_four(a) == "1949":
        print("test_passed")
    else: print("failed four")

def test_faculty(a):
    if check_faculty(a) is True:
        print("test_passed")
    else: print("failed faculty")

def test_missing(a):
    if missing(a) is True:
        print("test_passed")
    else: print("failed missing")

def test_clutter(a):
    if remove_clutter(a) == "49":
        print("test_passed")
    else: print("failed clutter")

def test_extract(a):
    if extract_year(a) == "66":
        print("test_passed")
    else: print("failed extract")

def test_has_DOB(a):
    if has_DOB(a) is True:
        print("test_passed")
    else: print("failed has_DOB")


print(test_two_digits("49"))
print(test_make_four("49"))
print(test_faculty("49 Faculty"))
print(test_missing(""))
print(test_clutter("49?49"))

print(test_extract("1/25/66"))
print(test_has_DOB("DOB: 1/25/66"))

