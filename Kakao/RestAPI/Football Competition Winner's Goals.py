#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getWinnerTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING competition
#  2. INTEGER year
#return total num of goal who won the competitions
import requests
def getWinnerTotalGoals(competition, year):
    url = f'https://jsonmock.hackerrank.com/api/football_competitions?name={competition}&year={year}'
    r = requests.get(url).json()
    winner = r['data'][0]['winner']
    url = f'https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={year}'
    result = 0
    for n in range(1,3):    
        url1 = f'{url}&team{n}={winner}'
        r = requests.get(url1).json()
        total_pages = r['total_pages']
        for t in range(total_pages):
            url2 = f'{url1}&page={t+1}'
            r = requests.get(url2).json()
            per_page = r['per_page']
            for p in range(per_page):
                try:
                    result += int(r['data'][p][f'team{n}goals'])
                except:
                    pass
    return result
