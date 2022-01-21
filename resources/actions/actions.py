import csv
import json

# wget https://raw.githubusercontent.com/xivapi/ffxiv-datamining/master/csv/Action.csv
# remove line 3 then 1

actions = {}

with open('Action.csv', 'r') as csvfile:
  reader = csv.DictReader(csvfile)
  for line in reader:
    #"/i/000000/000157.png"
    icon = int(line['Icon'])
    actions[line['\ufeff#']] = {
      'Image': f'/i/{int(int(icon/1000)*1000):06}/{icon:06}.png' if icon != 0 else '',
      'CooldownGroup': [
        int(line['CooldownGroup']),
        int(line['AdditionalCooldownGroup']),
      ]
    };

with open('actions.json', 'w') as jsonfile:
  jsonfile.write(json.dumps(actions, indent=2))
