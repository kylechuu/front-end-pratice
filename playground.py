from typing import DefaultDict


name = "enkai"
res = DefaultDict(int)

for i in range(len(name)):
    res[name[i]] += 1

print(res)