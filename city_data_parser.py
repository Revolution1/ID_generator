import csv
import json

dbfile = open('city_data.txt', 'r')
dataf = csv.reader(dbfile)

result = {}

# city = ''
# city_code = ''
# city_data = {}
# province = ''
# province_code = ''
# province_data = {}
# middle_code = ''
# for code, area in dataf:
#     # if code == '232701':
#     #     import wdb; wdb.set_trace()
#     if code.endswith('0000'):
#         if province_data:
#             result[province] = province_data
#         elif city_data:
#             result[province] = city_data
#         elif province:
#             result[province] = province_code
#         province_data = {}
#         city_data = {}
#         province = area
#         province_code = code
#     elif code.endswith('00'):
#         if city_data:
#             province_data[city] = city_data
#         else:
#             province_data[city] = code
#         city_data = {}
#         city = area
#         city_code = code
#     else:
#         city_data[area] = code
#     middle_code = code[2:4]
#

db = {code: area for code, area in dataf}
dbfile.seek(0)


def count_starts(s):
    c = 0
    for i in db:
        if i.startswith(s):
            c += 1
    return c

for code, area in dataf:
    # if code == '130100':
    #     import wdb; wdb.set_trace()
    if code.endswith('0000'):
        result[code[:2]] = {}
    elif code.endswith('00'):
        if code[:2] in result:
            result[code[:2]][code[:4]] = {}
    else:
        if code[:2] in result and code[:4] in result[code[:2]]:
            result[code[:2]][code[:4]][code] = {}
        elif code[:2] in result:
            # if count_starts(code[:4]) > 1 and code.endswith('01'):
            #     result[code[:2]] = {code[:4]: []}
            # else:
            result[code[:2]][code] = {}
        else:
            result[code] = []

print json.dumps({'struct': result, 'db': db})
