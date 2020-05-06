import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from df2gspread import gspread2df as d2f

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

##scope is added by default, idk why yet

credentials = ServiceAccountCredentials.from_json_keyfile_name(
         'key.json', scope)

##credentials for the google api, server client file obtained while creating the key. json file

gc = gspread.authorize(credentials)
##creating object of the gspread by passing credentials variable created as argument
##this gc object is our main

####

##https://towardsdatascience.com/using-python-to-push-your-pandas-dataframe-to-google-sheets-de69422508f

##using the df2gspread library. gspread2df func downloads sheet

# sprd_key = '1erN620rZwWtNZVm-r__8bHw8wEMlfkCHb-dKmAeZqIA'
# #this is obtained from the url of the sheet in between its there find it.
#
# wks_name = 'Sheet1'
# #name of worksheet to be downloaded
#
# df = d2f.download(sprd_key, wks_name, credentials=credentials, row_names=False)
# #downloads the file at given key, wksheet name, self expl rest.
#
#
# print(df)

####

##https://medium.com/@vince.shields913/reading-google-sheets-into-a-pandas-dataframe-with-gspread-and-oauth2-375b932be7bf


wks = gc.open("electric").sheet1
data = wks.get_all_values()
headers = data.pop(0)
df = pd.DataFrame(data, columns=headers)
print(df.head())

##didnt work because sheets and drive API wasnt activated fot the project. followed the link to activate them. on click
readings1 = []
for i in df['user1_reading']:
    readings1.append(i)

print(readings1)
