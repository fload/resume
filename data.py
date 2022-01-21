
import pandas as pd
import datetime
import json

#TODO - create a dataclass



Jobs = '''# Freelance Developer
## BrightMinds - Remote
*October 2020 to April 2021*  
What started as simple automation of legacy software ( Govt. ), involving a lot of scraping and data wrangling evolved into a full application suite of micro services hosted on google cloud services. The data involved hi-res aerial drone images in which the Micro services on Google's App Engine would handle processing the images exif/gps data into a Google-hosted Postgres/Postgis database, and finally storing the image and created thumbnails into Google's Cloud Storage. A front end was created in Django which allowed for the images to be viewed overlayed on a map (mapbox or downloadable KLM file) with Geo tagged documents listed and editable in browser. Small tools being built around this are as follows: flight path creation and delegation, drone pilot batch Image upload page, PDF document upload (scraped, tagged, mapped and saved into database).
This was a fun puzzle in the enormous field that is digital cartography, as my client was on a budget we did not use any of the convenient ESRI tools. However, QGIS was more than sufficient for our team's needs. Should the project have continued, I believe we could have leveraged Google's Cloud vision to enhance/verify our data-sets.
# Division Manager
## Century Calibrating Company
*January 2008 to January 2017*  
Being a small oil/gas tech service company I really had a lot of responsibilities. I handled all new employee training and every new client’s on-boarding. I took charge of bringing the company into the digital age, creating a portal for client document access and consolidation; created various android applications for field calculations in python leveraging the Kivy Gui framework. Also built custom hardware devices for calibration of meters using a mechanical Photocell bridged to Arduino and then Raspberry pi’s which replaced giant analog boxes. During my time here is when I learned to love programming! 
'''

Technical_skillset = [('Python',0.9,6),
            ('Javascript',0.5,2),
            ('Java',0.5,1),
            ('Node',0.4,1),
            ('GIS',0.7,1.5),
            ('Google Cloud',0.7,1.5),
            ('Docker', 0.5,1.5),
            ('Numpy',0.5,1.5),
            ('Pandas',0.7,1.5),
            ('SQL',0.6,1),
            ('NoSql(Mongo)', 0.7,2.5),
            ('ORM',0.7,2.5),
            ('Automation',0.75,4),
            ('Tensorflow',0.4,1),
            ('HTML',0.85,5),
            ('Linux',0.9,8),
            ('C#',0.5,1),
            ('Unity3d',0.5,0.5),
            ('Selenium',0.7,0.5),
            ('Kivy(cross-platform)',0.75,1),
            ('JSON',0.8,2),
            ('Jenkins',3,0.5),
            ('PostGres/Postgis',7.5,2),
            ('XML', 0.7,1)
            ]

#create a dataframe from list of tuples

skills_df = pd.DataFrame(Technical_skillset, columns= ['Skill','Use','Experience_years'])

#sort the items so the chart looks pretty
skills_df.sort_values(by=['Use'], inplace=True, ascending=False)


def load_data():
    with open('sample.json', 'r') as fh:
        data = pd.read_json(fh)
        return data.dropna()


mapping_sample = load_data().sample(10000)
