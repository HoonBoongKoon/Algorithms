a = input()

one = [ '','I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
ten = [ '','X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC' ]

a = sorted(a.rstrip())

for i in range(1,100):
    ans = ten[i//10] + one[i%10]
    if a == sorted(ans):
        print(ans)
        break