from bs4 import BeautifulSoup


def get_for_day(date, session):
    data_for_day = []
    cnt=1
    while True:
        URL = 'https://vukajlija.com/definicije/na-dan/' + date.strftime("%Y-%m-%d") + f"?strana={cnt}"

        soup = BeautifulSoup(session.get(URL).content, 'html.parser')

        card = soup.find(id='left-column').find_all('div', class_='clearfix definition post')

        page = []
        for c in card:
            description = c.find('blockquote')

            definition = ""
            for d in c.find('div', class_='copy').find_all('p', recursive=False):
                definition += (d.text + "\n")

            page.append({
                "term": c.find('h2').text,
                "definition": definition.strip(),
                "example": description.text.strip() if description else "",
                "author": c.find('li', class_='post-votal-show').find('a').text,
            })

        if page:
            data_for_day.extend(page)
            cnt += 1
        else:
            break

    return data_for_day


"""if __name__ == '__main__':
    items = get_for_day(date(2007,1,19))

    for item in items:
        print(item["term"])
        print(f"def: {item['definition']}")
        if (item["example"]):
            print(f"primjer: {item['example'].strip()}")
        print(f"autor: {item['author']}")
        print("\n")"""