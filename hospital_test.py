import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import f_oneway, ttest_rel, ttest_ind, chi2_contingency

df = pd.read_csv('cleanedData.csv')

#rating bins for chi test, cut() segments and sorts data into the bins 
df['Overall Rating_Bin'] = pd.cut(df['Overall Rating'],
                              bins= [1,2,3,4,5],
                              labels=['Low (1-2)','Medium (3)','High (4)','Best (5)'])


print("ANOVA test:")

state_groups = [ group['Overall Rating'].dropna().values
                for name, group in df.groupby('State')
                if len(group['Overall Rating']) >= 3]

if len(state_groups) >= 2:
    f_stat, p_val = f_oneway(*state_groups)
    print(f'pvalue: {p_val:.10f}') #can be displayed with p_val:.2e to show how small the value is






