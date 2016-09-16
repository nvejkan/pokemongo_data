import pandas as pd

def get_df_powerup():
    df_powerup = pd.read_table('powerup_cost_raw.txt')
    
    return df_powerup[['level','stardust', 'candy']]
