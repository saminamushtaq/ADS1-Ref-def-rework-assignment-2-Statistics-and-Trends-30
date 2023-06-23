#Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats


#Defining a function to read file and take the transpose
def read_files(file1, file2):
    
    """ Reads csv file, converts the csv file to pandas dataframe,
    takes transpose of that dataframe and finally prints the headers 
    of the given data
    """
    
    file1 = pd.read_csv(f"{file1}.csv")
    file1 = file1.drop(['Country Code', 'Indicator Code'],axis=1)
    file2 = file1.transpose()
    print("Original Data Frame header")
    print(file1.head)
    print(file1.columns)
    
    return file1, file2

#Giving the parameters to the function
df_countries, df_countries_tr = read_files("API_19_DS2_en_csv_v2_5552390",
                                   "API_19_DS2_en_csv_v2_5552390")


#getting uae n20 emission data
df_uae = df_countries[df_countries["Country Name"] == "United Arab Emirates"]
df_n2o = df_uae[df_uae['Indicator Name']=="Nitrous oxide emissions (thousand metric tons of CO2 equivalent)"].transpose()
df_n2o = df_n2o.drop(["Country Name", "Indicator Name"])

# drop nan values
df_n2o=df_n2o.dropna().transpose()


#Creating dataframes for analysis
UAE = pd.DataFrame()
UAE["N2O emissions"] = df_n2o.iloc[0]
UAE["N2O emissions"] = pd.to_numeric(UAE["N2O emissions"])

df_methane = df_uae[df_uae['Indicator Name']=="Methane emissions (kt of CO2 equivalent)"].transpose()
df_methane = df_methane.drop(["Country Name", "Indicator Name"])

# drop nan values
df_methane=df_methane.dropna().transpose()

#adding column to UAE dataframe
UAE["Methane emissions"] = df_methane.iloc[0]
UAE["Methane emissions"] = pd.to_numeric(UAE["Methane emissions"])

df_co2 = df_uae[df_uae['Indicator Name']=="CO2 emissions (kt)"].transpose()
df_co2 = df_co2.drop(["Country Name", "Indicator Name"])

# drop nan values
df_co2 = df_co2.dropna().transpose()

#adding column to UAE dataframe
UAE["CO2 emissions"] = df_co2.iloc[0]
UAE["CO2 emissions"] = pd.to_numeric(UAE["CO2 emissions"])

df_greenhouse = df_uae[df_uae["Indicator Name"] == "Total greenhouse gas emissions (kt of CO2 equivalent)"]
df_greenhouse = df_greenhouse.drop(["Country Name", "Indicator Name"], axis = 1)
df_greenhouse = df_greenhouse.transpose()

# drop nan values
df_greenhouse = df_greenhouse.dropna().transpose()

#adding column to UAE dataframe
UAE["Total greenhouse gas emissions"] = df_greenhouse.iloc[0]
UAE["Total greenhouse gas emissions"] = pd.to_numeric(UAE["Total greenhouse gas emissions"])

df_arabel = df_uae[df_uae["Indicator Name"] == "Arable land (% of land area)"]
df_arabel = df_arabel*100
df_arabel = df_arabel.drop(["Country Name", "Indicator Name"], axis = 1)
df_arabel = df_arabel.transpose()

# drop nan values
df_arabel = df_arabel.dropna().transpose()

#adding column to dataframe
UAE["Arable land"] = df_arabel.iloc[0]
UAE["Arable land"] = pd.to_numeric(UAE["Arable land"])


#Reseting the index column from years 
UAE = UAE.reset_index(level=0)
UAE = UAE.rename(columns = {"index":"Year"})

#Converting Year column to datetime object
UAE["Year"] = pd.to_datetime(UAE["Year"])


#Applying statistical tools to the data frame
print("Covariance")
print(UAE.cov())
print("Correlation")
correlation_M = UAE.corr()
print(correlation_M)

#Line plot
plt.figure()
plt.plot(UAE["Year"], UAE["N2O emissions"], 
          label = "N2O")
plt.plot(UAE["Year"], UAE["Methane emissions"], 
          label = "Methane")
plt.plot(UAE["Year"], UAE["CO2 emissions"], 
          label = "CO2")
plt.plot(UAE["Year"], UAE["Total greenhouse gas emissions"], 
         label = "Total greenhouse gases")
plt.plot(UAE["Year"], UAE["Arable land"], 
         label = "Arabel land")
plt.xlabel("Year")
plt.title("UAE")
plt.legend()
plt.savefig("UAE")
plt.show()








