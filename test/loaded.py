"""
@author: PGosavi

"""

import utils
import transformed
import pandas as pd

def loaded_data(): 
    
    transformed_path = "transformed"
    
    fpath = utils.open_path(transformed_path)
    
    most_recent_csv = utils.get_most_recent_csv(fpath)
    
    filename = most_recent_csv
    
    fname = utils.get_filename(filename, fpath)
    
    transformed_df = utils.read_csv_data(fname)
    
    loaded_df = transformed_df
    
    loaded_df ['Timestamp'] = utils.dt.datetime.now()
    
    l_r_count = utils.get_row_count(loaded_df)

    l_c_count = utils.get_column_count(loaded_df)

    l_collist = utils.get_columns_list(loaded_df)
    
    loaded_path = utils.create_path("loaded")
    
    loaded_dir = utils.create_dir(loaded_path)
    
    l_given_file_name = "Loaded_Data"
    
    l_file_name = utils.get_filename(l_given_file_name, loaded_path)
    
    utils.create_file(loaded_df, l_file_name, loaded_path)
    
    return loaded_df