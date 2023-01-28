def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for idx in range(list_length):
        try:
            product = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            print("division by 0")
            product = 0
        except TypeError:
            print("wrong type")
            product = 0
        except IndexError:
            print("out of range")
            product = 0
        finally:
            n_list.append(product)
    return n_list
