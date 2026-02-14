import requests
import json
from datetime import datetime
import csv

def write_to_info(url):
    response = requests.get(url)
    data = response.json()
    user_info = {}
    with open('info.json','w') as file:
        user_info['username'] = data['username']
        user_info['honor'] = data['honor']
        user_info['clan'] = data['clan']
        user_info['rank'] = data['ranks']['overall']['name']
        user_info['leaderboardPosition'] = data['leaderboardPosition']
        user_info['totalCompleted'] = data['codeChallenges']['totalCompleted']
        json.dump(user_info,file)

def write_to_completed(url):
    response = requests.get(url)
    completed = response.json()
    list_of_completed_tasks = []
    for i in completed['data']:
        s = str(i['completedAt'])
        dt = datetime.fromisoformat(s.replace('Z',"+00.00"))
        list_of_completed_tasks.append((i['name'],i['completedLanguages'],dt.date()))

    with open('completed.csv','w',newline='',encoding='utf-8-sig') as file:
        writer = csv.writer(file,delimiter=',')
        writer.writerow(['Name of kata','Completed language','Completed Date'])
        writer.writerows(list_of_completed_tasks)
    print('Completed:',completed['totalItems'],'katas')
    
def check_url(url):
    response = requests.get(url)
    return response.json()


username = input('Enter username: ')
info_url = f'https://www.codewars.com/api/v1/users/{username}'
data = check_url(info_url)
completed_url = f'http://www.codewars.com/api/v1/users/{username}/code-challenges/completed'
if 'success' in data.keys():
    print('Entered a wrong username!!!USERNAME NOT FOUND')
else:
    write_to_info(info_url)
    write_to_completed(completed_url)