import csv

def getinfo():
    facilityname = []
    coords = []
    beds = []
    opening = []
    closing = []
    contact = []
    icu = []
    ccu = []
    type = []

    with open("readingFile.csv", 'r') as infile:  # Opening contents of files
        reader = csv.reader(infile)
        header = next(reader)[0]  # Column Title
        #print(header)  # Print column title
        for row in reader:
            currentCoords = float(row[3]), float(row[4])  # print row values
            currentBeds = row[11]
            currentFacilityname = row[1]
            currentOpening = row[5]
            currentClosing = row[6]
            currentContact = row[12]
            currentICU = row[7]
            currentCCU = row[8]
            currentType = row[2]

            facilityname.append(currentFacilityname)
            coords.append(currentCoords)
            beds.append(currentBeds)
            opening.append(currentOpening)
            closing.append(currentClosing)
            contact.append(currentContact)
            icu.append(currentICU)
            ccu.append(currentCCU)
            type.append(currentType)

            """
            seq = row[0]
            facilityname = row[1]
            type = row[2]
            latitude = row[3]
            longitude = row[4]
            opening = row[5]
            closing = row[6]
            icu = row[7]
            ccu = row[8]
            vc = row[9]
            tc = row[10]
            capacity = row[11]
            print(seq,facilityname,type,latitude,longitude,opening,closing,icu,ccu,vc,tc,capacity)
            """
    return coords, beds, facilityname, opening,closing, contact, icu, ccu, type