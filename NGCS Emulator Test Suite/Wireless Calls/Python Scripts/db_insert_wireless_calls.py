import mysql.connector

def populate_database(read_file_name):

    dbconn = mysql.connector.connect(
        host="<db_host>",
        user="<db_username>",
        password = "<db_password>",
        database = "dbsEmulator"
    )

    query = """insert into call_data (
    data_type,
	telephone_number,
	esrd,
	NAM,
	street_address,
	HNO,
	RD,
	STS,
	POD,
	MP,
	LMK,
	A3,
	ESN,
	community,
	PC,
	legacy_cos,
	provider_string,
	provider_contact_number,
	provider_id,
	latitude,
	longitude,
	uncertainity,
	confidence,
	A1,
	country,
	comment,
	service_environment,
	service_type,
	service_mobility) values
	(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    data_type = None
    telephone_number = None
    esrd = None
    NAM = None
    street_address = None
    HNO = None
    RD = None
    STS = None
    POD = None
    MP = None
    LMK = None
    A3 = None
    ESN = None
    community = None
    PC = None
    legacy_cos = None
    provider_string = None
    provider_contact_number = None
    provider_id = None
    latitude = None
    longitude = None
    uncertainity = None
    confidence = None
    A1 = None
    country = None
    comment = None
    service_environment = None
    service_type = None
    service_mobility = None


    cursor = dbconn.cursor()
    in_file = open(read_file_name,"r")
    lines = in_file.readlines()

    line_number = 1;

    for line in lines:
        line_number += 1;
        if "RANDOM" in line:
            pass
        elif "SEQUENTIAL" in line:
            pass
        else:
            linefields = line.split(";")

            data_type = None if linefields[0].replace("ï»¿", "") == "" else linefields[0].replace("ï»¿", "")
            telephone_number = None if linefields[1].replace("ï»¿", "") == "" else linefields[1].replace("ï»¿", "")
            esrd =  None if linefields[2] == "" else linefields[2]
            NAM = None if linefields[7] == "" else linefields[7]
            street_address = None if linefields[8] == "" else linefields[8]
            RD = None if linefields[9] == "" else linefields[9]
            STS = None if linefields[10] == "" else linefields[10]
            POD = None if linefields[11] == "" else linefields[11]
            HNO = None if linefields[12] == "" else linefields[12]
            MP = None if linefields[13] == "" else linefields[13]
            LMK = None if linefields[14] == "" else linefields[14]
            A3 = None if linefields[15] == "" else linefields[15]
            ESN = None if linefields[16] == "" else linefields[16]
            community = None if linefields[17] == "" else linefields[17]
            PC = None if linefields[18] == "" else linefields[18]
            legacy_cos = None if linefields[19] == "" else linefields[19]
            provider_string = None if linefields[20] == "" else linefields[20]
            provider_contact_number = None if linefields[21] == "" else linefields[21]
            provider_id = None if linefields[22] == "" else linefields[22]
            latitude = None if linefields[24] == "" else linefields[24]
            longitude = None if linefields[25] == "" else linefields[25]
            uncertainity = None if linefields[26] == "" else linefields[26]
            confidence = None if linefields[27] == "" else linefields[27]
            A1 = None if linefields[28] == "" else linefields[28]
            country = None if linefields[29] == "" else linefields[29]
            comment = None if linefields[30] == "" else linefields[30]
            service_environment = None if linefields[31] == "" else linefields[31]
            service_type = None if linefields[32] == "" else linefields[32]
            service_mobility = None if linefields[33] == "" else linefields[33]

            record = (data_type,telephone_number,esrd,NAM,street_address,HNO,RD,STS,POD,MP,LMK,A3,ESN,community,PC,legacy_cos,provider_string,provider_contact_number,provider_id,latitude,longitude,uncertainity,confidence,A1,country,comment,service_environment,service_type,service_mobility)

            try:
                cursor.execute(query, record)
                dbconn.commit()
                print(str(line_number) + " Completed for " + line)
            except mysql.connector.Error as error:
                print("Failed to insert into MySQL table {}".format(error))


    in_file.close()




read_file_name = r'wireless_data.csv'

if __name__ == '__main__':
    populate_database(read_file_name)
