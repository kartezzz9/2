def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    number = int(input("Введите число для проверки: "))
    if is_prime(number):
        print(f"{number} - простое число.")
    else:
        print(f"{number} - составное число.")


if __name__ == "__main__":
    main()
