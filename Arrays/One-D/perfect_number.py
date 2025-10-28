def checkPerfectNumber(num: int) -> bool:
    if num <= 0:
        return False
    else:
        sum = 0

        for i in range(1, num):
            if num % i == 0:
                sum += i

        return sum == num


print(checkPerfectNumber(28))
print(checkPerfectNumber(7))
