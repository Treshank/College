for i in range(1, 50):
    k = "fizz" if i % 3 == 0 else "buzz" if i % 5 == 0 else "fizzbuzz" if i % 15 == 0 else i
    print(k)

