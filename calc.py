#!/usr/bin/python3
from functions import convert, getOperation, operators
print("Basic Calculator\n")

while True:
    q = input("press 'q' to quit or 'Enter' to continue: ")
    if q == 'q':
        print("Exiting...")
        break
    else:

        try:
            a, op, b = input("\nEnter your operation i.e (1 + 2):\n").split(" ")
        except ValueError:
            print("Inadequate operands")
            continue
        if a == 'q':
            print("Exiting...")
            break
        else:
            a = convert(a)
            if a is None:
                print("invalid operand!")
                continue
            else:
                # b = input("Enter num 2: ")
                if b == 'q':
                    print("Exiting...")
                    break
                else:
                    b = convert(b)
                    if b is None:
                        print("Invalid operand!")
                        continue
                    else:
                        if op in operators:
                            try:
                                result = getOperation(a, op, b)
                            except (TypeError, ZeroDivisionError):
                                print("Illigal Operation")
                            else:
                                print("\n{} {} {} = {:.1f}\n".format(a, op, b, result))
                        else:
                            print("Unkown operator!")