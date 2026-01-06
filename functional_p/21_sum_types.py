# Complete the get_csv_status function. It should use a match case statement to select the correct response depending on the status of the export operation. Create functions to handle each operation as follows:

# PENDING: return a tuple with the string "Pending..." and the data converted from a list of lists of anything, to a list of lists of strings.
# Try to use nested map functions to convert the data items into strings.
# Remember to convert from a map object back into a list.
# PROCESSING: return a tuple with the string "Processing..." and the data converted from a list of lists of strings into one string in CSV format.
# For each list of strings, combine the strings with join with commas in between to form a row.
# For each row string, combine the strings with join with newlines "\n" in between to form a table.
# SUCCESS: return a tuple with the string "Success!" and simply return the data as is.
# FAILURE: return a tuple with the string "Unknown error, retrying..." and the data after it has been prepared and processed into a CSV string, by combining the steps for Pending and Processing.
# Any Other Status: raise an Exception with the string "unknown export status".

from enum import Enum


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4

def handle_processing(data):
    joined = ''
    for row in data:
                joined += ",".join(row) + "\n"
    joined = joined[:-1]
    return joined

def handle_pending(data):
# I honestly hate this one liners syntax 😭
    table = list(map(lambda row: list(map(lambda nested: str(nested), row)) ,data))
    return  table
    

def get_csv_status(status, data):
    match(status):
        case CSVExportStatus.PENDING:            
            return ('Pending...', handle_pending(data))

        case CSVExportStatus.PROCESSING:
            return ('Processing...', handle_processing(data))
            
        case CSVExportStatus.SUCCESS:
            return ('Success!', data)

        case CSVExportStatus.FAILURE:
            return ('Unknown error, retrying...', handle_processing(handle_pending(data)))
        
        case _:
            raise Exception('unknown export status')
