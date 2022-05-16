import requests
import datetime
import re


def POSIX_time():
    todate_date = datetime.date.today()
    fromdate_date = todate_date - datetime.timedelta(days=period)
    POSIX_todate = int((todate_date - datetime.date(1970, 1, 1)).total_seconds())
    POSIX_fromdate = int((fromdate_date - datetime.date(1970, 1, 1)).total_seconds())
    return POSIX_fromdate, POSIX_todate


def questions_about_tag(tag):
    dict_questions = requests.get(
        f'https://api.stackexchange.com/2.3/questions?fromdate={date[0]}&todate={date[1]}&order=desc&sort=activity&tagged={tag}&site=stackoverflow&filter=!nKzQUR3Egv').json()
    all_questions = {questions["link"]: questions['body'] for questions in dict_questions['items']}
    for link, question in all_questions.items():
        cleaner = re.compile('<.*?>')
        question = re.sub(cleaner, '', question)
        print(link, question, sep='\n')


period = 2
date = POSIX_time()
our_tag = 'Python'
questions_about_tag(our_tag)
