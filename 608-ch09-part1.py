#Program Name: 608-ch09-part1.py
#Assignment Module 6
#Class 44680 Block 44599 Section 01
#Michael Baumli
#Date: 20210613


#Imports Section
import csv
from functools import total_ordering
import urllib
import pandas as pd
from pandas.core.frame import DataFrame
'''/
with open('accounts.csv', mode='w', newline='') as accounts:
    writer = csv.writer(accounts)
    writer.writerow([100,'Jones', 24.98])
    writer.writerow([200,'Doe', 345.67])
    writer.writerow([300,'White', 0.00])
    writer.writerow([400,'Stone', -42.16])
    writer.writerow([500,'Rich', 224.62])

with open('accounts.csv', mode='r', newline = '') as accounts:
    print(f'{"Account":>10}{"Name":>10}{"Balance":>10}')
    reader = csv.reader(accounts)
    for record in reader:
        account,name,balance = record
        print(f'{account:>10}{name:>10}{balance:>10}')
/'''
#So I am skipping a few steps because why should I mess with manual processes. 
titanicRead = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv')
print(f'{"Name":>15}{"Survived":>10}{"Sex":10}{"Age":>10}{"Class":>10}')
#reader = csv.reader(titanicRead)
#print(len(titanicRead))
total = (len(titanicRead.index))
titanicRead.columns = ['Name','Survived','Sex','Age','Class']
#print(total)
pd.set_option('precision', 2) 
for i in range(total):
    print(f'{titanicRead.Name[i]:<40}{titanicRead.Survived[i]:10}{titanicRead.Sex[i]:<10}{titanicRead.Age[i]:<10}{titanicRead.Class[i]:10}')
    #name,survived,sex,age,travelclass = record
    #print(f'{name:>50}{survived:>10}{sex:>8}{age:>5}{travelclass>6}')

    
#Done just to prove I could
with open('TitanicSurvival.csv', mode='w', newline='') as titanicWrite:
    writer = csv.writer(titanicWrite)
    for i in range(total):
        row2write = titanicRead.Name[i],titanicRead.Survived[i],titanicRead.Sex[i],titanicRead.Age[i],titanicRead.Class[i]
        writer.writerow(row2write)

#Showing head and tail of the file.
print("Showing the head and tail of the file")
print(titanicRead.head())
print(titanicRead.tail())


with open('TitanicSurvivors.csv', mode='w', newline='') as titanicSurvivors:
    for i in range(total):
        if(titanicRead.Survived[i] == 'yes'):
            writer = csv.writer(titanicSurvivors)
            row2write = titanicRead.Name[i],titanicRead.Survived[i],titanicRead.Sex[i],titanicRead.Age[i],titanicRead.Class[i]
            writer.writerow(row2write)
            

titanicFiltered = pd.read_csv('TitanicSurvivors.csv')
print(f'{"Name":>15}{"Survived":>10}{"Sex":10}{"Age":>10}{"Class":>10}')
#reader = csv.reader(titanicRead)
#print(len(titanicRead))
total = (len(titanicFiltered.index))
titanicFiltered.columns = ['Name','Survived','Sex','Age','Class']
#print(total)
pd.set_option('precision', 2) 
for i in range(total):
    print(f'{titanicFiltered.Name[i]:<40}{titanicFiltered.Survived[i]:10}{titanicFiltered.Sex[i]:<10}{titanicFiltered.Age[i]:<10}{titanicFiltered.Class[i]:10}')

print(titanicFiltered.describe())