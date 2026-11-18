p = 1200
r = 5.4
t = 2
Amt = p
for i in range(t):
    Amt = Amt * (1+r/100)
CI = Amt-p
print("Compound interest: ", CI)