def display_sublist(lst):
    l = len(lst)
    sublists = [[]]

    for i in range(l-1):
        for j in range(i+1, l+1):
            sublists.append(lst[i:j])
    return sublists

print(display_sublist(["a", "b", "c"]))