import sys

import pandas as pd
import requests
import xml.etree.ElementTree as ET
import time
import re

pattern = re.compile(
    r"""
    ^(?:                               # Non-capturing group for optional unit
      (?P<UNIT>\d+)\s(?=\d)             # Unit (if it's followed by another number)
    )?
    (?P<HNO>\d+)\s+                     # House number
    (?P<RD>.*\s)?                       # Road (captures everything until the penultimate word)
    (?P<STS>\b\w+\b)\s                 # Street Suffix (single word preceding POD)
    (?P<POD>NW|SW|SE|NE)$               # Post Direction (always the last word)
    """, re.VERBOSE
)


# file_name = sys.argv[1]
df = pd.read_csv("../one.txt",low_memory=False)

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
        values = [components.get(key, 'None').strip() for key in ['UNIT', 'HNO', 'RD', 'STS', 'POD']]
        line = ",".join(value for value in values).strip(',')
        print("Parsed,",line)
    else:
        print(f"Unparsed")




