import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import f_oneway, ttest_rel, ttest_ind, chi2_contingency

df = pd.read_csv('cleanedData.csv')
summary_results = []

#rating bins for chi test, cut() segments and sorts data into the bins 
df['Overall Rating_Bin'] = pd.cut(df['Overall Rating'],
                              bins= [1,2,3,4,5],
                              labels=['Low (1-2)','Medium (3)','High (4)','Best (5)'])


print("\nANOVA test:")

state_groups = [ group['Overall Rating'].dropna().values
                for name, group in df.groupby('State')
                if len(group['Overall Rating']) >= 3]

if len(state_groups) >= 2:
    f_stat, p_val = f_oneway(*state_groups)
    #print(f'pvalue: {p_val:.10e}') can be displayed with p_val:.2e to show how small the value is
    summary_results.append(
        {
            'Test': 'ANOVA',
            'Comparison': 'Ratings cross states',
            'Test Statistics': f'F= {f_stat:.4f}',
            'P-Value': f'{p_val:.4f}',
            'Significant': 'Yes' if p_val < 0.05 else 'No'
        }
    )


print("\nPaired T-test:")

paired_data = df.dropna(subset=['Cost of Heart Attack Procedure','Cost of Heart Failure Procedure'])
 
if len(paired_data)> 0:
    t_stat, p_val = ttest_rel(paired_data['Cost of Heart Attack Procedure'], 
                              paired_data['Cost of Heart Failure Procedure'])
    
    mean_diff = (paired_data['Cost of Heart Attack Procedure']-paired_data['Cost of Heart Failure Procedure']).mean()
    # print(f"mean cost difference: ${mean_diff:,.4f}")
    # print(f'pvalue: {p_val:.10e}')
    summary_results.append(
        {
            'Test': 'Paired T-test',
            'Comparison': 'Cost of Heart Attack Procedure compared to Heart Failure Procedure per hospital',
            'Test Statistics': f't= {t_stat:.4f}',
            'P-Value': f'{p_val:.4f}',
            'Significant': 'Yes' if p_val < 0.05 else 'No'
        }
    )

print('\nTwo-Sample T-test:')

#statecounts order the states in descending order to then get the top two states with the most hospitals
state_counts = df['State'].value_counts()
top_states = state_counts.head(2).index.tolist()

#if there are moe than two states topstates, map them to state 1 and 2 
#filters rows so only the states matching state 1 and 2 are selected then select col
if len(top_states) >= 2:
    state1, state2 = top_states[0], top_states[1]
    costs_state1 = df[df['State'] == state1]['Cost of Heart Attack Procedure'].dropna()
    costs_state2 = df[df['State'] == state2]['Cost of Heart Attack Procedure'].dropna()

    if len(costs_state1) > 0 and len(costs_state2) > 0:
        t_stat, p_val = ttest_ind(costs_state1,costs_state2, equal_var=False) # tells test not to assume the states have the same varience, spread of values
        #print(f'pvalue: {p_val:.4f}')
        summary_results.append(
        {
            'Test': 'Two-Sample T-test',
            'Comparison': f'Cost of Heart Attack Procedure: {state1} vs {state2}',
            'Test Statistics': f't= {t_stat:.4f}',
            'P-Value': f'{p_val:.4f}',
            'Significant': 'Yes' if p_val < 0.05 else 'No'
        }
    )

print('\nChi-square test:')

contingency = pd.crosstab(df['Overall Rating_Bin'], df['State']) 
filtered_contin = contingency.loc[:, contingency.sum(axis=0) >= 5] #axis0 means go down the rows
print(filtered_contin) #frequency table

if filtered_contin.shape[1] >= 2:
    chi2_stat, p_val, dof, expected = chi2_contingency(filtered_contin)
    # print(f'chi stats: {chi2_stat:.4f}')
    # print(f'degrees of freedom: {dof}')
    # print(f'pvalue: {p_val:.2e}')
    summary_results.append(
        {
            'Test': 'Chi-Square Test',
            'Comparison': 'Ratings vs State comparison',
            'Test Statistics': f'χ²= {chi2_stat:.4f}',
            'P-Value': f'{p_val:.4f}',
            'Significant': 'Yes' if p_val < 0.05 else 'No'
        }
    )

summary_df = pd.DataFrame(summary_results)
#summary_df.to_csv('hypothesisTest_summary', index=False)