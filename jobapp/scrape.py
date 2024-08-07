import requests
from bs4 import BeautifulSoup
from .models import *
from datetime import datetime, date
import logging

BASE_URL = 'https://www.myjobmag.co.ke'  # Base URL for job listings

def fetch_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.content

def parse_html(content):
    return BeautifulSoup(content, 'lxml')

def parse_date(date_str):
    # Remove 'Posted: ' prefix
    date_str = date_str.replace('Posted: ', '').strip()
    
    # Parse the date in 'MMM D, YYYY' format
    try:
        parsed_date = datetime.strptime(date_str, '%b %d, %Y').date()
        formatted_date = parsed_date.strftime('%Y-%m-%d')
        logging.info(f"Parsed date: {formatted_date}")
    except ValueError as e:
        logging.error(f"Error parsing date '{date_str}': {e}")
        formatted_date = date.today().strftime('%Y-%m-%d')
        logging.info(f"Using today's date: {formatted_date}")

    return formatted_date

def extract_job_links(soup):
    job_links = []
    job_list = soup.find_all('ul', class_='job-list')
    for item in job_list:
        for link in item.find_all('a', href=True):
            job_links.append(BASE_URL + link['href'])
    return job_links

def extract_job_details(soup):
    title_element = soup.find('h1', class_='job-title')
    company_element = soup.find('span', class_='company')
    job_industry_element = soup.find('span', class_='industry')
    date_posted_element = soup.find('span', class_='date')
    job_description_element = soup.find('div', class_='description')
    job_key_info_element = soup.find('div', class_='key-info')
    location_element = soup.find('span', class_='location')

    date_posted_raw = date_posted_element.text.strip() if date_posted_element else None
    date_posted = parse_date(date_posted_raw) if date_posted_raw else date.today().strftime('%Y-%m-%d')
    
    return {
        'title': title_element.text.strip() if title_element else 'Unknown',
        'company': company_element.text.strip() if company_element else 'Unknown',
        'job_industry': job_industry_element.text.strip() if job_industry_element else 'Unknown',
        'date_posted': date_posted,
        'job_description': job_description_element.text.strip() if job_description_element else 'No description provided',
        'job_key_info': job_key_info_element.text.strip() if job_key_info_element else 'No key information provided',
        'location': location_element.text.strip() if location_element else 'Unknown',
        'source': 'Web'
    }

def save_to_database(job_data):
    for job in job_data:
        logging.info(f"Saving job: {job['title']}")
        JobListing.objects.update_or_create(
            title=job['title'],
            defaults={
                'company': job.get('company', 'Unknown'),
                'job_industry': job.get('job_industry', 'Unknown'),
                'date_posted': job.get('date_posted', date.today()),  
                'job_description': job.get('job_description', 'No description provided'),
                'job_key_info': job.get('job_key_info', 'No key information provided'),
                'location': job.get('location', 'Unknown'),
                'source': job.get('source', 'Unknown')
            }
        )

def scrape_job_listings():
    search_url = 'https://www.myjobmag.co.ke/search/jobs?q=software+engineer&location='
    current_page = 1
    max_pages = 10 
    
    zindua_alumni_db = []

    while current_page <= max_pages:
        url = f"{search_url}&page={current_page}"
        logging.info(f"Fetching page {current_page}")
        search_content = fetch_page(url)
        search_soup = parse_html(search_content)

        job_links = extract_job_links(search_soup)
        if not job_links:
            break
        
        for link in job_links:
            job_content = fetch_page(link)
            job_soup = parse_html(job_content)
            job_details = extract_job_details(job_soup)
            zindua_alumni_db.append(job_details)

        current_page += 1

    save_to_database(zindua_alumni_db)

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


