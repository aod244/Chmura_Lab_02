import csv, json, os
import pandas as pd
import matplotlib.colors as colors

master_df = pd.DataFrame()

for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
        master_df = master_df.append(pd.read_csv(file))

master_df.to_csv('combined.csv', index=False)

df = pd.read_csv('combined.csv')
hex_value = df['value'].tolist()
rgb = []
for i in hex_value:
    new_i = colors.hex2color(i)
    rgb.append(new_i)

df['rgb'] = rgb 

df.to_csv('combined.csv') 

with open ("combined.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    data = {"color": []}
    for row in reader:
        data["color"].append({"color name": row[1], "Hex": row[2], "RGB": row[3]})

with open ("names.json", "w") as file:
    json.dump(data, file, indent=4)
 