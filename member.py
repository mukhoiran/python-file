#Work with JSON
import json

""" write data json """

# data = {}
# data['member'] = [
#     {'name':'Messi', 'number':'10'},
#     {'name':'Suarez', 'number':'9'},
#     {'name':'Griezmann', 'number':'17'}
# ]
#
# with open('member.txt','w') as memberfile:
#     json.dump(data, memberfile)

""" read data json """
with open('member.txt','r') as memberfile:
    data = json.load(memberfile)

    print(data)
