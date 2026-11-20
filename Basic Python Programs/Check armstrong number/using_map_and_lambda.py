n = 153
p = len(str(n))
s = sum(map(lambda d: int(d) ** p, str(n)))
if s == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
    