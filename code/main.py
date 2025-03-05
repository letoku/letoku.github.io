from parser import download_page
from markdown_generator import create_index_page, generate_sub_page
from searcher import find_additional_info

if __name__ == "__main__":
    parsed_openings = download_page()
    page_md = create_index_page(parsed_openings)
    with open('index.md', 'w') as file:
        file.write(page_md)

    for opening in parsed_openings:
        additional_info, link = find_additional_info(opening)
        if additional_info is None:
            continue
        opening_page_md = generate_sub_page(opening, additional_info, link)

        with open(f'{opening}.md', 'w') as file:
            file.write(opening_page_md)
