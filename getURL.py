from urllib.request import urlopen
import xml.etree.ElementTree as ET

"""get METAR from aviationweather.gov"""

link = "https://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=tafs&requesttype=retrieve&format=xml&hoursBeforeNow=3&mostRecentForEachStation=constraint&stationString=EDDH"


def read_url(url):
    f = urlopen(url)
    my_file = f.read()
    my_string = my_file.decode("utf-8")  # convert bytes to string
    root = ET.fromstring(my_string)
    return root


def print_root(given_root) -> None:
    print(given_root.find("request_index").text)
    for child in given_root:
        print(child.tag, child.attrib)
    a = list(given_root.iter('wind_speed_kt'))
    print(a)
    for elem in a:
        print(elem.text)


root = read_url(link)
print_root(root)

"""

import untangle
obj = untangle.parse('myfile')

print (obj.given_root.child['raw_text'])


https://azure.microsoft.com/de-de/services/open-datasets/catalog/noaa-global-forecast-system/
# This is a package in preview.
from azureml.opendatasets import NoaaGfsWeather

from dateutil import parser


start_date = parser.parse('2019-09-19')
end_date = parser.parse('2019-09-20')
gfs = NoaaGfsWeather(start_date, end_date)
gfs_df = gfs.to_pandas_dataframe()

"""
