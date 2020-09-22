import requests, sys

from pprint import pprint as pp

base_url = 'https://api.collegefootballdata.com/{}'

play_types = {}
stat_types = {}
##FIRST WORD
skip_first_word = ['Timeout',
                   ]

##SECOND WORD
skip_second_word = ['Penalty'
                    ]

##THIRD WORD
play_words = ['run','pass','kickoff','punt','sacked'
              ]
trash_words = ['clock', '1st','2nd','3rd','4th'
               ]
skip_words = ['Jr.','III','II', 'II,','IV'
              ]

final_dict = {'run': 54927, 'pass': 52449, 'kickoff': 9167, 'punt': 7886, 'sacked': 3512, 'clock': 2811, 'Jr.': 2671, 'III': 2042, 'Penalty,': 1729, 'for': 1214, '3rd': 847, '1st': 846, 'ST,': 820, 'false': 772, '4th': 770, 'rush': 694, 'II': 545, 'False': 432, 'Defensive': 307, 'Plumlee': 303, 'incomplete': 239, 'delay': 178, 'CAROLINA,': 173, 'TECH,': 154, 'Offensive': 141, 'on-side': 136, 'Waal': 122, '32': 113, '27': 107, 'unsportsmanlike': 105, 'personal': 101, 'ST': 100, '25': 98, '40': 97, '31': 94, '43': 90, 'MISS,': 88, '26': 86, '22': 85, '47': 84, '35': 83, '23': 82, '38': 80, '29': 79, 'MICHIGAN,': 78, '28': 76, 'Delay': 75, '41': 74, '50': 73, '39': 72, '33': 71, 'deep': 70, '45': 69, '1': 67, '46': 65, 'sideline': 63, 'Buren': 62, '49': 61, 'STATE,': 60, 'Taylor': 59, 'complete': 52, 'IV': 51, '20': 50, 'Romo': 47, 'VIRGINIA,': 46, 'MEXICO,': 44, 'KENTUCKY,': 43, 'A&M,': 42, 'Personal': 40, 'FL,': 39, 'JOSÉ': 38, 'Rosenberg': 37, 'TEXAS,': 36, 'FLORIDA,': 35, 'MEXICO': 34, 'MICH,': 33, 'TENN,': 32, 'OH,': 31, 'ALABAMA,': 30, 'FORCE,': 29, '19': 28, '5': 27, 'COLLEGE,': 26, 'substitution': 25, '4': 24, 'blocked': 23, 'Illegal': 22, 'illegal': 21, '8': 19, '13': 18, 'Ulonzo': 17, '9': 16, '12': 15, 'ILLINOIS,': 14, 'Miller': 12, 'Ineligible': 11, 'OT': 10, 'Brown': 9, 'up': 8, 'intercepted': 7, 'T': 6, 'targeting': 5, 'roughing': 4, 'Lynn': 3, 'the': 2, 'II,': 1}
##r = requests.get(base_url.format('play/types'))
##for row in r.json():
##    play_types[row['id']] = row['text']
##
##
##r = requests.get(base_url.format('play/stat/types'))
##              
##for row in r.json():
##    stat_types[row['id']] = row['name']

params = {'year': '2019', 'week': '1'}



params['week'] = str(int(params['week'])+1)
