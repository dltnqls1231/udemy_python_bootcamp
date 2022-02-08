import pandas as pd

df = pd.DataFrame({'id': ['a', 'b', 'c', 'd', 'e', 'f'],
                   'var': [1, 2, 3, 4, 5, 6]})

new = df[df["id"].isin(['z'])]
newenw = new.to_dict()
print(newenw)