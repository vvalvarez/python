print('1234567890'[1:6])  # 2345
print('1234567890'[:3])  # 123
print('1234567890'[::-2])  # 08642
print('1234567890'[-3:])  # 890
print('1234567890'[-1:])  # 0
print('1234567890'[1:3])  # 23

pv=2000
fv='4,152.32'
r=11
n=5
answer=f"If we had bought ${pv} crypto coins at the weekend, we would have had ${fv} with a profit share of {r}% after {n} days"
print(answer)


txt = "If we had bought ${pv1} crypto coins at the weekend, we would have had ${fv1} with a profit share of {r1}% after {n1} days."
print(txt.format(pv1 = 2000, fv1 = '4,152.32', r1 = 11, n1 = 5))