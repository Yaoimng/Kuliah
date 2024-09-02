from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import json

# Function to scrape data from Dicoding
def scraper(url):
    try:
        print("im scraping")
        # Configure WebDriver to use headless Firefox
        options = Options()
        # options.add_argument('-headless')
        driver = webdriver.Firefox(options=options)
        
        
        # Get the URL given
        driver.get(url)
 
        # Selenium will wait for a maximum of 5 seconds for an element matching the given criteria to be found. 
        # If no element is found in that time, Selenium will raise an error.
        try:
            wait = WebDriverWait(driver, timeout=5)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="css-1dq1dix"]')))
            print('element found')
        except:
            raise LookupError("There is no element specified")
        
        # BeautifulSoup will parse the URL
        contents = driver.page_source
        soup = BeautifulSoup(contents, 'html.parser')

        # Prepare the variable for JSON data
        contents = []
        
        # BeautifulSoup will find the CSS class that contain product container
        for content in soup.find_all('div', class_='css-bk6tzz e1nlzfl2'):
            
            # Get the text from the specified element and assign them to the variables
            content_name = content.find_all('span', {'class':'css-20kt3o'})[0].text
            content_price = content.find_all('span', {'class':'css-o5uqvq'})[0].text
            content_loc = content.find_all('span', {'class': 'css-ywdpwd'})[0].text
            content_toko = content.find_all('span', {'class': 'css-ywdpwd'})[1].text


            # Not all contents in the list has rating, so we should manage it. 
            # If it has rating, get the text. If none, set it to empty string.
            try:
                # Extract the content rating
                rating_element = content.find('div', class_='css-1riykrk')
                if rating_element:
                    # Count the number of stars (represented by <img> tags)
                    stars = len(rating_element.find_all('img', class_='css-177n1u3'))
                    # Extract the rating count from the <span> element
                    rating_count = rating_element.find('span').text
                    content_rating = f'{stars} stars ({rating_count})'
                else:
                    content_rating = ''

                # Extract the content discount and price
                disc_element = content.find('div', class_='css-1nl8cnn')
                if disc_element:
                    discount_percentage = disc_element.find_all('div')[0].text
                    price = disc_element.find_all('div')[1].text
                    content_disc = f'{discount_percentage}, {price}'
                else:
                    content_disc = ''

            except IndexError:
                # Handle cases where elements are not found
                content_rating = ''
                content_disc = ''

            # print(f'Content Rating: {content_rating}')
            # print(f'Content Discount: {content_disc}')

        #     # Not all contents in the list has total students, so we should manage it. 
        #     # If it has total students, get the text. If none, set it to empty string.
        #     try:
        #         content_total_students = content.find_all('span', {'class':'mr-3'})[1].get_text()
        #     except:
        #         content_total_students = ''
        
            # Append the scraped data into contents variable for JSON data
            contents.append(
                {
                    'Produk': content_name,
                    'Harga': content_price,
                    'Lokasi': content_loc,
                    'Toko': content_toko,
                    'Rating': content_rating,
                    'Diskon': content_disc,
                    
                }
            )
        # print(contents)
        driver.quit()
            
        return contents
    
    except Exception as e:
        print('error: ' + e)
        driver.quit()
 
if __name__ == '__main__':
    # Define the URL
    url = 'https://www.tokopedia.com/p/handphone-tablet/handphone'
    print('mulai Scraping')
    data = scraper(url)

    # Save data to JSON file
    with open('tokped_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)