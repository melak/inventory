import json

with open('products.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for entry in data:
    if 'location' not in entry:
        entry['location'] = ''

with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
