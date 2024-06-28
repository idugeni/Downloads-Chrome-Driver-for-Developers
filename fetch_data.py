import requests
from bs4 import BeautifulSoup
import datetime

# URL to scrape
url = "https://googlechromelabs.github.io/chrome-for-testing/"

# Fetching the webpage
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting specific sections
table_wrapper = soup.find('div', class_='table-wrapper summary')
stable_section = soup.find('section', class_='status-ok', id='stable')
beta_section = soup.find('section', class_='status-ok', id='beta')
dev_section = soup.find('section', class_='status-ok', id='dev')
canary_section = soup.find('section', class_='status-ok', id='canary')

# Extracting necessary data
title = soup.find('h1').text.strip()
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Google_Chrome_icon_and_wordmark_%282011%29.svg/648px-Google_Chrome_icon_and_wordmark_%282011%29.svg.png"
description = "This page lists the latest available cross-platform Chrome for Testing versions and assets per Chrome release channel."
update_time = datetime.datetime.now(datetime.timezone.utc).isoformat()

# Function to extract inner HTML content
def extract_inner_html(element):
    return ''.join(str(child) for child in element.children)

# Generating the README content
readme_content = f"""# [{title}]({url}) availability

<div align="center">

![{title} availability]({image_url})

</div>

{description}

Consult [our JSON API endpoints](https://github.com/GoogleChromeLabs/chrome-for-testing#json-api-endpoints) if you’re looking to build automated scripts based on Chrome for Testing release data.

<div align="center">

*Last updated @ {update_time}*

</div>

<!-- IDUGENI:START -->

### Table Summary
{extract_inner_html(table_wrapper) if table_wrapper else 'Data not available.'}

{extract_inner_html(stable_section) if stable_section else 'Data not available.'}

{extract_inner_html(beta_section) if beta_section else 'Data not available.'}

{extract_inner_html(dev_section) if dev_section else 'Data not available.'}

{extract_inner_html(canary_section) if canary_section else 'Data not available.'}

<!-- IDUGENI:END -->

Source : [{url}]({url})
"""

# Writing to README.md
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("README.md successfully updated.")
