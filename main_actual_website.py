from bs4 import BeautifulSoup
import requests

html_requests = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation=').text
soup = BeautifulSoup(html_requests,'lxml')

jobs = soup.find('li')
job_name = jobs.find('div',class_ = 'srp-job-heading')
job_posted = jobs.find('span',class_ = 'posting-time')
final_job = job_name.find('a')

location = jobs.find('div',class_ = 'srp-loc')

skills_class = jobs.find('div',class_ = 'srp-keyskills').a.text
# particulars = skills_class.find_all('a',class_ = 'srphglt')



print(final_job.text)
print(location.text)
print(job_posted.text)
for aSkill in skills_class:
    print(aSkill)