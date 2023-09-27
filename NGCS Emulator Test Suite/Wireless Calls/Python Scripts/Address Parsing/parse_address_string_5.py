import pandas as pd
import re

pattern = re.compile(
    r"""
    ^(?P<HNO>\d+)                   # House number at the start
    \s+(?P<RD>[\w\s]+?)            # Road name (greedily captures everything until STS, non-greedy)
    \s+(?P<STS>\b\w+\b)            # Street Suffix (single word)
    \s+(?P<POD>NE|NW|SE|SW)$       # Post Direction (always the last word)
    """, re.VERBOSE
)




# file_name = sys.argv[1]
df = pd.read_csv("../../one.txt",low_memory=False)

for index, row in df.iterrows():
    HNO = None
    PRD = None
    RD = None
    STS = None
    POD = None

    address = str(row.iloc[0])
    match = pattern.match(address)

    if match:
        components = match.groupdict(default='None')
        values = [components.get(key, 'None').strip() for key in ['HNO', 'RD', 'STS', 'POD']]
        line = ",".join(value for value in values).strip(',')
        print("Parsed,", line)
    else:
        print(f"Unparsed")










