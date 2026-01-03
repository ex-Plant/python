# Fix the sort_dates function. It takes as input a list of dates in "MONTH-DAY-YEAR" format and returns a list of the dates sorted in ascending order.

# Tips
# The built-in sorted function might work better here than the .sort() list method. Create a function to transform the dates to make them easier to compare with the sorted function.

# Pay attention to the expected date order. Is it ordered by day, month, or year?

# The sorted function accepts a second optional parameter. This parameter is a function that will be called on each iteration.


def transform_date(str):
    strArr=str.split("-")
    return strArr[2] + strArr[0] + strArr[1]
    

def sort_dates(dates):
    sr = sorted(dates, key=transform_date )
    return sr
