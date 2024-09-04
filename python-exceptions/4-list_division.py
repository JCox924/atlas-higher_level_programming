#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            num1 = my_list_1[i]
            num2 = my_list_2[i]

            result.append(num1 / num2)
        except IndexError:
            # Handle the case where lists are too short
            print("out of range")
            result.append(0)
        except ZeroDivisionError:
            # Handle division by zero
            print("division by 0")
            result.append(0)
        except TypeError:
            # Handle incorrect types
            print("wrong type")
            result.append(0)

            # Ensure result list is exactly the required length
        if len(result) > list_length:
            result = result[:list_length]
        while len(result) < list_length:
            result.append(0)

        print(result)
        return result
