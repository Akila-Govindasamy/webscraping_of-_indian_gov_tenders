# Scraper1.py
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup


def scrap1(url):
    # Replace 'your_path_to_chromedriver' with the actual path to your ChromeDriver executable
    driver = webdriver.Chrome()

    try:
        # Open the web page
        driver.get(url)  # Replace with the URL of the web page containing the link

        # Find the link element by its text
        link_element = driver.find_element(By.XPATH, "//a[@title='Tenders by Organisation' and @class='link1']")

        # Click on the link
        link_element.click()

        # Wait for the new page to load with a different URL
        wait = WebDriverWait(driver, 30)  # Adjust the timeout as needed
        current_url = driver.current_url
        print(current_url)

        # Get the page source of the new page
        driver.get(current_url)
        page_source = driver.page_source

        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')

        # Find the table element with the specified attributes
        table = soup.find('table', {'id': 'table', 'class': 'list_table'})

        # Initialize a list to store the data
        data1 = []
        data = []

        # Iterate through the table rows and extract data
        for row in table.find_all('tr')[1:]:  # Skip the header row
            columns = row.find_all('td')
            if len(columns) == 3:
                s_no = columns[0].text.strip()
                org_name = columns[1].text.strip()
                tender_count = columns[2].text.strip()
                data.append([s_no, org_name, tender_count])

        with open('Tenders_Count.csv', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['S.No', 'Organisation Name', 'Tender Count'])  # Write header
            csv_writer.writerows(data)  # Write data rows

        print("Data saved as 'tenders.csv'")

        # Find and store the link elements again on the original page
        # Collect all the links' href attributes in a list
        link_elements = driver.find_elements(By.XPATH, "//tr[@class='even' or @class='odd']/td/a")
        link_urls = [link.get_attribute("href") for link in link_elements]

        # Iterate over the link URLs and visit each page
        for link_url in link_urls:
            driver.get(link_url)  # Visit the link URL

            page_source1 = driver.page_source

            # Parse the page source with BeautifulSoup
            soup = BeautifulSoup(page_source1, 'html.parser')

            # Find the table element with the specified attributes
            table1 = soup.find('table', {'id': 'table', 'class': 'list_table'})

            # Iterate through the table rows and extract data
            for row1 in table1.find_all('tr')[1:]:  # Skip the header row
                columns1 = row1.find_all('td')
                if len(columns1) == 6:
                    s_no = columns1[0].text.strip()
                    e_Published_Date = columns1[1].text.strip()
                    Closing_Date = columns1[2].text.strip()
                    Opening_Date = columns1[3].text.strip()
                    Title_and_RefNo_or_Tender_ID = columns1[4].text.strip()
                    Organisation_Chain = columns1[5].text.strip()
                    data1.append([e_Published_Date, Closing_Date, Opening_Date, Title_and_RefNo_or_Tender_ID,
                                  Organisation_Chain])

            # Save the data as a CSV file
            with open('tender_by_organisation.csv', 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(
                    ['e-Published Date', 'Closing Date', 'Opening Date', 'Title and Ref.No./Tender ID',
                     'Organisation Chain'])  # Write header
                csv_writer.writerows(data1)  # Write data rows

            driver.back() # Go back to the original page
            # Re-find the link elements on the original page


    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the WebDriver session
        driver.quit()
    return


