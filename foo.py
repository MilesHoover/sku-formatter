import re

raw_sku_list = ["00123456","001234567","001234567"]

def format_skus(raw_sku_list):
    formatted_sku_list = []

    for raw_sku in raw_sku_list:
        stripped_sku = re.sub('^0+', '', raw_sku) # ^ means starts with 0 and replaces it with nothing (stripping the zeros)
        if stripped_sku == '':
            continue
        else:
            formatted_sku_list.append(stripped_sku)

    # deduped_sku_set = set(formatted_sku_list) # sets are unordered, unchangable, unidexible. They also don't allow duplicates hence why this works

    # deduped_sku_list = []

    # deduped_sku_list.extend(deduped_sku_set)

    deduped_sku_list = dict.fromkeys(formatted_sku_list, 0)

    return deduped_sku_list

print(format_skus(raw_sku_list))