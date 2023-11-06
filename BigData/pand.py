import pandas as pd

data = {
    'nama': ['fadhil','romi','aldo'],
    'age': [20,19,18],
    'job': ['Engineer', 'Manager', 'CEO'],
}
df = pd.DataFrame(data)
print(df)