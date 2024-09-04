#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            num1 = my_list_1[i]
            num2 = my_list_2[i]

            division_result = num1 / num2

            result.append(int(division_result) if division_result == 0 else division_result)
        except IndexError:
            print("out of range")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        finally:
            if len(result) > list_length:
                result = result[:list_length]
            while len(result) < list_length:
                result.append(0)

    return result
