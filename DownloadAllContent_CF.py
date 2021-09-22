import requests
import bs4
import logging

# debugging set up
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.info('Start of program')


url = "https://academy.hoppersroppers.org/course/view.php?id=8"
page = requests.get(url)
page.raise_for_status()

soup = bs4.BeautifulSoup(page.content, "html.parser")
page_content = soup.find(id="page-content")

# gets a list of all the urls on the website
links = []
for alink in page_content.find_all("a", href=True):
    link = alink["href"]
    if "section" in link:
        continue
    else:
        links.append(link)

# loops over the URL list
for link in links:
    try:
        logging.debug('This is iteration for %s', link)
        url2 = link
        page2 = requests.get(url2)
        page2.raise_for_status()

        soup2 = bs4.BeautifulSoup(page2.content, "html.parser")
        page_content2 = soup2.find(id="page-content")
        page_text2 = page_content2.find_all("div", attrs={"role": "main"})
        # appends the text from each website to a file
        for text in page_text2:
            f = open("ComputingFundamentals.txt", "a")
            f.write(text.text.strip())
            f.close()
    except:
        continue

logging.debug('End of program')
