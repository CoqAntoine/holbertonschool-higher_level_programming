#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    liste_non_vue = []
    for i in set_1:
        if i not in set_2:
            liste_non_vue.append(i)
    for j in set_2:
        if j not in set_1:
            liste_non_vue.append(j)
    return liste_non_vue
