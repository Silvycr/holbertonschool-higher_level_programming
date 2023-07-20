#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    novo_list = []
    for z in range(list_length):
        var = 0
        try:
            quotient = my_list_1[z] / my_list_2[z]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            novo_list.append(var)
    return novo_list
