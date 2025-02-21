def fib(max_count):
    a, b = 0, 1
    for _ in range(max_count):
        a, b = b, a + b
        yield a


def test_fib():
    gen_obj = fib(20)
    for value in gen_obj:
        print(value)


def calc_average():
    total, counter = 0, 0
    avg_value = None
    while True:
        curr_value = yield avg_value
        total += curr_value
        counter += 1
        avg_value = total / counter


def main():
    obj = calc_average()
    # 生成器预激活
    first = obj.send(None)
    print(f"init: {first}")
    for _ in range(5):
        print("input:")
        res = obj.send(float(input()))
        print(f"output: {res}")


if __name__ == "__main__":
    main()
