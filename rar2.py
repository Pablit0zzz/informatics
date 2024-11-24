def clear_number(s):
    return "".join(list(map(lambda x: x if x.isdigit() else "", s)))
print(clear_number("+7 (123) 456-78-90"))
