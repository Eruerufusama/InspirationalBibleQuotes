from sys import argv
import json


def create_probability_distribution(li):
    li_sum = sum(li)
    li_multiplyer = 100 / li_sum
    li_out = []
    for i in li:
        li_out.append((i * li_multiplyer) / 100)
    return li_out


def append_emoji(dct, elem, val):
    i_li = [val]
    i_dict = {elem: val}
    percentage_dict = {}

    for key, val in dct.items():
        i_li.append(val * (len(dct)))

    percentage_li = create_probability_distribution(i_li)

    percentage_dict[elem] = percentage_li[0]
    for i, (key, val) in enumerate(dct.items()):
        i += 1
        percentage_dict['0001' + key] = percentage_li[i]

    return percentage_dict


def json_to_dict(json_file):
    with open(json_file) as json_file:
        j_emoji = json.load(json_file)
        return dict(j_emoji)


def write_to_json(json_file, dct):
    with open(json_file, 'w') as json_file:
        print(dct)
        json.dump(dct, json_file)


if __name__ == '__main__':
    if len(argv) > 1:
        json_file = 'emojis.json'
        dict_emoji = json_to_dict(json_file)
        try:
            if argv[1] == 'add':
                emoji = argv[2]
                value = int(argv[3])
                dct = append_emoji(dict_emoji, emoji, value)
            elif argv[1] == 'rm':
                del dict_emoji[argv[2]]
                dct = dict_emoji

            write_to_json(json_file, dct)
        except:
            print('Unknown parameter. Format: admin_emoji.py \{emoji} \{value}')
