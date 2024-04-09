from bs4 import BeautifulSoup
import requests

# import lxml
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "lxml")
# soup = BeautifulSoup(contents, "html.parser")

# print(soup.title.string)
#
# print(soup.prettify())

# print(soup.p)
#
# all_anchgor_tags = soup.find_all(name="a")
# print(all_anchgor_tags)
# for tag in all_anchgor_tags:
#     # print(tag.getText)
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
# section_heading = soup.find(name="h3", class_="heading")
#
# company_url = soup.select_one(selector="p  a")
# print(company_url)

# name = soup.select_one(selector="#name")
# # print(name)
# headings = soup.select(".heading")
# print(headings)

# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, "html.parser")
# find_articles = soup.find_all(class_="titleline")
# articles = []
# for article in find_articles:
#     articles.append(article.findChild())
# article_texts = []
# article_links = []
# for article_tag in articles:
#     if article_tag.getText() == "":
#         pass
#     else:
#         article_text = article_tag.getText()
#         article_texts.append(article_text)
#         article_link = article_tag.get("href")
#         article_links.append(article_link)
#
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(class_="score")]
#
# highest_score = max(article_upvotes)
# index = article_upvotes.index(highest_score)
# print(article_texts[index+1])
# print(article_links[index+1])
# print(article_upvotes[index])

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empire = response.text
soup = BeautifulSoup(empire, "html.parser")
articles = soup.find_all(class_="gallery__content-item")
titles= []
for article in articles:
    title = article.select_one(selector="div h3")
    title = title.getText()
    titles.append(title)
titles.reverse()
print(titles)
with open("movies.txt", "w", encoding="utf-8") as file:
    for title in titles:
        file.write(f"{title}\n")