from stack import get_last_page, get_page
from save import save_file


last_page = get_last_page()

results = get_page(last_page)

save_file(results)

