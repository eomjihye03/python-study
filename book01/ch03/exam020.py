# match ~ case
#   match 서브젝트:
#       case 패턴:
#           문장
#       case 패턴:
#           문장
#       case _: 
#           문장

score = 'C'
match score:
    case 'A':
        print("Amazing!!")
    case 'B':
        print("Good job!!")
    case _: # wildcard
        print("Try harder...")

score = 'C'
match score:
    case 'A+' | 'A':
        print("Amazing!!")
    case 'B+' | 'B':
        print("Good job!!")
    case 'C+' | 'C' | 'D+' | 'D':
        print("Try harder...")
    case _: # wildcard
        print("Terrible")

# sequence pattern matching
data = [
    ('Damon', 172, False, (100, 100, 100), 300, 100.0),
    ('Elena', 20, False, (90, 90, 90)),
    ('Stefan', 166, True, (90, 90, 90, 90), 360, 90.0),
    ('Bonnie', (90, 90, 90), 270, 90.0),
]

for score in data:
    match score: # 데이터를 unpacking 하는 패턴을 지정.
        case [name, _, _, (kor, eng, math), sum, aver]: # sequence pattern
            print(f"{name:10} | {kor:>5} | {eng:>5} | {math:>5} | {sum:>5} | {aver:>5.1f}")
        case [name, _, _, (kor, eng, math)]:
            print(f"{name:10} | {kor:>5} | {eng:>5} | {math:>5} | {kor+eng+math:>5} | {(kor+eng+math)/3:>5.1f}")
        case [name, _, _, (kor, eng, math, _), _, _]:
            print(f"{name:10} | {kor:>5} | {eng:>5} | {math:>5} | {kor+eng+math:>5} | {(kor+eng+math)/3:>5.1f}")
        case [name, (kor, eng, math), sum, aver]:
            print(f"{name:10} | {kor:>5} | {eng:>5} | {math:>5} | {sum:>5} | {aver:>5.1f}")

