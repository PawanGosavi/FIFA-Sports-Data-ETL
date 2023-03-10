"""
@author: PGosavi

"""

import utils
import extracted
import pandas as pd

def transformed_data():
       
    extracted_path = "extracted"
    
    fpath = utils.open_path(extracted_path)
    
    most_recent_csv = utils.get_most_recent_csv(fpath)
    
    filename = most_recent_csv
    
    fname = utils.get_filename(filename, fpath)
    
    extracted_df = utils.read_csv_data(fname)
        
    # extracted_df = extracted_df.dropna(inplace = True)
    
    trans_df = pd.DataFrame()
    
    trans_df['ID'] = extracted_df['ID'].astype('str').str.strip().fillna(0).astype('int')
    trans_df['Name'] = extracted_df['Name'].astype('str').str.strip().fillna("UNK").astype('str')
    trans_df['Age'] = extracted_df['Age'].astype('str').str.strip().fillna(0).astype('int')
    trans_df['Nationality'] = extracted_df['Nationality'].astype('str').str.strip().fillna("UNK").astype('str')
    trans_df['Joined'] = pd.to_datetime(extracted_df['Joined']).fillna(pd.to_datetime('2000-01-01')).astype('datetime64[ns]')
    trans_df['Weight_lbs'] = extracted_df['Weight'].astype('str').str.strip().str.rstrip('lbs').fillna(0).replace("nan", 0).astype('int')
    
    filt_df = trans_df[(trans_df['Age'] >= 18) & (trans_df['Nationality'] == "England") & (trans_df['Weight_lbs'] < 150)]
    
    ord_df = filt_df.sort_values(by=['Weight_lbs', 'Age'], ascending = False)
    
    transformed_df = ord_df
    
    t_r_count = utils.get_row_count(transformed_df)

    t_c_count = utils.get_column_count(transformed_df)

    t_collist = utils.get_columns_list(transformed_df)
    
    transformed_path = utils.create_path("transformed")
    
    transformed_dir = utils.create_dir(transformed_path)
    
    t_given_file_name = "Transformed_Data"
    
    t_file_name = utils.get_filename(t_given_file_name, transformed_path)
    
    utils.create_file(transformed_df, t_file_name, transformed_path)
    
    return transformed_df
