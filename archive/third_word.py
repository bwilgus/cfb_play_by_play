import requests

from pprint import pprint as pp

base_url = 'https://api.collegefootballdata.com/{}'

play_types = {}
stat_types = {}
third_word = []

r = requests.get(base_url.format('play/types'))
for row in r.json():
    play_types[row['id']] = row['text']


r = requests.get(base_url.format('play/stat/types'))
for row in r.json():
    stat_types[row['id']] = row['name']

params = {'year': '2019', 'week': '1'}

while True:
    print(params['week'])
    r = requests.get(base_url.format('plays'),params=params)
    if len(r.json()) == 0:
        break
    

    for p in r.json():
        if len(p['play_text'].split(' ')) > 2:
            third_word.append(p['play_text'].split(' ')[2])
        else:
            continue

    params['week'] = str(int(params['week'])+1)

word_set = list(set(third_word))

wordfreq = [third_word.count(w) for w in word_set]

freq_dict = {}

for x in range(len(word_set)):
    freq_dict[wordfreq[x]] = word_set[x]

final_dict = {}
wordfreq.sort(reverse=True)

for x in wordfreq:
    final_dict[freq_dict[x]] = x
