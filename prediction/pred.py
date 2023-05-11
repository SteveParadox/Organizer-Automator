from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests
import pandas as pd

from _ext import teams, prediction

urls = [
    "https://www.flashscore.mobi/",
    "https://www.flashscore.mobi/?d=1",
    "https://www.flashscore.mobi/?d=2",
    
]

# Getting the fixtures of the already predicted teams
def get_fixtures():
    try:
        for_team, against_team, any_win = prediction()
        match_fix = (span.next_sibling.strip() for url in urls 
                                               for span in BeautifulSoup(requests.get(url).content, "lxml").find('div', {'id': 'score-data'}).find_all('span') 
                                               if span.next_sibling is not None and span.next_sibling.next_sibling is not None)
        match_fix = [i for i in match_fix]
        # Use a set comprehension instead of a for loop here
        compiled_for = {item for selection in set(line.strip() for line in for_team) for item in match_fix if selection in item}
        compiled_against = {item for selection in set(line.strip() for line in against_team) for item in match_fix if selection in item}
        compiled_any = {item for selection in set(line.strip() for line in any_win) for item in match_fix if selection in item}

        return compiled_for, compiled_against, compiled_any
    
    except Exception as e:
        print(f"Error: {e}")
        return None 

def arrange_fixture():
    # Removing unwanted data and organizing the fixtures into sections
    compiled_for, compiled_against, compiled_any = get_fixtures()
    compiled_for = {match for match in compiled_for if 'Ladies' not in match and 'Women' not in match }
    compiled_against = {match for match in compiled_against if 'Ladies' not in match and 'Women' not in match }
    compiled_any = {match for match in compiled_any if 'Ladies' not in match and 'Women' not in match }

    return compiled_for, compiled_against, compiled_any

def my_pick():
    compiled_for, compiled_against, compiled_any = get_fixtures() # Cleaned Fixtures
    for_team, against_team, any_win, data = teams() # league tables

    compiled_for = [[s.strip() for s in item.split('-')] for item in compiled_for]
    compiled_against = [[s.strip() for s in item.split('-')] for item in compiled_against]
    compiled_any = [[s.strip() for s in item.split('-')] for item in compiled_any]

    comp_ = []
    _comp = []
    pick_for = []
    pick_against = []

    for compiled, comp in zip([compiled_against, compiled_for], [comp_, _comp]):
        for pair in compiled:
            sublist = []
            for item in pair:
                for row in data:
                    if item in row:
                        sublist.extend(row)
            if len(sublist) == 26:
                comp.append(sublist)

    for i, j in zip(comp_, compiled_against):
        if i[0] in j and i[-1] >= 3 and i[15] >= 14:
            pick_against.append(i[0])
        elif i[13] in j and i[12] >= 3 and i[2] >= 14: 
            pick_against.append(i[13])
    for i, j in zip(_comp, compiled_for):
        if i[0] in j and i[-1] <= -2 and i[15] <= 13:
            pick_for.append(i[0])
        elif i[13] in j and i[12] <= -2 and i[2] <= 13:
            pick_for.append(i[13])
    
    return pick_for, pick_against


if __name__ == "__main__":
    pick_for, pick_against = my_pick()
    print(pick_for)
    print(pick_against)
