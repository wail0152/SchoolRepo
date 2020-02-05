def sortMethode(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[j] > lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
    return lst
