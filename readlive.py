import pandas as pd
import json
f = open("live.txt", "r")
x=json.loads(json.dumps(f.readline()))
print(x[1])
