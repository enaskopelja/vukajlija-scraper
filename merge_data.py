from pathlib import Path
import json
import pprint
from tqdm import tqdm

p = Path('data')

data = []
cnt=0
for path in tqdm(p.glob('*.json')):
    with open(path, encoding="utf8") as f:
        try:
            d = json.load(f)
        except:
            print(f"error loading file {str(path)}")

        for entry in d:
            data.append(entry)


with open(p/'all.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
