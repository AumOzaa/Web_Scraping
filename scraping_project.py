from bs4 import BeautifulSoup
import requests

html_requests = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation=').text
soup = BeautifulSoup(html_requests,'lxml')

jobs = soup.find_all('li')
# job_box = jobs[15].find('div',class_ = 'srp-job-bx')

for job in jobs:
    job_box = job.find('div',class_ = 'srp-job-bx')

    if job_box:

        job_title = job_box.find('h3').text
        job_location = job_box.find('div',class_ = 'srp-loc').text
        job_experience_required = job_box.find('div',class_ = 'srp-exp').text
        job_skill_box = job_box.find('div',class_ = 'srp-keyskills').text.replace(' ',',')
        job_company_name = job_box.find('span',class_ = 'srp-comp-name').text


        print(f'Job Title : {job_title}')
        print(f'Company Name : {job_company_name}')
        print(f'Job Location : {job_location}')
        print(f'Job Experience requried : {job_experience_required}')
        print(f'Skills Required : {job_skill_box}')
    else:
        continue
