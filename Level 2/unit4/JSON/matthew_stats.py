import json
filename = '.vscode\\unit4\\JSON\\player.json'
stats_file = open(filename)
text = stats_file.read()
stats_file.close()

stats = json.loads(text)
player = stats['person']

print(f'Player name: {player["fullName"]}')
print(f'{player["primaryNumber"]} {player["height"]} {player["primaryPosition"] ["name"]}')