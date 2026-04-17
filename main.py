while True:
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))

    print("1: 더하기")
    print("2: 빼기")
    print("3: 곱하기")
    print("4: (두 수의 합) x 3")
    print("0: 종료")

    choice = input("원하는 연산 번호를 선택하세요: ")

    if choice == "1":
        print(f"결과: {num1 + num2}")
    elif choice == "2":
        print(f"결과: {num1 - num2}")
    elif choice == "3":
        print(f"결과: {num1 * num2}")
    elif choice == "4":
        print(f"결과: {(num1 + num2) * 3}")
    elif choice == "0":
        print("프로그램 종료")
        break
    else:
        print("잘못된 선택입니다.")