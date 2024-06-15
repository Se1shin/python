def some(Test: bool = True):  # Здесь нет перегрузок методов(
    smth_list = []
    if Test:
        return smth_list  # return list
    else:
        return  # return None