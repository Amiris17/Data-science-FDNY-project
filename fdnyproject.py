"Name: Amiris Olivo"
"Email: Amiris.Olivo56@Myhunter.cuny.edu"
"URL:https://github.com/AimbotMiz/DS/blob/main/DS.ipynb"
"Reference: https://www.nyc.gov/site/fdny/about/resources/data-and-analytics/citywide-statistics.page" "2019"
"Title: Fire Incidents per borough in NYC"
import pandas as pd
import matplotlib.style as style
import matplotlib.pyplot as plt


df= pd.read_csv("FDNY_Monthly_Response_Times.csv")



First_month_year1=df.loc[df['YEARMONTH']=='2009/07'] # I am Selecting Yearmonth and the rows where it is 2009/07

sorted=First_month_year1.sort_values(by='INCIDENTCOUNT') # I wanted to sort this by the respective column

new_df=sorted.groupby('INCIDENTBOROUGH') #Assigning a New data frame to avoid overwriting original

# Selecting the groups we want for each borough and acquiring their mean #This step will be repeated multiple times
Queens=new_df.get_group('Queens')
Queens_Incidents0907=(Queens['INCIDENTCOUNT'].mean())

Bronx=new_df.get_group('Bronx')
Bronx_Incidents0907=(Bronx['INCIDENTCOUNT'].mean())


Brooklyn=new_df.get_group('Brooklyn')
Brooklyn_Incidents0907=(Brooklyn['INCIDENTCOUNT'].mean())

Manhattan=new_df.get_group('Manhattan')
Manhattan_Incidents0907=(Manhattan['INCIDENTCOUNT'].mean())

Staten_Island=new_df.get_group('Staten Island')
Staten_Island_Incidents0907=(Staten_Island['INCIDENTCOUNT'].mean())

### Acuqiring the x and y labels and plotting accordingly which will also be repeated in multiple instances
test=pd.DataFrame()
style.use('fivethirtyeight')
test['Boroughs']='Queens','Manhattan','Brooklyn','Bronx','Staten Island'
test['Average Incident Count']=Queens_Incidents0907,Manhattan_Incidents0907,Brooklyn_Incidents0907,Bronx_Incidents0907,Staten_Island_Incidents0907

plt.bar(test['Boroughs'],test['Average Incident Count'],color=['Blue','Red','Purple','Green','Yellow'])
plt.xlabel('Boroughs')
plt.ylabel('Average Incident Count')
plt.title('2009/07 Average Incident/Borough',fontname= 'Freestyle Script',size=25)
plt.show()

Sec_month_year1=df.loc[df['YEARMONTH']=='2009/08']

sorted2=Sec_month_year1.sort_values(by='INCIDENTCOUNT')

new_df2=sorted2.groupby('INCIDENTBOROUGH')

Queens2=new_df2.get_group('Queens')
Queens_Incidents0908=(Queens2['INCIDENTCOUNT'].mean())

Bronx2=new_df2.get_group('Bronx')
Bronx_Incidents0908=(Bronx2['INCIDENTCOUNT'].mean())


Brooklyn2=new_df2.get_group('Brooklyn')
Brooklyn_Incidents0908=(Brooklyn2['INCIDENTCOUNT'].mean())

Manhattan2=new_df2.get_group('Manhattan')
Manhattan_Incidents0908=(Manhattan2['INCIDENTCOUNT'].mean())

Staten_Island2=new_df2.get_group('Staten Island')
Staten_Island_Incidents0908 = (Staten_Island2['INCIDENTCOUNT'].mean())

test2=pd.DataFrame()
style.use('fivethirtyeight')
test2['Boroughs']='Queens','Manhattan','Brooklyn','Bronx','Staten Island'
test2['Average Incident Count']=Queens_Incidents0908,Manhattan_Incidents0908,Brooklyn_Incidents0908,Bronx_Incidents0908,Staten_Island_Incidents0908

plt.bar(test2['Boroughs'],test2['Average Incident Count'],color=['Blue','Red','Purple','Green','Yellow'])
plt.xlabel('Boroughs')
plt.ylabel('Average Incident Count')
plt.title('2009/08 Average Incident/Borough',fontname= 'Freestyle Script',size=25)
plt.show()



