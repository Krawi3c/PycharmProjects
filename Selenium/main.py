# from interaction import Interaction

# events_html = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
#
# events_list = [element.text for element in events_html.find_elements(By.TAG_NAME, "li")]
# events_dict = {}
# events = []
# for element in events_list:
#     for item in element.split("\n"):
#         events.append(item)
# index = 0
# for element in range(len(events)):
#     if element % 2 == 0:
#         events_dict[index] = {"time": events[element], "name": events[element + 1]}
#         index += 1
#
# print(events_dict)
