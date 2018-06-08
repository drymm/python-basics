import json

train_accuracy = 0.893
test_accuracy = 0.912

with open("dominostats.json", 'a') as f:
   f.write("\n")
   f.write(json.dumps({"train_accuracy":train_accuracy,"test_accuracy":test_accuracy}))
