test = {"name": "John", "address": {"State": "FL", "City": "Miami"}}

for key, value in test.items():
    if isinstance(value, dict):
        print(f"{value} is a nested json element")
        for nkey, nvalue in value.items():
            print(nkey, nvalue)
