#!/usr/bin/python3
def common_elements(set_1, set_2):
    liste_vue = []
    for i in set_1:
        for j in set_2:
            if i == j:
                liste_vue.append(i)
    return liste_vue
