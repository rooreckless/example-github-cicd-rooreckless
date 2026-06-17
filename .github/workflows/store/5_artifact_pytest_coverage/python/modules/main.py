def fizz_buzz(input_value):
    if not isinstance(input_value, int):
        return "unknown"
    elif input_value % 3 == 0 and input_value % 5 == 0:
        return "fizzbuzz"
    elif input_value % 3 == 0:
        return "fizz"
    elif input_value % 5 == 0:
        return "buzz"
    else:
        return "unknown"