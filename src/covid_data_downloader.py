import urllib.request
import json

# Webpage where the file is located
BASE_URL = "https://data.rivm.nl/covid-19/"

# Location where the file should be saved
FILE_DESTINATION_FOLDER = "data/"

# The files and relevant keys we want to download
files = [{"file_name": "COVID-19_aantallen_gemeente_per_dag.json", "keys": ["Date_of_publication", "Municipality_code", "Total_reported", "Hospital_admissions", "Deceased"]},
         {"file_name": "COVID-19_Infectieradar_symptomen_per_dag.json",
             "keys": ["Date_of_statistics", "Perc_covid_symptoms", "MA_perc_covid_symptoms"]},
         {"file_name": "COVID-19_aantallen_gemeente_cumulatief.json",
             "keys": ["Date_of_report", "Municipality_code", "Total_reported", "Hospital_admissions", "Deceased"]},
         {"file_name": "COVID-19_aantallen_settings_per_dag.json",
             "keys": ["Date_of_publication", "Security_region_code", "Source_and_contact_tracing_phase", "Total_reported", "Setting_reported", "Number_settings_reported"]},
         {"file_name": "COVID-19_gedrag.json", "keys": ["Date_of_measurement", "Region_code", "Subgroup_category", "Subgroup",
                                                        "Indicator_category", "Indicator", "Sample_size", "Figure_type", "Value", "Lower_limit", "Upper_limit"]},
         {"file_name": "COVID-19_ic_opnames.json",
             "keys": ["Date_of_statistics", "IC_admission_notification", "IC_admission"]},
         {"file_name": "COVID-19_prevalentie.json",
             "keys": ["Date", "prev_low", "prev_avg", "prev_up", "population"]},
         {"file_name": "COVID-19_reproductiegetal.json",
             "keys": ["Date", "Rt_low", "Rt_avg", "Rt_up", "population"]},
         {"file_name": "COVID-19_rioolwaterdata.json",
             "keys": ["Date_measurement", "RWZI_AWZI_code", "RNA_flow_per_100000"]},
         {"file_name": "COVID-19_uitgevoerde_testen.json",
             "keys": ["Date_of_statistics", "Security_region_code", "Tested_with_result", "Tested_positive"]},
         {"file_name": "COVID-19_vaccinatiegraad_per_gemeente_per_week_leeftijd.json",
             "keys": ["Date_of_statistics", "Region_code", "Birth_year", "Vaccination_coverage_partly", "Vaccination_coverage_completed"]},
         {"file_name": "COVID-19_varianten.json",
             "keys": ["Date_of_statistics_week_start", "Variant_code", "Sample_size", "Variant_cases"]},
         {"file_name": "COVID-19_ziekenhuis_ic_opnames_per_leeftijdsgroep.json",
             "keys": ["Date_of_statistics_week_start", "Age_group", "Hospital_admission_notification", "Hospital_admission", "IC_admission_notification", "IC_admission"]},
         {"file_name": "COVID-19_ziekenhuisopnames.json", "keys": ["Date_of_statistics", "Municipality_code",
                                                                   "Municipality_code", "Security_region_code", "Hospital_admission_notification", "Hospital_admission"]},
         ]


def process_file(file_name, keys):
    # location where the file is located on the web
    url = BASE_URL + file_name
    # location where the file shoulde be saved
    file_destination = FILE_DESTINATION_FOLDER + file_name

    # donwloading the file from the website and loading it as a json object
    response = urllib.request.urlopen(url)
    json_object = json.loads(response.read())

    # Strips all unnecessary keys from the json file and creates a new json object without these keys
    new_json_object = []
    for item in json_object:
        new_item = {k: v for (k, v) in item.items() if k in keys}
        new_json_object.append(new_item)

    #Stores the json object as a file
    with open(file_destination, 'w') as outfile:
        json.dump(new_json_object, outfile)

if __name__ == "__main__":
    for file in files:
        process_file(file["file_name"], file["keys"])