"""
@author: PGosavi

"""

import utils

def extracted_data():
    
    source_path = "source"
    
    fpath = utils.open_path(source_path)
    
    most_recent_csv = utils.get_most_recent_csv(fpath)
    
    filename = most_recent_csv
    
    fname = utils.get_filename(filename, fpath)
    
    raw_df = utils.read_csv_data(fname)
    
    desired_col_list = ['ID', 'Name', 'Age', 'Nationality', 'Joined', 'Weight']
    
    extracted_df = raw_df[desired_col_list]
    
    e_r_count = utils.get_row_count(extracted_df)

    e_c_count = utils.get_column_count(extracted_df)

    e_collist = utils.get_columns_list(extracted_df)
    
    extracted_path = utils.create_path("extracted")
    
    extracted_dir = utils.create_dir(extracted_path)
    
    e_given_file_name = "Extracted_Data"
    
    e_file_name = utils.get_filename(e_given_file_name, extracted_path)
    
    utils.create_file(extracted_df, e_file_name, extracted_path)
    
    return extracted_df
