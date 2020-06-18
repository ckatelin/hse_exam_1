from itertools import islice

def read_data(file_name):
    data = set()
    with open(file_name, 'r', encoding='utf-8') as f:
        f.readline()
        for line in f:
            parts = line.strip().split(',')
            key = (parts[2], parts[3])
            if parts[7]:
                record = tuple(islice(parts, 2, None))
                data.add(record)
    return data


def make_dict(data, key_extractor, sort_key, reverse=False):
    d = {}
    for item in data:
        key = key_extractor(item)
        if key not in d:
            d[key] = [item]
        else:
            d[key].append(item)
    for item in d:
        d[item].sort(key=sort_key, reverse=reverse)
    return d


def save_data(location_dict):
    for key in location_dict:
        with open(f'output/{key[0]}-{key[1]}.csv', 'w', encoding='utf-8') as f:
            for record in location_dict[key]:
                f.write(','.join(record))
                f.write('\n')


all_tickets = read_data('renfe.csv')
location_dict = make_dict(all_tickets, lambda t: (t[0], t[1]), lambda t: t[2])
save_data(location_dict)
date_dict = make_dict(all_tickets, lambda t: (t[0], t[1], t[2][:10]), lambda t: t[5])

while True:
    source = input("Enter origin: ").upper()
    if not source:
        break
    dest = input("Enter destination: ").upper()
    date = input("Enter date in the YYYY-MM-DD format: ")
    key = (source, dest, date)
    if key in date_dict:
        for item in date_dict[key]:
            print(item)
    else:
        print("Combination not found")
