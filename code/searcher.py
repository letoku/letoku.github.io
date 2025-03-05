import time
from duckduckgo_search import DDGS


WAITING_TIME = 0.5


def find_additional_info(opening_name: str) -> tuple[str, str]:
    result = None
    
    try:
        result = DDGS().text(opening_name, max_results=1)[0]
    except:
        time.sleep(WAITING_TIME)
        try:
            result = DDGS().text(opening_name, max_results=1)[0]
        except Exception as e:
            return "", ""
    
    return result['body'], result['href']

# def find_additional_info(opening_name: str) -> tuple[str, str]:
#     result = None
#     while True:
#         try:
#             result = DDGS().text(opening_name, max_results=3)[0]
#         except:
#             print("Error while scraping")
#             print(opening_name)
#             time.sleep(WAITING_TIME)
#             continue
#         break
    
#     print(f"Successfully scraped {opening_name}")
#     return result['body'], result['href']
