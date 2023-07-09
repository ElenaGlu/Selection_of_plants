# ATT
def some_func(a: int, some_dict: dict) -> dict:
    """
    Deletes 3 key from dict
    :param a: key
    :param some_dict: some dict filled with flowers. Example {"rose": "lala", }
    :return: same dict without key.
    """
    if a == 3:
        some_dict.pop(a)
    return some_dict