Sec_year=df.loc[df['YEARMONTH']=='2010/07']

sorted_year2=Sec_year.sort_values(by='INCIDENTCOUNT')

new_df_year2=sorted_year2.groupby('INCIDENTBOROUGH')

Queens_year2=new_df_year2.get_group('Queens')
Queens_Incidents1007=(Queens_year2['INCIDENTCOUNT'].mean())

Bronx_year2=new_df_year2.get_group('Bronx')
Bronx_Incidents1007=(Bronx_year2['INCIDENTCOUNT'].mean())

Brooklyn_year2=new_df_year2.get_group('Brooklyn')
Brooklyn_Incidents1007=(Brooklyn_year2['INCIDENTCOUNT'].mean())

Manhattan_year2=new_df_year2.get_group('Manhattan')
Manhattan_Incidents1007=(Manhattan_year2['INCIDENTCOUNT'].mean())

Staten_Island_year2=new_df_year2.get_group('Staten Island')
Staten_Island_Incidents1007=(Staten_Island_year2['INCIDENTCOUNT'].mean())


test_Year2=pd.DataFrame()
style.use('fivethirtyeight')
test_Year2['Boroughs']='Queens','Manhattan','Brooklyn','Bronx','Staten Island'
test_Year2['Average Incident Count']=Queens_Incidents1007,Manhattan_Incidents1007,Brooklyn_Incidents1007,Bronx_Incidents1007,Staten_Island_Incidents1007

plt.bar(test_Year2['Boroughs'],test_Year2['Average Incident Count'],color=['Blue','Red','Purple','Green','Yellow'])
plt.xlabel('Boroughs')
plt.ylabel('Average Incident Count')
plt.title('2010/07 Average Incident/Borough',fontname= 'Freestyle Script',size=25)
plt.show()




Sec_year_month2=df.loc[df['YEARMONTH']=='2010/08']

sorted_year2_month2=Sec_year_month2.sort_values(by='INCIDENTCOUNT')

new_df_year2_month2=sorted_year2_month2.groupby('INCIDENTBOROUGH')

Queens_year2_month2=new_df_year2_month2.get_group('Queens')
Queens_Incidents1008=(Queens_year2_month2['INCIDENTCOUNT'].mean())

Bronx_year2_month2=new_df_year2_month2.get_group('Bronx')
Bronx_Incidents1008=(Bronx_year2_month2['INCIDENTCOUNT'].mean())

Brooklyn_year2_month2=new_df_year2_month2.get_group('Brooklyn')
Brooklyn_Incidents1008=(Brooklyn_year2_month2['INCIDENTCOUNT'].mean())

Manhattan_year2_month2=new_df_year2_month2.get_group('Manhattan')
Manhattan_Incidents1008=(Manhattan_year2_month2['INCIDENTCOUNT'].mean())

Staten_Island_year2_month2=new_df_year2_month2.get_group('Staten Island')
Staten_Island_Incidents1008=(Staten_Island_year2_month2['INCIDENTCOUNT'].mean())


test_Year2_month2=pd.DataFrame()
style.use('fivethirtyeight')
test_Year2_month2['Boroughs']='Queens','Manhattan','Brooklyn','Bronx','Staten Island'
test_Year2_month2['Average Incident Count']=Queens_Incidents1008,Manhattan_Incidents1008,Brooklyn_Incidents1008, Bronx_Incidents1008 ,Staten_Island_Incidents1008

plt.bar(test_Year2_month2['Boroughs'],test_Year2_month2['Average Incident Count'],color=['Blue','Red','Purple','Green','Yellow'])
plt.xlabel('Boroughs')
plt.ylabel('Average Incident Count')
plt.title('2010/08 Average Incident/Borough',fontname= 'Freestyle Script',size=25)
plt.show()



"Resources: https://www.lexipol.com/resources/blog/understanding-and-measuring-fire-department-response-times/#:~:text=Alarm%20Processing%20Time%3A%2064%20seconds,80%20seconds%20for%20fire%20responses "
"https://data.cityofnewyork.us/Social-Services/FDNY-Monthly-Response-Times/j34j-vqvt "
'https://en.wikipedia.org/wiki/New_York_City_Fire_Department. '
