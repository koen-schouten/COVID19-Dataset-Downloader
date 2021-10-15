"""
Gets the Municipality and Security region codes from the dataset and stores it in a "RVIG.json" json file as follows:

    {
     "GM0003" : {"region_name" : "Appingedam", "Region_level" : "Gemeente"},
     "GM0014" : {"region_name" : "Groningen", "Region_level" : "Gemeente"},
     "VR01" : {"region_name" : "Groningen", "Region_level" : "Veiligheidsregio"},
    }

"""
import urllib.request
import json

# Webpage where the file is located
BASE_URL = "https://data.rivm.nl/covid-19/"

# Two files that use RVIG codes as
#
# Region_code : "GM0014"
# Region_name : "Groningen"

# For municipalities as:
FILE_NAME = "COVID-19_aantallen_gemeente_cumulatief.json"
# For Security regions and country
FILE2_NAME = "COVID-19_gedrag.json"

# Location where the file should be saved
FILE_DESTINATION_FOLDER = "data/"

# file name
OUTPUT_FILE_NAME = "RVIG.json"

if __name__ == "__main__":
    url1 = BASE_URL + FILE_NAME
    url2 = BASE_URL + FILE2_NAME
    file_destination = FILE_DESTINATION_FOLDER + OUTPUT_FILE_NAME

    response = urllib.request.urlopen(url1)
    json_gemeentes = json.loads(response.read())

    response = urllib.request.urlopen(url2)
    json_veiligheids_regios = json.loads(response.read())

    RVIG_codes = {}
    for data_point in json_gemeentes:
        if(data_point["Municipality_code"] != None):
            RVIG_codes[data_point["Municipality_code"]] = {"region_name" : data_point["Municipality_name"], "Region_level" : "Gemeente"}

    for data_point in json_veiligheids_regios:
        if(data_point["Region_code"].startswith("V")):
            RVIG_codes[data_point["Region_code"]] = {"region_name" : data_point["Region_name"], "Region_level" : "Veiligheidsregio"}
        elif(data_point["Region_code"].startswith("N")):
            RVIG_codes[data_point["Region_code"]] = {"region_name" : data_point["Region_name"], "Region_level" : "Nederland"}

    #Stores the json object as a file
    with open(file_destination, 'w') as outfile:
        json.dump(RVIG_codes, outfile)




