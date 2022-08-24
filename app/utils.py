import bs4, helium, time

def get_missions():
    url = "https://www.freelancer.ma/missions/"
    browser = helium.start_chrome(url, headless=True)
    time.sleep(5)
    html = browser.page_source
    soup = bs4.BeautifulSoup(html, "html.parser")
    mission_ul = soup.find_all("li", class_="mission-freelance")
    missions = []
    for li in mission_ul:
        a = li.find(class_="mission_title")
        p = li.find("p", class_="my-2")
        budget = li.find("span", class_="budget")
        ul_headers = li.find("ul", class_="headers")
        date, kind, state, by = ul_headers.find_all("li", "list-inline-item")
        ul_skills = li.find("ul", class_="list-unstyled")
        skills = [li_el.text for li_el in ul_skills.find_all("li")]
        missions.append(dict(
            title = a.text,
            link = "https://www.freelancer.ma/"+ a["href"],
            desc = p.text,
            date = date.text,
            kind = kind.text,
            state = state.text,
            by = by.text,
            skills = skills,
            budget = budget.text
        ))
    return missions