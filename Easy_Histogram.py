"""help me 119"""
def main(text):
    """easy histogram no dict"""
    key_list = []
    value_list = []
    for i in text:
        if i in key_list:
            value_list[key_list.index(i)] += 1
        elif i == " ":
            continue
        else:
            key_list.append(i)
            value_list.append(1)
    add_key_value = zip(key_list,value_list)
    change = list(tuple(add_key_value))
    change_sort = sorted(change, key=lambda x: (x[0].lower(), x[0].isupper()))
    for i in change_sort:
        print(f"{i[0]} = {i[1]}")
main(input())
