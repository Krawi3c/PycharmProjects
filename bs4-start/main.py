from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

tr = soup.find_all('tr', class_="athing")
articles_list = []
for item in tr:
    id = item.get('id')
    span = item.findChildren('span', 'titleline')
    title = span[0].text
    link = span[0].find('a').get("href")
    try:
        upvote = soup.find('span', id=f"score_{id}").text
        upvote = int(upvote.replace(" points", ""))
    except AttributeError:
        pass
    articles_list.append(upvote)
highest_score = articles_list.index(max(articles_list))
print(tr[highest_score].findChildren('span', 'titleline')[0].text)























# import lxml
#
# with open('website.html') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
#
# # all_anchor_tags = soup.find_all(name='a')
# #
# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))
#
# # heading = soup.find(name='h1', id='name')
# # print(heading)
#
# # section_heading = soup.find(name='h3', class_='heading')
# # print(section_heading)
#
# # company_url = soup.select_one(selector='p a')
# # print(company_url)
#
# # name = soup.select_one('#name')
# # print(name)
#
# # headings = soup.select('.heading')
# # print(headings)
#
#
#
#
