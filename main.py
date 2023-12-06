#webscraping 99 acres using selenium as it doesnt support scraping
#using chrome in debug mode

#import libraries
import pdb
import pandas as pd
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests


#setting driver
driver_path = r"D:\chromedriver-win64_120\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(service=service, options=chrome_options)

# cmd command
# "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\selenium\ChromeProfile"

#fetching html content of the page
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# url = "https://www.99acres.com/search/property/buy/gurgaon?city=8&preference=S&area_unit=1&res_com=R"


#function to introduce random delays
def random_delay():
    # Generate a random delay between 1 and 5 seconds
    delay = random.uniform(4.8, 12.9)
    time.sleep(delay)



# Initialize lists to store extracted data
data = {
    "Property": [],
    "Project": [],
    "Rating": [],
    "Places Nearby": [],
    "Price": [],
    "Price per Sq.ft": [],
    "Area": [],
    "Area in Sq.ft": [],
    "Area in Sq.m": [],
    "Description": [],
    "Posted Date": [],
    "Posted By": []
}


try:
    #webscraping all pages in loop
    while True:
        # Fetching html content of the page
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        # Webscraping all boxes on the page
        property_boxes = soup.find_all('div', class_='srpTuple__cardWrap')

        # Extract information from each property box
        for prop in property_boxes:
            try:
                property_name = prop.find("h2", class_="srpTuple__tupleTitleOverflow").text.strip()
            except AttributeError:
                property_name = None

            try:
                project_name = prop.find("td", class_="srpTuple__propertyPremiumHeading").text.strip()
            except AttributeError:
                project_name = None
            
            try:
                rating = prop.find("span", class_="Fomo__carouselShortlistTag").text.strip()
            except AttributeError:
                rating = None
                
            try:
                places_nearby = prop.find("div", class_="SliderTagsAndChips__nearByInfo").text.strip()
            except AttributeError:
                places_nearby = None

            try:
                price = prop.find("td", id="srp_tuple_price").text.strip()
            except AttributeError:
                price = None
                
            try:
                price_per_sqft = prop.find("div", id="srp_tuple_price_per_unit_area").text.strip()
            except AttributeError:
                price_per_sqft = None

            try:
                area = prop.find("td", id="srp_tuple_primary_area").text.strip()
            except AttributeError:
                area = None

            try:
                description = prop.find("div", class_="ellipsis srpTuple__smallDescriptionStyle").text.strip()
            except AttributeError:
                description = None

            try:
                posted_date = prop.find("div", class_="srpTuple__postedByText").text.strip()
            except AttributeError:
                posted_date = None

            try:
                posted_by = prop.find("div", class_="srpTuple__postedByText list_header_semiBold Ng100 ellipsis").text.strip()
            except AttributeError:
                posted_by = None

            # Splitting area into different parts
            try:
                area_parts = area.split('\n')
                area_sqft = area_parts[0]
                area_sqm = area_parts[1]
            except (AttributeError, IndexError):
                area_sqft = None
                area_sqm = None

            # Append extracted data to respective lists
            data["Property"].append(property_name)
            data["Project"].append(project_name)
            data["Rating"].append(rating)
            data["Places Nearby"].append(places_nearby)
            data["Price"].append(price)
            data["Price per Sq.ft"].append(price_per_sqft)
            data["Area"].append(area)
            data["Area in Sq.ft"].append(area_sqft)
            data["Area in Sq.m"].append(area_sqm)
            data["Description"].append(description)
            data["Posted Date"].append(posted_date)
            data["Posted By"].append(posted_by)

        # Check if the "Next Page" button is clickable
        next_page = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[5]/div[3]/div[3]/div[3]/a')
        if 'disabled' in next_page.get_attribute('class'):
            # If the "Next Page" button is disabled, break the loop
            break

        # Introduce a random delay
        random_delay()

        # Click on the next page button
        next_page.click()

        # Introduce another delay before continuing
        random_delay()

except Exception as e:
    print(e)


finally:
    # Create a dataframe from the extracted data
    df = pd.DataFrame(data)

    # Display the dataframe
    print(df)
