import sys

filename1 = sys.argv[1]
filename2 = sys.argv[2]

print(f"file1: {filename1}")
print(f"file2: {filename2}")

with open(filename1,'r') as f1:
    data = f1.read()
    
with open(filename2,'r') as f2:
    data2 = f2.read()

if data == data2:
    print("Same")
else:
    print("Different")
        
        