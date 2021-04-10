# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

i=0
for S in sys.stdin:
    line = S.rstrip()
    if i!=0:    
        print(line[::2],line[1::2])
    i=i+1
