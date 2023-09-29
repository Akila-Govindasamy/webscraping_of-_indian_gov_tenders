# Scraper1.py
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup


def scrap2(url):

    # Replace 'your_path_to_chromedriver' with the actual path to your ChromeDriver executable
    driver = webdriver.Chrome()

    try:
        # Open the web page
        driver.get(url)  # Replace with the URL of the web page containing the link

        # Find the link element by its text
        link_element = driver.find_element(By.XPATH, "//a[@title='Tenders by Organisation' and @class='link1']")

        # Get the current URL before clicking the link
        # Click on the link
        link_element.click()

        # Wait for the new page to load with a different URL
        wait = WebDriverWait(driver, 30)  # Adjust the timeout as needed
        current_url = driver.current_url

        print(current_url)

        # Get the page source of the new page
        driver.get(current_url)

        link_elements = driver.find_elements(By.XPATH, "//tr[@class='even' or @class='odd']/td/a")
        link_urls = [link.get_attribute("href") for link in link_elements]

        csv_file = "Tenders_Detail.csv"
        # Define column headers
        column_headers = [
            "Organisation Chain", "Tender Reference Number", "Tender ID", "Withdrawal Allowed",
            "Tender Type", "Form Of Contract", "Tender Category", "No. of Covers",
            "General Technical Evaluation Allowed", "ItemWise Technical Evaluation Allowed",
            "Payment Mode", "Is Multi Currency Allowed For BOQ", "Is Multi Currency Allowed For Fee",
            "Allow Two Stage Bidding", "Tender Fee in ₹", "Fee Payable To", "Fee Payable At",
            "Tender Fee Exemption Allowed", "EMD Amount in ₹", "EMD through BG/ST or EMD Exemption Allowed",
            "EMD Fee Type", "EMD Percentage", "EMD Payable To", "EMD Payable At", "Title", "Work Description",
            "NDA/Pre Qualification", "Independent External Monitor/Remarks", "Tender Value in ₹",
            "Product Category", "Sub category", "Contract Type", "Bid Validity(Days)", "Period Of Work(Days)",
            "Location", "Pincode", "Pre Bid Meeting Place", "Pre Bid Meeting Address", "Pre Bid Meeting Date",
            "Bid Opening Place", "Should Allow NDA Tender", "Allow Preferential Bidder", "Published Date",
            "Bid Opening Date", "Document Download / Sale Start Date", "Document Download / Sale End Date",
            "Clarification Start Date", "Clarification End Date", "Bid Submission Start Date",
            "Bid Submission End Date", "Name", "Address"
        ]

        # Open the CSV file for writing
        with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(column_headers)

            # Iterate over the link URLs and visit each page
            for link_url in link_urls:
                driver.get(link_url)  # Visit the link URL

                page_source1 = driver.page_source

                # Parse the page source with BeautifulSoup
                soup = BeautifulSoup(page_source1, 'html.parser')

                # Initialize row_data for each page
                link_elements1 = driver.find_elements(By.XPATH, "//tr[@class='even' or @class='odd']/td/a")
                inner_link_urls = [link1.get_attribute("href") for link1 in link_elements1]  # Use a different variable name

                # Iterate through the table rows and extract data for each column
                for link_url1 in inner_link_urls:
                    driver.get(link_url1)
                    text_data = []
                    # Define the XPath expressions
                    xpath_list = [
                        '//*[@id="content"]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table/tbody',
                        '//*[@id="content"]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table[2]/tbody/tr/td/table/tbody/tr[9]/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody',
                        '//*[@id="content"]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table[2]/tbody/tr/td/table/tbody/tr[9]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody',
                        '//*[@id="content"]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table[2]/tbody/tr/td/table/tbody/tr[14]/td/table/tbody',
                        '//*[@id="content"]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table[2]/tbody/tr/td/table/tbody/tr[17]/td/table/tbody',
                        '//*[@id="content"]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table[2]/tbody/tr/td/table/tbody/tr[23]/td/table/tbody',
                        '//*[@id="content"]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table[2]/tbody/tr/td/table/tbody/tr[26]/td/table/tbody'
                    ]

                    # Iterate through the XPath expressions
                    for xpath in xpath_list:
                        try:
                            # Find the element with the specified XPath
                            element = driver.find_element(By.XPATH, xpath)

                            # Get the innerHTML of the element (i.e., the HTML content)
                            html_content = element.get_attribute('innerHTML')
                            # Parse the HTML content with BeautifulSoup
                            soup = BeautifulSoup(html_content, 'html.parser')
                            # Find all elements with the class 'td_field' within the parsed HTML
                            td_field_elements = soup.find_all(class_='td_field')

                            # Extract the text from each 'td_field' element and append it to the text_data list
                            for element in td_field_elements:
                                text_data.append(element.get_text(strip=True))

                        except Exception as e:
                            print(f"XPath '{xpath}' not found. Error: {e}")

                    # Write row_data to a new row in the CSV file
                    csv_writer.writerow(text_data)

                driver.back()  # Go back to the original page

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the WebDriver session
        driver.quit()
    return

