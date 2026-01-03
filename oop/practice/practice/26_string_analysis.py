# Fix Inventory Summary (Simulated File Read)
# The summarize_inventory function is supposed to read inventory data from a string (pretend it’s the contents of a file) and return a summary dictionary of total quantities per item.
#
# Because we run in a sandbox, you won’t open real files. Instead, the entire file content is provided as a single string input. Your job is to parse it correctly.
#
# Rules for parsing:
#
# Process the input by lines (like reading a file). Use str.splitlines() which handles both "\n" and Windows "\r\n" newlines.
# Ignore empty lines.
# Ignore full-line comments that start with #.
# Support inline comments: anything after a # on a data line should be ignored.
# Each valid data line (after removing comments) must be in the format: name,quantity
# Trim whitespace around both name and quantity.
# Convert name to lowercase.
# quantity must be an integer (like 10, -2, 0). If it’s not a valid integer, skip the line entirely.
# If the name is empty after trimming, skip the line.
# Sum quantities across multiple lines for the same item.
# Return a dictionary mapping item names (lowercase strings) to their total quantity (int).
#
# Inline # comments are not handled.
# Extra whitespace isn’t trimmed.
# Item names aren’t normalized to lowercase.
# Quantities that aren’t valid integers shouldn’t be counted.
# Lines with the wrong format (missing comma or too many commas) should be skipped.
# Duplicate items should have their quantities added together, not overwritten.

# ✅ Solution
def summarize_inventory(file_text):
    totals = {}
    for line in file_text.splitlines():
        if not line:
            continue

        if line.startswith("#"):
            continue

        parts = line.split(",")
        if len(parts) != 2:
            continue

        name = parts[0].strip().lower()
        if not name:
            continue

        qty = parts[1]
        if '#' in qty:
            qty = qty.split('#')
            qty = qty[0].strip()

        try:
            quantity = int(qty)
        except Exception:
            continue

        if name in totals:
            totals[name] = quantity + totals[name]
        else:
            totals[name] = quantity
    return totals
