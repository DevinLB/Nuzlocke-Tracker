# MAKE A JSON FILE WITH CURRENT DATABASE
# python3 manage.py dumpdata --natural-foreign --natural-primary --sort_keys=True --indent=2 > main_app/fixtures/full_seed.json
# LOAD A JSON FILE INTO YOUR DATABASE
# python3 manage.py loaddata SEEDNAME.json

import requests
import json
print("Sanity")

## ---- File Path to Fixtures Folder ----
# ../main_app/fixtures/SEED_NAME.json


### -=-=-=-=-=- START SEEDING CODE -=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-



response_test = requests.get("https://pokeapi.co/api/v2/pokemon/1")

# Check status code, 200 means API call successfully returned data
print(response_test.status_code)
# Put data into a usable format
pokemon_parsed = response_test.json()
print(pokemon_parsed['name'])


pk_data = []

number_of_pokemon = 2
for i in range(number_of_pokemon):

  url = "https://pokeapi.co/api/v2/pokemon/" + str(i + 1)
  response = requests.get(url)

  pk_parsed = response.json()
  # print(pk_parsed['name'])

  pk_name = pk_parsed['name']
  pk_id = pk_parsed['id']
  pk_json = pk_parsed

  pk_data.append(
    {"model": "main_app.pkinfo", 
    "pk": i + 1, 
    "fields": {
      "name": pk_name,
      "pk_id": pk_id,
      "jfield": pk_parsed,
      },
    }
  )

  print(pk_name, pk_id)

# print(pk_data)
# print(json.dumps(pokemon_parsed, sort_keys=True, indent=4))
# print(type(pokemon_parsed))
# print(type(response_test))


### -=-=-=-=-=-  END SEEDING CODE  -=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-

# # Open and add the new data to a separate JSON file
### -------------- (Uncomment next 4 lines to leave testing mode)
f = open('main_app/fixtures/pokemon.json', 'w')
json.dump(pk_data, f, sort_keys=True, indent=2)
# Close the file
f.close()

print("Successfully added")