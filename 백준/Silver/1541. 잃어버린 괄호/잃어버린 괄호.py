n = input()
m = n.split("-")
ans = 0

x = sum(map(int, (m[0].split("+"))))
ans += x

for x in m[1:]:
    x = sum(map(int, (x.split('+'))))
    ans -= x

print(ans)
