import pandas as pd
import numpy as np


def file_input(path):
    # TODO: Read other file types
    df = pd.read_csv(path)
    return df

def select(table,
           columnList):
    # TODO: Select any number of columns
    return newTable

def filterRows(table,
               columns,
               filter):
    newTable = table[columns] == filter
    return newTable

def join(table1,
         table2,
         index):
    newTable = table1.join(table2,
                           index)
    return newTable

def newColumn(table,
              columnName,
              calc):
    newTable = table[columnName] = calc
    return newTable

def sort(table,
         columnName):
    newTable = table.sort_values(by=columnName)
    return newTable

def replace(table,
            toReplace,
            values):
    newTable = table.replace(toReplace,
                             values)
    return newTable

class pipeStream:
    pipeInput = {} # A pipeInput is an ordered dictionary of order:input (can be a list)
    pipeMethod = {} # A pipeInput is an ordered dictionary of order:method
    # TODO: pipeInput validator against pipeMethod

def interpreter(pipeStream):

    for k, v in pipeStream.pipeInput.items():
        methodToCall = getattr(main, pipeStream.pipeMethod[k])(*pipeStream.pipeInput[k])

    # TODO: multiple simultaneous pipeStream input
