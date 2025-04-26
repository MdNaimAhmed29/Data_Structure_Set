"""
Set{}
    -unordered
    -mutable
    -dynamic size
    -not allowed duplicates
    -heterogeneous
    -add()
    -update()
    -remove()
    -pop()
    -clear()
    -union()
    -intersection()
    -difference()
    -issubset()
    -issuperset()
"""

#sets

country = {"bangladesh", "pakistan", "china"}
city = {"manikganj", "rajshahi", "kushtia"}

res = country.union(city)
print(res)

res2 = country.intersection(city)
print(res2)

res3 = country.difference(city)
print(res3)

res4 = country.issubset(city)
print(res4)

res5 = country.issuperset(city)
print(res5)

country.add("America")
print(country)

country.update(["A", "B"])
print(country)

country.pop()
print(country)