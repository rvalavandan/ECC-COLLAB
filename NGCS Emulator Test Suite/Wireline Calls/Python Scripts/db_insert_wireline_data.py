import mysql.connector

def populate_database(read_file_name):

    dbconn = mysql.connector.connect(
        host="dbhost",
        user="dbusername",
        password = "dbpass",
        database = "database"
    )

    query = """insert into table_call_data_for_ali_spill (
    data_type,
    telephone_number,
    NAM,
    street_address,
    UNIT,
    HNS,
    HNO,
    RD,
    STS,
    POD,
    A3,
    A1,
    country,
    ESN,
    community,
    PC,
    legacy_cos,
    provider_id,
    comment,
    provider_string,
    provider_contact_number,
    service_environment,
    service_type,
    service_mobility

    ) values
    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    data_type = telephone_number = NAM = street_address = UNIT = HNS = HNO = RD = STS = POD = A3 = A1 = country = ESN = community = PC = legacy_cos = provider_id = comment = provider_string = provider_contact_number = service_environment = service_type = service_mobility = None



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
            NAM = street_address = None if linefields[2] == "" else linefields[2]
            street_address = None if linefields[7] == "" else linefields[7]
            UNIT = None if linefields[8] == "" else linefields[8]
            HNS = None if linefields[9] == "" else linefields[9]
            HNO = None if linefields[10] == "" else linefields[10]
            RD = None if linefields[11] == "" else linefields[11]
            STS = None if linefields[12] == "" else linefields[12]
            POD = None if linefields[13] == "" else linefields[13]
            A3 = None if linefields[14] == "" else linefields[14]
            A1 = None if linefields[15] == "" else linefields[15]
            country = None if linefields[16] == "" else linefields[16]
            ESN = None if linefields[17] == "" else linefields[17]
            community = None if linefields[18] == "" else linefields[18]
            PC = None if linefields[19] == "" else linefields[19]
            legacy_cos = None if linefields[20] == "" else linefields[20]
            provider_id = None if linefields[29] == "" else linefields[29]
            provider_string = None if linefields[27] == "" else linefields[27]
            provider_contact_number = None if linefields[28] == "" else linefields[28]
            comment = None if linefields[35] == "" else linefields[35]
            service_environment = None if linefields[36] == "" else linefields[36]
            service_type = None if linefields[37] == "" else linefields[37]
            service_mobility = None if linefields[38] == "" else linefields[38]

            record = (data_type, telephone_number, NAM, street_address, UNIT, HNS, HNO, RD, STS, POD, A3, A1, country, ESN, community, PC, legacy_cos, provider_id, comment, provider_string, provider_contact_number, service_environment, service_type, service_mobility)

            try:
                cursor.execute(query, record)
                dbconn.commit()
                print(str(line_number) + " Completed for " + line)
            except mysql.connector.Error as error:
                print("Failed to insert into MySQL table {}".format(error))


    in_file.close()




read_file_name = r'ALI_spill_landline_dataset.csv'

if __name__ == '__main__':
    populate_database(read_file_name)
