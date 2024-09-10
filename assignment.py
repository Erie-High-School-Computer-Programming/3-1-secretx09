#Chapter 3: Lists

def return_first_element(lst: list) -> str:
    """
    Returns the first element of the input list
    Remember that the first element is at index 0
    """
    return lst[0]


def return_last_element(lst: list) -> str:
    """
    Returns the last element of the input list
    """
    return lst[-1]

def add_element_to_a_string(lst: list) -> str:
    """
    Access the first element of the list and return it as in the sentence
    Modify the element so it is in title case.
    "The first element of the list is: <element>"
    """
    element = lst[0].title()
    return f"The first element of the list is: {element}"

def change_the_first_element(lst: list) -> list:
    """
    Change the first element of the list to "Python"
    """
    lst[0] = "Python"
    return lst

def change_the_last_element(lst: list) -> list:
    """
    Change the last element of the list to "Spam"
    """
    lst[-1] = "Spam"
    return lst

def add_element_to_the_end(lst: list) -> list:
    """
    Add the element "Eggs" to the end of the list
    """
    lst.append("Eggs")
    return lst

def add_element_to_the_beginning(lst: list) -> list:
    """
    Add the element "Eggs" to the beginning of the list
    """
    lst.insert(0, 0)
    lst.insert(0, "Eggs")
    return lst

def remove_last_element(lst: list) -> list:
    """
    Remove the last element of the list
    """
    lst.pop()
    return lst

def remove_first_element(lst: list) -> tuple[list, str]:    
    """
    Remove the first element of the list
    Store the value in a variable called "removed_element", and return it
    Be sure to return the list and the removed element separated by a comma
    Ex: return lst, removed_element
    """
    removed_element = lst[0]
    lst.pop(0)
    return lst, removed_element

def remove_element_at_index(lst: list, index: int) -> list:
    """
    Remove the element at the index provided as an argument
    """
    lst.pop(index)
    return lst

def insert_element_at_index(lst: list, index: int, element: str) -> list:
    """
    Insert the element at the index provided as an argument
    """
    lst.insert(2, element)
    return lst

def remove_element_by_value(lst: list, element: str) -> list:
    """
    Remove the element by value
    """
    lst.pop(2)
    return lst

def sort_list_alphabetically(lst: list) -> list:
    """
    Sort the list alphabetically
    """
    lst.sort()
    return lst

def reverse_list(lst: list) -> list:
    """
    Reverse the list
    """
    lst = lst[::-1]
    return lst
