import json
employee_data='''
{
"people";[
{"name": "Aaron",
"email":["aa@gmail.com","aa2@g.com"]},
{"name": "David",
"email":["dd@gmail.com","dd2@g.com"]}
]
}
'''
#print(employee_data)
data=json.loads(employee_data)
print(data)