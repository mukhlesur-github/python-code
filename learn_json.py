import json

try:
    with open('data/mukhlesur_cv.json','r') as file:
        data=json.load(file)
except FileNotFoundError:
    print("Error: mukhlesur_cv.json not found")
    exit()

print(f"first_name: {data['first_name']}")
print(f"roles: {data['experience']['roles'][0]}")