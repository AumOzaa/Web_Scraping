from bs4 import BeautifulSoup
import requests


storage_file = "storageFile.txt"

def saving_output(job_title_tag, job_company_tag, job_location_tag, job_experience_tag, job_skill_box_tag):

    file = open("storageFile.txt",'a')
    file.write(f"Job Title: {job_title_tag}\n")
    file.write(f"Company Name: {job_company_tag}\n")
    file.write(f"Job Location: {job_location_tag}\n")
    file.write(f"Experience Required: {job_experience_tag}\n")
    file.write(f"Skills: {job_skill_box_tag}\n")
    file.write('-'*50)
    file.write("\n")


html_requests = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation=').text
soup = BeautifulSoup(html_requests, 'lxml')

jobs = soup.find_all('li')

for job in jobs:
    job_box = job.find('div', class_='srp-job-bx')

    if job_box:
        job_heading = job_box.find('div', class_='srp-job-heading')
        job_title_tag = job_heading.find('h3') if job_heading else None
        job_company_tag = job_heading.find('span', class_='srp-comp-name') if job_heading else None

        job_location_tag = job_box.find('div', class_='srp-loc')
        job_experience_tag = job_box.find('div', class_='srp-exp')
        job_skill_box_tag = job_box.find('div', class_='srp-keyskills')

        if all([job_title_tag, job_company_tag, job_location_tag, job_experience_tag, job_skill_box_tag]):
            # print(f"Job Title: {job_title_tag.text.strip()}")
            # print(f"Company Name: {job_company_tag.text.strip()}")
            # print(f"Job Location: {job_location_tag.text.strip()}")
            # print(f"Experience Required: {job_experience_tag.text.strip()}")
            # print(f"Skills: {job_skill_box_tag.text.strip().replace(' ', ',')}")
            # print("-" * 50)
            saving_output(job_title_tag.text.strip(), job_company_tag.text.strip(), job_location_tag.text.strip(), job_experience_tag.text.strip(), job_skill_box_tag.text.strip().replace(' ', ','))
