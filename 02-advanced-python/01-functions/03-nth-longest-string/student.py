# Write your code here
def nth_longest_string(n,strings):
    list = sorted(strings,key = len)
    return list[-n]
