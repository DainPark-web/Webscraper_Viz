import requests
from bs4 import BeautifulSoup


STACK_URL = f"https://stackoverflow.com/jobs/companies?q=python"

def get_last_page():
    # verstehen URL
    stack_result = requests.get(STACK_URL)
    # Lesen HTML
    stack_soup = BeautifulSoup(stack_result.text, "html.parser")
    # Find Pagination
    pagination = stack_soup.find("div", {"class": "s-pagination"}).find_all("a")

    pages = []
    for page in pagination[:-1]:
        pages.append(int(page.find("span").get_text()))
    
    last_page = pages[-1]
    return last_page


def get_job(job):
    company = job.find("h2").get_text().strip("\n")
    locationBox = job.find("h2").parent.find("div").find_all("div")
    location = locationBox[0].get_text()
    comt = locationBox[1].get_text()


    return {
        "Company": company,
        "Location": location,
        "Com2": comt
    }



def get_page(last_page):

    jobs = []

    for page in range(last_page):
        print(f"scrapping page{page}")
        stack_result = requests.get(f"{STACK_URL}&pg={page + 1}")
        result = BeautifulSoup(stack_result.text, "html.parser")
        page = result.find_all("div", {"class": "-company"})
        
        for job in page:
            job = get_job(job)
            jobs.append(job)

    return jobs
