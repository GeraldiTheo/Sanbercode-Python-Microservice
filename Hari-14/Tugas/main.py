import json

result = {}
result['Indonesia'] = []
result['Jepang'] = []
result['India'] = []

file = open('country/country_indonesia.json')
data = json.load(file)

for datum in data:    
    cases = datum['Cases']
    result['Indonesia'].append(cases)

file = open('country/country_japan.json')
data = json.load(file)

for datum in data:    
    cases = datum['Cases']
    result['Jepang'].append(cases)
    
file = open('country/country_india.json')
data = json.load(file)

for datum in data:    
    cases = datum['Cases']
    result['India'].append(cases)

print(json.dumps(result, indent=2))