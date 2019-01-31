import re


def equals_a(string):
    return re.fullmatch(r'a', string)

def starts_with_a(string):
    return re.match(r'a', string)

def contains_a(string):
    return re.search(r'a', string)

def ends_with_a(string):
    return re.search(r'a$', string)

def contains_no_a(string):
    return re.fullmatch(r'[^a]*', string)

def does_not_start_with_a(string):
    return re.fullmatch('|[^a].*', string)

def does_not_end_with_a(string):
    return re.fullmatch('|.*[^a]', string)

def contains_three_as(string):
    return re.search('a.*a.*a', string)