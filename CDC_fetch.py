import requests
import xml.etree.ElementTree as ET

# Step 1: Define the API endpoint
url = "https://wonder.cdc.gov/controller/datarequest/D76"

# Step 2: Define the XML payload
payload = """
<request-parameters>
    <parameter>
        <name>B_1</name>
        <value>D76.V9</value> <!-- Group by County -->
    </parameter>
    <parameter>
        <name>B_2</name>
        <value>D76.V1</value> <!-- Group by Year -->
    </parameter>
    <parameter>
        <name>F_D76.V27</name>
        <value>42</value> <!-- Pennsylvania (State FIPS Code) -->
    </parameter>
    <parameter>
        <name>F_D76.V2</name>
        <value>X40-X44</value> <!-- ICD-10 Codes for unintentional drug overdose -->
    </parameter>
    <parameter>
        <name>O_V1_fmode</name>
        <value>freg</value> <!-- Regular mode for selecting years -->
    </parameter>
    <parameter>
        <name>O_show_totals</name>
        <value>true</value> <!-- Show totals -->
    </parameter>
    <parameter>
        <name>O_show_zeros</name>
        <value>true</value> <!-- Show zero-value rows -->
    </parameter>
    <parameter>
        <name>O_show_suppressed</name>
        <value>true</value> <!-- Show suppressed data -->
    </parameter>
    <parameter>
        <name>V_D76.V1</name>
        <value>2010
                2011
                2012
                2013
                2014
                2015
                2016
                2017
                2018
                2019
                2020</value> <!-- Select years -->
    </parameter>
    <parameter>
        <name>accept_datause_restrictions</name>
        <value>true</value> <!-- Accept data use agreement -->
    </parameter>
</request-parameters>
"""

# Step 3: Send the POST request
headers = {
    "Content-Type": "application/xml",  # Indicate that the request is XML
}

response = requests.post(url, data=payload, headers=headers)

# Step 4: Process the response
if response.status_code == 200:
    # Parse the XML response
    print("Request successful!")
    with open("cdc_wonder_response.xml", "w") as file:
        file.write(response.text)
    print("Response saved as 'cdc_wonder_response.xml'.")
else:
    print(f"Failed to fetch data: {response.status_code}")
    print(f"Error details: {response.text}")