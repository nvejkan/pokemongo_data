import pandas as pd

def get_df_cpup():
    df = pd.read_csv('cp_per_powerup_raw.csv')
    return df
    
