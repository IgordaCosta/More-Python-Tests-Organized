import pandas





TableYXILocation = ['0.0.2.0.1', '0.0.3.0.1', '0.0.4.0.1', '0.0.5.0.1', '0.0.6.0.1', '0.0.7.0.1', '0.0.8.0.1', '0.0.9.0.1', '0.1.3.0.1', '0.1.4.0.1', '0.1.5.0.1', '0.1.6.0.1', '0.1.7.0.1', '0.1.8.0.1', '0.1.9.0.1', '0.2.1.0.1', '0.2.2.0.1', '0.2.3.0.1', '0.2.5.0.1', '0.2.6.0.1', '0.2.7.0.1', 
'0.2.9.0.1', '0.3.0.3.20.0.3.0.10.0.12.0.16', '0.3.0.10.20.0.3.0.10.0.12.0.16', '0.3.0.12.20.0.3.0.10.0.12.0.16', '0.3.0.16.20.0.3.0.10.0.12.0.16', '0.3.1.3.20.0.3.0.10.0.12.0.16', '0.3.1.10.20.0.3.0.10.0.12.0.16', '0.3.1.12.20.0.3.0.10.0.12.0.16', '0.3.1.16.20.0.3.0.10.0.12.0.16', '0.3.2.3.20.0.3.0.10.0.12.0.16', '0.3.2.10.20.0.3.0.10.0.12.0.16', '0.3.2.12.20.0.3.0.10.0.12.0.16', '0.3.2.16.20.0.3.0.10.0.12.0.16', '0.3.3.0.1', '0.3.4.0.1', '0.3.5.0.1', '0.3.7.0.1', '0.3.8.0.1', '0.3.9.0.1', '1.0.2.0.1', '1.0.3.0.1', '1.0.4.0.1', '1.0.5.0.1', 
'1.0.6.0.1', '1.0.7.0.1', '1.0.8.0.1', '1.0.9.0.1', '1.1.3.0.1', '1.1.4.0.1', '1.1.5.0.1', '1.1.6.0.1', '1.1.7.0.1', '1.1.8.0.1', '1.1.9.0.1', '6.0.0.0.1', '6.4.4.0.1']



print('len(TableYXILocation):', str(len(TableYXILocation)))



TableYXILocationPandas= pandas.Series(TableYXILocation).unique()

print('TableYXILocationPandas bellow :')

print(TableYXILocationPandas)

# TableYXILocationPandasUnique = TableYXILocationPandas.unique()


print('len(TableYXILocationPandasUnique): ', str(len(TableYXILocationPandas)))


