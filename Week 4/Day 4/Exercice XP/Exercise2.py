import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)

salary = data['company']['employee']['payable']['salary']

data['company']['employee']['birth_date'] = '2005-09-25'

with open('updated_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
