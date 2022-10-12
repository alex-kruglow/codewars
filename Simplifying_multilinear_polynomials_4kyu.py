#!/usr/bin/env python3

##########################################################
# https://www.codewars.com/kata/55f89832ac9a66518f000118 #
##########################################################

def len_alpha(s: str) -> int:
    '''Return value how many alpha symbols is contained in the string.'''
    return len([c for c in s if c.isalpha()])


def get_alpha_only(s: str) -> str:
    '''Return only alpha symbols.'''
    return ''.join([c for c in s if c.isalpha()])


def sort_items_by_len_and_abc(list_to_sort: list) -> list:
    '''Return sorted list by item length and abc if len is equal.'''
    flag: bool = True
    l_t_s = list_to_sort.copy()
    while flag:
        flag = False
        for i in range(len(list_to_sort) - 1):
            j = i + 1
            len_i: int = len_alpha(l_t_s[i])
            len_j: int = len_alpha(l_t_s[j])
            if len_i > len_j:
                l_t_s[i], l_t_s[j] = l_t_s[j], l_t_s[i]
                flag = True
            len_is_equal: bool = len_i == len_j
            alpha_only_i: str = get_alpha_only(l_t_s[i])
            alpha_only_j: str = get_alpha_only(l_t_s[j])
            abc_incorrect = alpha_only_i > alpha_only_j
            if len_is_equal and abc_incorrect:
                l_t_s[i], l_t_s[j] = l_t_s[j], l_t_s[i]
                flag = True
    return l_t_s


def simplify(poly: str) -> str:
    '''Return the simplified formula.'''
    formula_list: list = []
    part: str = ''
    for c in poly:
        if c in '+-':
            if part:
                formula_list.append(part)
            part = c
        else:
            part = f'{part}{c}'
    if part:
        formula_list.append(part)
    formula_dict: dict = {}
    for item in formula_list:
        sign: int = 1
        dig: int = 0
        dig_str: str = ''
        variables: str = ''
        for c in item:
            if c in '+-':
                if c == '+':
                    sign = 1
                else:
                    sign = -1
            if c.isdigit():
                dig_str = f'{dig_str}{c}'
            if c.isalpha():
                variables = f'{variables}{c}'
        if not dig_str:
            dig_str = '1'
        dig = sign * int(dig_str)

        index = ''.join(sorted(variables))
        if index in formula_dict:
            formula_dict[index] += dig
        else:
            formula_dict[index] = dig
    formula_list = []
    for formula_item_key, formula_item_val in formula_dict.items():
        if formula_item_val:
            if formula_item_val == 1:
                formula_list.append(f'+{formula_item_key}')
            elif formula_item_val == -1:
                formula_list.append(f'-{formula_item_key}')
            elif formula_item_val > 1:
                formula_list.append(f'+{formula_item_val}{formula_item_key}')
            else:
                formula_list.append(f'{formula_item_val}{formula_item_key}')
    formula_list = sort_items_by_len_and_abc(formula_list)
    formula_str: str = ''.join(formula_list)
    return formula_str if formula_str[0] == '-' else formula_str[1:]


def main():
    print("Test reduction by equivalence")
    assert simplify("dc+dcba") == "cd+abcd"

    assert simplify("2xy-yx") == "xy"

    assert simplify("-a+5ab+3a-c-2a") == "-c+5ab"

    print("Test monomial length ordering")
    assert simplify("-abc+3a+2ac") == "3a+2ac-abc"

    assert simplify("xyz-xz") == "-xz+xyz"

    print("Test lexicographic ordering")
    assert simplify("a+ca-ab") == "a-ab+ac"

    assert simplify("xzy+zby") == "byz+xyz"

    print("Test no leading +")
    assert simplify("-y+x") == "x-y"

    assert simplify("y-x") == "-x+y"


if __name__ == '__main__':
    main()
