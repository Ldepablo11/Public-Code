main = organize(data)

import os

example_class = main['DV Services 2021']['Professional Training']

print(example_class)

def save_dataframes_to_csv(data_dict, base_folder):

    if not os.path.exists(base_folder):
        os.makedirs(base_folder)
    
    # Iterate through each year in the dictionary
    for year, dfs_dict in data_dict.items():
        # Create a folder for the current year
        year_folder = os.path.join(base_folder, str(year))
        if not os.path.exists(year_folder):
            os.makedirs(year_folder)
        
        # Iterate through each DataFrame in the year's dictionary
        for df_name, df in dfs_dict.items():
            # Define the path for the CSV file
            csv_path = os.path.join(year_folder, f"{df_name}.csv")
            
            # Save the DataFrame to a CSV file
            df.to_csv(csv_path, index=False)

save_dataframes_to_csv(main, '/Users/libertodepablo/Desktop/Years')
