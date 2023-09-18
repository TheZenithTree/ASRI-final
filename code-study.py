import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


homeless = pd.read_csv('/content/gdrive/MyDrive/HUD-homeless-data.csv')
#newHUD = pd.read_excel('/content/gdrive/MyDrive/2007-2022-PIT-Counts-by-State.xlsx')
type(homeless) #Not defining type, just looking at what type it is
homeless.isnull().sum()
#Each subset is its own dataframe

anti_col = ["FL", "TX", "GA", "AL", "MS", "TN", "KY", "IN", "AR", "MO", "IA", "OK", "KS", "NE", "SD", "ND", "MT", "ID", "UT", "Year"]
pro_col = ["CO", "CA", "MD", "WA", "OR", "NM", "HI", "MN", "IL", "VT", "MA", "CT", "NJ", "Year"]

anti_col.sort()
pro_col.sort()

# 1:9

### :, columns
# : selects everything
subset_anti = homeless.loc[(homeless["Metric"] == "Overall Homeless - Transgender"), anti_col]

subAnt_cols = list(subset_anti.select_dtypes(include='object').columns)
for i in subAnt_cols:
  subset_anti[i] = subset_anti[i].apply(str)
  subset_anti[i] = subset_anti[i].str.replace(',', '').astype(float)


subset_pro = homeless.loc[(homeless["Metric"] == "Overall Homeless - Transgender"), pro_col]
subPro_cols = list(subset_pro.select_dtypes(include='object').columns)
for j in subPro_cols:
  subset_pro[j] = subset_pro[j].apply(str)
  subset_pro[j] = subset_pro[j].str.replace(',', '').astype(float)

plt.title("Overall Homeless Trans People in Anti-Trans States")
plt.xlabel("Year")
plt.ylabel("Number of Homeless Trans People per State")
plt.plot(subset_anti["Year"], subset_anti[anti_col[0 : 19]]) #Worked

plt.title("Overall Homeless Trans People in Pro-Trans States")
plt.xlabel("Year")
plt.ylabel("Number of Homeless Trans People per State")
plt.plot(subset_pro["Year"], subset_pro[pro_col[1 : 13 ]]) #Worked

subset_anti_Overall = homeless.loc[(homeless["Metric"] == "Overall Homeless"), anti_col]
subAntAll_cols = list(subset_anti_Overall.select_dtypes(include='object').columns)
for i in subAntAll_cols:
  subset_anti_Overall[i] = subset_anti_Overall[i].apply(str)
  subset_anti_Overall[i] = subset_anti_Overall[i].str.replace(',', '').astype(float)

subset_pro_Overall = homeless.loc[(homeless["Metric"] == "Overall Homeless"), pro_col]
subProAll_cols = list(subset_pro_Overall.select_dtypes(include='object').columns)
for j in subProAll_cols:
  subset_pro_Overall[j] = subset_pro_Overall[j].apply(str)
  subset_pro_Overall[j] = subset_pro_Overall[j].str.replace(',', '').astype(float)

