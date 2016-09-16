import pandas as pd
from pandasql import sqldf
def get_df_cpup():
    df = pd.read_csv('cp_per_powerup_raw.csv')
    return df

def get_df_powerup():
    df_powerup = pd.read_table('powerup_cost_raw.txt')
    
    return df_powerup[['level','stardust', 'candy']]

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

def get_df_spawn():
    df = pd.read_csv('spawn_rate_raw.csv')
    return df

df_cp = get_df_cpup()
#df_cost = get_df_powerup()
df_cost = pd.read_csv('level_candy.csv')
df_candy_km = get_df_candy_km()
df_spawn = get_df_spawn()
df_pokemon =  pd.read_csv('pokemon_evolve_raw.csv')

q = """
select df_cp.name
,candy*km,max_level
,cp_per_powerup
,1.0*cp_per_powerup/(candy*km) as cp_per_km
,df_spawn.avg_per_10000
,(1.0*cp_per_powerup/(candy*km))/df_spawn.avg_per_10000 as score
from df_spawn
,df_candy_km
,df_cost
,df_cp
where df_cp.name = df_candy_km.name
and df_cp.name = upper(df_spawn.pokemon)
"""

ret = sqldf(q, locals())
#ret['minus_spawn'] = -1* ret['avg_per_10000']
#ret['cp_per_km*spawn'] = ret['cp_per_km']* ret['minus_spawn']
#ret['cp_per_km_spawn'] = 1.0*ret['cp_per_km']/ret['avg_per_10000']

q = """
select ret.*
,df_pokemon.*
from ret
left outer join df_pokemon on upper(df_pokemon.name) = ret.name
"""
ret2 = sqldf(q, locals())

ret.to_csv('ret.csv',index=False)
ret2.to_csv('ret2.csv',index=False)
