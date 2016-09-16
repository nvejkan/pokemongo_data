import pandas as pd

def get_df_candy_km():
    infile = open('candy_km_raw.txt','r')
    name = []
    km = []
    size = []
    for i in infile:
        splited = i.strip().upper().split('\t')
        #print(splited)
        name.append(splited[0])
        km.append(splited[1])
        size.append(splited[2])

    dict_to_df = { 'name':name
                   ,'km':km
                   ,'size':size
                }
    df_candy_km = pd.DataFrame(dict_to_df)
    return df_candy_km
