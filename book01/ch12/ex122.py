# 딕셔너리 요소 정렬하기
# sorted()

# key 정렬 ==> key list
d = {'Damon': 172, 'Stefan': 166, 'Alaric': 35, 'Klause': 1000}
r = sorted(d) # key를 오름차순으로 정렬하여 list로 리턴.
print(d)
print(r)

# key 정렬 ==> item list
d = {'Damon': 172, 'Stefan': 166, 'Alaric': 35, 'Klause': 1000}
r = sorted(d.items()) # key를 오름차순으로 정렬한 (k,v)를  list로 리턴.
print(d)
print(r)

# key 내림차순 정렬 ==> list
d = {'Damon': 172, 'Stefan': 166, 'Alaric': 35, 'Klause': 1000}
r = sorted(d.items(), reverse=True) # key를 내림차순으로 정렬하여 list로 리턴.
print(d)
print(r)

# 값으로 정렬
d = {'Damon': 172, 'Stefan': 166, 'Alaric': 35, 'Klause': 1000}
r = sorted(d.items(), key=lambda t: t[1])
print(r)


def determine_key(k_v):
    return k_v[1]

d = {'Damon': 172, 'Stefan': 166, 'Alaric': 35, 'Klause': 1000}
r = sorted(d.items(), key=determine_key)
print(r)

d = {'Damon': 172, 'Stefan': 166, 'Alaric': 35, 'Klause': 1000}
r = sorted(d.items(), key=lambda kv: kv[1])
print(r)

d = {'Damon': 172, 'Stefan': 166, 'Alaric': 35, 'Klause': 1000}
r = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
print(r)