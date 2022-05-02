# Write your code here
def countdown(n):
    string = []
    for i in range(n):
        string.append(f"{n-i}")
    str = ", ".join(string)
    return str


