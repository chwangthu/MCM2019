# calculate the correlation between drug reports and socio-economic factors
import pandas as pd
import numpy as np

fac_frame = pd.read_excel("../data/cluster_entropy.xlsx")
rep_frame = pd.read_excel("../data/cluster_drugreports.xlsx")

dg = pd.DataFrame()

corr_whole = []
for i in range(10): # represents 10 clusters
    factors = fac_frame[fac_frame["cluster"].isin([i])].iloc[:, 4:]
    factors = np.array(factors)
    m, n = factors.shape
    # for item in factors:
    #     print(item)
    reports = rep_frame[rep_frame["cluster"].isin([i])].iloc[:7, 3:]
    reports = np.array(reports)
    # print(reports[:, 0])
    corr = []
    for j in range(n):
        column_j = factors[:, j]
        # print(column_i)
        corr.append(np.corrcoef(column_j, reports[:, 0])[0,1])
    corr_whole.append(corr)
    # dg.iloc[i] = corr
    # print(reports)
# dg.to_excel("../data/corr.xls")
corr_whole = np.array(corr_whole)
for i in range(4, len(fac_frame.columns.values)):
    # print(fac_frame.columns.values[0])
    dg[fac_frame.columns.values[i]] = corr_whole[:, i-4]
dg.to_excel("../data/corr.xls")
# print(factors_year)