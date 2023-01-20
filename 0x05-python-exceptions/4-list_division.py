#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    listf = []
    for i in range(list_length):
        try:
            listf.append(float(my_list_1[i] / my_list_2[i]))
        except TypeError:
            print("wrong type")
            listf.append(0)
            pass
        except ValueError:
            print("wrong type")
            listf.append(0)
            pass
        except ZeroDivisionError:
            print("division by 0")
            listf.append(0)
            pass
        except IndexError:
            print("out of range")
            listf.append(0)
            pass
        finally:
            pass
    return listf
