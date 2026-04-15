name = input("이름: ")
hours = float(input("근무 시간: "))
rate = float(input("시급: "))   
salary = hours * rate
print("이름:", name)
print("급여:", salary)
# 세금 15% 계산
tax = salary * 0.15
net_salary = salary - tax
print("세금:", tax)
print("실수령액:", net_salary)
