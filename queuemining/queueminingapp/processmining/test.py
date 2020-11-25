from pm4py.objects.log.importer.xes import importer as xes_importer
import pandas as pd
from pm4py.objects.log.util import dataframe_utils
from pm4py.objects.conversion.log import converter as log_converter
from pm4py.algo.filtering.log.timestamp import timestamp_filter



class FileNotCompatible(Exception):
    def __init__(self, file):
        self.file = file
        self.message = "The fileformat" + self.file  +"is not Compatible with our product"
        super().__init__(self.message)





def gettingLog(datapath, timestampcolumn):
    fileformat = datapath[-4:]
    if fileformat == '.xes':
        log = xes_importer.apply(datapath)
    elif fileformat == '.csv':
        log_csv = pd.read_csv(datapath, sep=',')
        log_csv = dataframe_utils.convert_timestamp_columns_in_df(log_csv)
        log_csv = log_csv.sort_values(timestampcolumn)
        log = log_converter.apply(log_csv)
    else:
        raise FileNotCompatible(fileformat)

    return log

def creatingTables(log):

    for trace in log:





