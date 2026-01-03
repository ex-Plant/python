# Looking up items by key is O(1) - extremely fast!

def find_last_name(names_dict, first_name):  
    if first_name in names_dict:
        return names_dict[first_name] 
    return None

# Solution
# def find_last_name(names_dict, first_name):
#     try:
#         return names_dict[first_name]
#     except KeyError:
#         return None
