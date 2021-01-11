import requests, re
from bs4 import BeautifulSoup
from Model import Project, UsersProject
from tool import log as _l

log = _l("PARSER", "parser.log")

def write_db(f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        mutation = UsersProject.custom_insert(result)
        return mutation
    return wrapper

@write_db
def get_projects():
    url = "https://kwork.ru/projects"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) \
                                                Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)'}
    projects = []
    response = requests.get(url, headers=headers)
    log.info( "Status code: %d. Length: %d " % ( response.status_code, len( response.text ) ) )
    html = response.text
    soup = BeautifulSoup( html, "html.parser" )
    items = soup.select("div[class*=js-card]")
    for item in items[:]:
        title = item.select_one("div[class*=header-title]")
        title = title.text if title else "Error title"
        price = item.select_one("div.wants-card__right")
        price = re.findall( r"\d{3}|\d{1,2}\s\d{3}", str(price) )
        price = " - ".join(price)
        description = item.select_one("div.breakwords.hidden")
        description = description.text.replace("Скрыть","").strip() if description else "Description error"
        if description == "Description error":
            description = item.select_one("div.breakwords.first-letter ~ div")
            description = description.text if description else "Description error2"
            # import pdb;pdb.set_trace()
        proposal_count = item.find(lambda tag:tag.name == "span" and "Предложений:" in tag.text)
        proposal_count = re.findall(r"\d+", proposal_count.text)[0] if proposal_count else "Prop error"
        author = item.select_one("a.v-align-t")
        author = author.text if author else "Author error"
        link = item.select_one("div.wants-card__header-title a")
        link = link['href'] if link else "Link error"
        timer = item.find( lambda tag:tag.name == "span" and "Осталось" in tag.text)
        timer = timer.text if timer else "timer error"
        params = (title, description, author, proposal_count,
                  price, timer, link)
        project = Project( *params )
        projects.append( project )
    return projects

def main():
    res = get_projects()
    # import pdb;pdb.set_trace()

if __name__ == '__main__':
    main()