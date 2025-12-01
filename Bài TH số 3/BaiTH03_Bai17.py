data = [
    {"name": "A", "score": 7},
    {"name": "B", "score": 9},
    {"name": "A", "score": 8},
]
result = {}

for item in data:
    ten = item['name']
    diem = item['score']
    
    if ten not in result:
        result[ten] = [] 
        
    result[ten].append(diem)

print(result)
