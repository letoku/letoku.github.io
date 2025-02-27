import os
import requests
import bs4
from bs4 import BeautifulSoup


URL = "https://www.thechesswebsite.com/chess-openings/"
MAIN_DIV_CLASS = "elementor-element elementor-element-7f0d9d87 elementor-widget elementor-widget-shortcode"
IMAGES_DIR = "images"


def get_page_and_soup(url: str) -> bs4.BeautifulSoup:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    
    return soup


def get_openings(soup: bs4.BeautifulSoup) -> list[bs4.element.Tag]:
    main_div = soup.find("div", {"class": MAIN_DIV_CLASS})
    openings_container = main_div.find(id="cb-container")

    openings = openings_container.find_all(recursive=False)

    return openings


def download_img(opening: bs4.element.Tag, opening_name: str) -> bool:
    # img_tag = opening.find("img")
    # if img_tag is None:
    #     return False
    # img_url = img_tag.get("src")
    # if img_url is None:
    #     return False
    
    # img_name = os.path.join(IMAGES_DIR, opening_name)
    # with open(img_name, "wb") as f:
    #     img_data = requests.get(img_url).content
    #     f.write(img_data)
    #     print(f"Downloaded: {img_name}")

    return True


def get_opening_name(opening: bs4.element.Tag) -> str:
    name_header = opening.find("h5")
    if name_header is None:
        return None
    else:
        return name_header.get_text()


def process_opening(opening: bs4.element.Tag, parsed_openings: list):
    not_free_content = opening.find("span")
    if not_free_content is not None:
        return
    name = get_opening_name(opening)
    if name is None:
        return
    downloaded = download_img(opening, name)
    if downloaded:
        parsed_openings.append(name)


def download_page() -> list[str]:
    soup = get_page_and_soup(URL)

    openings = get_openings(soup)
    parsed_openings = []

    for opening in openings:
        process_opening(opening, parsed_openings)

    return parsed_openings
