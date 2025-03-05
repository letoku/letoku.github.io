IMAGES_DIR = "images"


def replace_spaces_to_md_substitute(name: str) -> str:
    return name.replace(" ", "%20")

def create_list_entry(opening: str) -> str:
    opening_name_without_spaces = replace_spaces_to_md_substitute(opening) + ".html"
    return f"- [{opening}](./{opening_name_without_spaces})"


def add_jekyll_header(page_title: str) -> str:
    header = """---\n"""
    header += """layout: default\n"""
    header += f"""title: {page_title}\n"""
    header += """---\n"""
    return header


def create_index_page(openings: list[str]) -> str:
    page_md = add_jekyll_header("index")
    page_md += "# Chess Openings\n"
    for opening in openings:
        page_md += create_list_entry(opening)
        page_md += "\n"
    
    return page_md


def generate_sub_page(opening: str, additional_info: str, link: str) -> str:
    page_md = add_jekyll_header(opening)
    page_md += f"# {opening}\n"
    opening_name_without_spaces = replace_spaces_to_md_substitute(opening)
    page_md += f"""![{opening}]({IMAGES_DIR}/{opening_name_without_spaces})"""
    page_md += "\n\n\n"
    page_md += additional_info
    page_md += "\n"
    page_md += "\n---\n"
    page_md += f"[Reference link]({link})"

    return page_md
