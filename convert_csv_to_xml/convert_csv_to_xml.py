import sys
import os
import pandas as pd

def csvtoxml_save_to_xml_file(csvdata,xml_filepath):
    xml_data = csvdata.to_xml()

    f = open(xml_filepath, "w")
    f.write(xml_data)
    f.close()
    output="Conversion success!! Check the output file in " + xml_filepath
    display_response(0, output)
   
def load_data_from_csv_filepath(csv_filepath):
    data = pd.read_csv(csv_filepath)
    return data
    
def load_data_into_xml_filepath(xml_filepath,xmldata):
    with open(xml_filepath, mode='w') as out:   
        out.write(xmldata)
        output="Conversion success!! Check the output file in " + xml_filepath
        display_response(0, output)

def display_response(resp_code, resp_msg):
    """ Return the response message along with response code."""
    if resp_code == 0:
        sys.stdout.write(str(resp_msg) + '\n')
        sys.exit(0)
    else:
        sys.stderr.write(str(resp_msg) + '\n')
        sys.exit(1)

csv_filepath=input()
xml_filepath=input()
csvdata=load_data_from_csv_filepath(csv_filepath)
xmldata=csvtoxml_save_to_xml_file(csvdata,xml_filepath)