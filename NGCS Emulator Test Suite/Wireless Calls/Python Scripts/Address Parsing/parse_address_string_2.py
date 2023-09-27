import pandas as pd
import re

pattern = re.compile(
    r"""
    ^(?P<HNO>[A-Za-z]*\d+[A-Za-z]?)\s+       # House number, which may start with letters, contain digits, and end with an optional letter
    (?P<RD>(?:\w+\s){0,2}\w+)\s             # Road (1 to 3 words)
    (?P<STS>\b\w+\b)                        # Street Suffix
    (?:\s(?P<POD>NW|SW|SE|NE))?             # Optional: Post Direction
    $                                       # End of string
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

    address_fields = address.split()

    if len(address_fields) == 3:
        if match:
            components = match.groupdict(default='None')
            values = [components.get(key, 'None').strip() for key in ['HNO', 'RD', 'STS', 'POD']]
            line = ",".join(value for value in values).strip(',')
            print("Parsed,", line)
        else:
            print(f"Unparsed")
    else:
        print(f"Unparsed")







