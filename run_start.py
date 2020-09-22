import pandas as pd, requests, sys, time

from pprint import pprint as pp
from tqdm import tqdm

base_url = 'https://api.collegefootballdata.com/{}'

games_df = pd.read_csv('games.csv')

plays = []

for index, row in tqdm(games_df.iterrows()):
    r = requests.get(base_url.format('play/stats')
                     ,params = {'gameId':row.id}
                     )

    plays.append(pd.DataFrame(r.json()))
    time.sleep(1)
    print()

df = plays.pop(0)
for p in plays:
    df = df.append(p)

