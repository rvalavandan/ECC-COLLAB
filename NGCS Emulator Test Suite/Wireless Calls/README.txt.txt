1. Create the wireless_calls_small_dataset.csv file (though the fields are delimited by semicolon rather than comma). 
The same file will be used to populate the database that will be used for ADR and HELD responses.
This file will be used to populate the call scenario file wireless_calls.xml.

data_type - internally used by calgary to point if ita real address or made up one (for some scenarios like looooooooooooooooooooooooong street name etc).	
caller_number - you can use real numbers if you have a database or use create_tns.py to create random phone numbers using the NPA you use.	
esrd	- same as above
NAM - free string that will appear as caller name in the call-taker interface	
nena-callid	- use create_nena_call_ids.py to create random numbers and copy/paste into the spreadsheet
nena-incident-id- use create_nena_incident_ids to create these
uuid1	- use create_uuids.py to create these.
uuid2	- use create_uuids.py to create these.	
street_address	- full string of street address like: 123 4200 COUNTRY HILLS BLVD NW - this will be split into UNIT, HNO, RD, STS and POD. I have used several iterations of the scripts under Address Parsing. 
For the 40,000 addresses in our dataset, this is where I spent much of the time on. It requires some learning about how the civic addresses are used in NG9-1-1 and require multiple passes, python skill, excel skill,
Notepad++ and a variety of tools are used,did I say it requires enormous patience?
RD	- Street name
STS	- Street suffix
POD	- typically quadrant
HNO	- house number
MP	- Mile Post for rural addresses
LMK	- Landmark
A3	- city
ESN	- Emergency service number for the addresses
community	- community	
legacy_cos	
Provider_String	- TELUS for example
Provicer_Number	- Contact number for the provider
Provider-ID	- TELMU for example 
uuid3		- use create_uuids.py to create these.
latitude	- latitude of the caller
longitude	- longitude
uncertainity	- radius in metres
confidence	- always 90
A1	- Province code, AB, BC etc.
country	- CA for us
comment	- used to indicate class of service.
service_environment	
service_type	
service_mobility	
random_number1	
uuid4	- use create_uuids.py to create these.	
END_OF_RECORD


