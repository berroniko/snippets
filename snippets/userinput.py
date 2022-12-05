def input_float() -> float:
    """Request user to provide a number.

    Repeats the request until the user provides a number that can be converted to float.
    """
    n = None
    while True:
        n = input("Please provide a number!: ")
        try:
            n = float(n)
            break
        except ValueError:
            print("Only integers and floats are valid!\n")
    return n


r = input_float()

print(f"The number is: {r:.2f}")
