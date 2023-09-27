import pandas as pd

df = pd.read_csv("../../one.txt",low_memory=False)

seen = set()

for index, row in df.iterrows():
    HNO = None
    PRD = None
    RD = None
    STS = None
    POD = None

    address = str(row.iloc[0]).strip()

    if address not in seen:
        print(address)
        seen.add(address)
