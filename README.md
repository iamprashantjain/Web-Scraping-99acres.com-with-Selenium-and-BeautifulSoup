# Web-Scraping-99acres.com-with-Selenium-and-BeautifulSoup

![image](https://github.com/iamprashantjain/Web-Scraping-99acres.com-with-Selenium-and-BeautifulSoup/assets/111352127/6af98a58-d907-48db-964f-458c0ad020eb)


This Python script leverages Selenium, a web automation tool, in conjunction with BeautifulSoup, a HTML parsing library, to extract real estate data from 99acres.com. Utilizing Chrome in debug mode, the Selenium WebDriver navigates through the site, emulating user interaction to bypass scraping restrictions.

The script mimics human behavior by introducing random delays between page requests to prevent detection while collecting details of properties listed on the site. Extracted information encompasses property names, project details, pricing, area specifications, descriptions, and associated metadata.

The iterative process scrapes multiple pages, identifying and storing property details until it exhausts the available listings or encounters an exception. Upon completion, the script compiles the gathered data into a structured Pandas DataFrame, facilitating subsequent analysis or storage of the acquired real estate information.
