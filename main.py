import pandas as pd
import matplotlib.pyplot as plt
import DataFunctions


importdata = pd.read_excel("importsandexports.xlsx","Import")
exportdata = pd.read_excel("importsandexports.xlsx","Export")


DataFunctions.TurkeyGeneral(importdata,exportdata)


donotclose = input("_")
#print(importdata)
#print(exportdata)