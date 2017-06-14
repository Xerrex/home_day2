def find_max_min(list):
    min_value=min(list)
    max_value=max(list)

    if min_value==max_value:
        return[len(list)]
    else:
        return [min_value, max_value]



