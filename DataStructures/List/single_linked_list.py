def new_list():
    newlist = {
        'first': None,
        'last': None,
        'size': 0
    }
    return newlist

def get_elemet(my_list, pos):
    searchpos = 0
    node = my_list['first']
    while searchpos < pos:
        node = node['next']
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list['first']
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp['info']) == 0:
            is_in_array = True
        else:
            temp = temp['next']
            count += 1
    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    new_node = {'info': element, 'next': None}
    if my_list['first'] is None:
        my_list['first'] = new_node
        my_list['last'] = new_node
    else:
        new_node['next'] = my_list['first']
        my_list['first'] = new_node
    my_list['size'] += 1
    return my_list

def add_last(my_list, element):
    new_node = {'info': element, 'next': None}
    if my_list['first'] is None:
        my_list['first'] = new_node
        my_list['last'] = new_node
    else:
        my_list['last']['next'] = new_node
        my_list['last'] = new_node
    my_list['size'] += 1
    return my_list

def size(my_list):
    return my_list['size']

def first_element(my_list):
    return my_list['first']['info']

def delete_element(my_list, pos):
    if pos == 1:
        my_list['first'] = my_list['first']['next']
    else:
        searchpos = 0
        node = my_list['first']
        while searchpos < pos - 1:
            node = node['next']
            searchpos += 1
        node['next'] = node['next']['next']
    my_list['size'] -= 1

def change_info(my_list, pos, new_info):
    searchpos = 0
    node = my_list['first']
    while searchpos < pos:
        node = node['next']
        searchpos += 1
    node["info"] = new_info    

def exchange(my_list, pos1, pos2):
    searchpos = 0
    node1 = my_list['first']
    while searchpos < pos1:
        node1 = node1['next']
        searchpos += 1
    searchpos = 0
    node2 = my_list['first']
    while searchpos < pos2:
        node2 = node2['next']
        searchpos += 1
    temp_info = node1["info"]
    node1["info"] = node2["info"]
    node2["info"] = temp_info

def sub_list(my_list,pos_i,num_elem):
    sublist = new_list()
    searchpos = 0
    node = my_list['first']
    while searchpos < pos_i:
        node = node['next']
        searchpos += 1
    for i in range(num_elem):
        add_last(sublist, node["info"])
        node = node['next']
    return sublist