"""
@author: PGosavi

"""

def main ():
    
    print("\n------------------ Operation Start ------------------\n")
    
    import extracted
    
    extracted.extracted_data()
    
    import transformed
    
    transformed.transformed_data()

    import loaded
    
    loaded.loaded_data()

    print("\n------------------ Operation End ------------------\n")

if __name__ == '__main__':
    main()
    