import sys

import pandas as pd
import requests
import xml.etree.ElementTree as ET
import time
import re

pattern = re.compile(
    r"""
    ^(?:                                     # Non-capturing group for optional unit
      (?P<UNIT>[A-Z0-9]+)\s(?=\d+\s)         # Unit (if it's followed by a pure number)
    )?
    (?P<HNO>\d+[A-Z]?)\s+                    # House number with optional A-Z
    (?P<RD>.+?)\s                            # Road (captures everything until the last word)
    (?P<STS>\b\w+\b)$                        # Street Suffix (always the last word)
    """, re.VERBOSE
)


# file_name = sys.argv[1]
df = pd.read_csv("../one.txt")

for index, row in df.iterrows():
    UNIT = ""
    HNS = ""
    HNO = ""
    PRD = ""
    RD = ""
    STS = ""
    POD = ""

    address = str(row.iloc[0])
    match = pattern.match(address)
    if match:
        components = match.groupdict(default='None')
        values = [components.get(key, 'None').strip() for key in ['UNIT', 'HNO', 'RD', 'STS']]
        line = ",".join(value for value in values if value != 'None').strip(',')
        print("Parsed,",line)
    else:
        print(f"Unparsed")




