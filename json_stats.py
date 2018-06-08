import json

auc=0.456
r2=0.99

with open("dominostats.json", "w") as f:
   f.write(json.dumps({"auc":auc, "r2":r2}))

