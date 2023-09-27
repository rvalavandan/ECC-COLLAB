import sys

import pandas as pd
import requests
import xml.etree.ElementTree as ET
import time
import re

def generate_pidflo(row_num,address_id,country,province,city,address_str,community,postal_code,name,esn_value,service_type):

    if service_type == 'fire':
        service_urn = 'urn:service:sos.fire'
    elif service_type == 'police':
        service_urn = 'urn:service:sos.police'
    elif service_type == 'ambulance':
        service_urn = 'urn:service:sos.ambulance'

 #   pattern = r'(?:(\w+) )?(\d+) ([\w\s]+) (\w{2,}) (\w{2})'
 #   pattern = r'(?:(\w+\d*)\s+)?(\d+)\s+([\w\s]+?)\s+(\w{2,})\s*(\w{2})?$'
 #   pattern = r'(?:(\w+)\s*)?(\d+\w?)\s+([\w\s]+?)\s+(\w{2,})\s*(\w{2})?$'
    pattern = r'(?:(\w+)\s*)?(\d+\w?)\s+([\w\s]+?)\s+(\w{2,})\s*(\w{1,2})?$'
    match = re.match(pattern, address_str)

    esn = str(esn_value)

    if match:
        unit, hno, rd, sts, pod = (x.strip() if x is not None else None for x in match.groups())
#        xml_string = "Row: "+str(row_num) + "|TN: "+str(address_id) + "|country: "+str(country) + "|province: "+str(province) + "|city: "+str(city) + "|unit: "+str(unit) + "|hno: "+str(hno) + "|rd: "+str(rd) + "|sts: "+str(sts) + "|pod: "+str(pod) + "|name: "+str(name) + "|ESN: "+str(esn) + "|service: "+str(service_urn)
        find_service = ET.Element('findService', attrib={'xmlns': 'urn:ietf:params:xml:ns:lost1'})

        location = ET.SubElement(find_service, 'location', attrib={'profile': 'civic'})
        civic_address = ET.SubElement(location, 'civicAddress',
                                      attrib={'xmlns': 'urn:ietf:params:xml:ns:pidf:geopriv10:civicAddr'})
        ET.SubElement(civic_address, 'country').text = 'CA'
        ET.SubElement(civic_address, 'A1').text = province
        ET.SubElement(civic_address, 'A3').text = city
        ET.SubElement(civic_address, 'STS').text = sts
        ET.SubElement(civic_address, 'RD').text = rd
        ET.SubElement(civic_address, 'POD').text = pod
        ET.SubElement(civic_address, 'HNO').text = hno
        ET.SubElement(civic_address, 'NAM').text = name
        ET.SubElement(civic_address, 'ESN', attrib={'xmlns': 'http://911datamaster.com/pidfloext'}).text = str(ESN)
        service = ET.SubElement(find_service, "service")
        service.text = service_urn

        tree = ET.ElementTree(find_service)

        xml_string = ET.tostring(find_service, encoding='utf-8', method='xml').decode('utf-8')
        xml_string = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n' + xml_string

    else:
        return None
    return xml_string


file_name = sys.argv[1]
df = pd.read_csv(file_name)

services = ["fire", "police", "ambulance"]
country = "CA"
telephone_numbers = []

for index, row in df.iterrows():
    if index < 10:
        cos = str(row.iloc[9])
        if cos == 'RES':
            row_num = str(row.iloc[0])
            telephone_number = str(row.iloc[1])
            if telephone_number not in telephone_numbers:
                telephone_numbers.append(telephone_number)
                name = str(row.iloc[3])
                address_str = str(row.iloc[4])
                city = str(row.iloc[5])
                ESN = str(row.iloc[6])
                community = str(row.iloc[7])
                postal_code = str(row.iloc[8])
                province = str(row.iloc[14])

                for service in services:
                    xml_string = generate_pidflo(row_num, telephone_number,country, province, city, address_str,community,postal_code,name,ESN,service)
                    print(xml_string) if xml_string else print("Unable to parse the Address in row: " + row_num + ":" + address_str)



