def new_list():
    newlist = {
        'elements': [], 
        'size': 0
    }
    return newlist

def get_element(my_list, index):
    # Convert 1-based index to 0-based for underlying Python list
    return my_list['elements'][index - 1]

def is_present(my_list, element, cmp_function):
    size = my_list['size']
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list['elements'][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            # Return 1-based position to match the rest of the codebase
            return keypos + 1
    return -1

def add_first(my_list, element):
    my_list['elements'].insert(0, element)
    my_list['size'] += 1
    return my_list

def add_last(my_list, element):
    my_list['elements'].append(element)
    my_list['size'] += 1
    return my_list

def size(my_list):
    return my_list['size']

def first_element(my_list):
    return my_list['elements'][0]

def is_empty(my_list):
    return my_list['size'] == 0

def get_last_element(my_list):
    return my_list['elements'][-1]

def get_element(my_list, index):
    return my_list['elements'][index - 1]

def remove_first(my_list):
    if my_list['size'] > 0:
        removed_element = my_list['elements'].pop(0)
        my_list['size'] -= 1
        return removed_element
    else:
        raise IndexError("List is empty")

def remove_last(my_list):
    if my_list['size'] > 0:
        removed_element = my_list['elements'].pop()
        my_list['size'] -= 1
        return removed_element
    else:
        raise IndexError("List is empty")

def insert_element(my_list, element, index):
    if index < 1 or index > my_list['size'] + 1:
        raise IndexError("Index out of bounds")
    my_list['elements'].insert(index - 1, element)
    my_list['size'] += 1
    return my_list


