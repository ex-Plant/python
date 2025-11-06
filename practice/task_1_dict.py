# Aggregate Warehouse Inventory
# Complete the function aggregate_inventory(warehouses).
#
# You’re given inventory data from multiple warehouses. Each warehouse maps item names to quantities. Your job is to combine them into a single inventory summary.
#
# Rules:
#
# Combine quantities for the same item across all warehouses.
# Item names are case-insensitive. For example, "Apple" and "apple" should be treated as the same item. Normalize item names to lowercase.
# If an item’s total quantity is less than or equal to 0 after combining, do not include it in the result.
# Return a dictionary that maps normalized item names (lowercase) to their total positive quantities.
# Notes:
#
# Use basic dictionary operations and loops.
# You can use str.lower() to normalize names to lowercase.

def aggregate_inventory(warehouses):
    total = {}
    for items in warehouses:
        for item in warehouses[items]:
            if not item.lower() in total:
                total[item.lower()] = warehouses[items][item]
            else:
                total[item.lower()] = warehouses[items][item] + total[item.lower()]

    result = {}
    for val in total:
        if total[val] > 0:
             result[val] = total[val]
    return result
