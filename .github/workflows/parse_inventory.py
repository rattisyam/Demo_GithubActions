import json
matrix = []
with open("inventory.ini") as f:
    for line in f:
        if line.strip() and not line.startswith("["):
            parts = line.split()
            node = parts[0]
            ip = [p.split("=")[1] for p in parts if p.startswith("ansible_host=")][0]
            matrix.append({"node": node, "ip": ip})
print(json.dumps({"include": matrix}))

