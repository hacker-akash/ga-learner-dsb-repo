# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
#Code starts here 
data['Gender'].replace('-', 'Agender', inplace = True)
gender_count = data.Gender.value_counts()
plt.bar(gender_count, gender_count.index)


# --------------
#Code starts here
alignment = data.Alignment.value_counts()
plt.pie(alignment)


# --------------
#Code starts here
sc_df = data[['Strength', 'Combat']].copy()
sc_covariance = sc_df.cov().iloc[0,1]
sc_strength = sc_df.Strength.std()
sc_combat = sc_df.Combat.std()
sc_pearson = sc_covariance/(sc_strength * sc_combat)
ic_df = data[['Intelligence', 'Combat']].copy()
ic_covariance = ic_df.cov().iloc[0,1]
ic_intelligence = ic_df.Intelligence.std()
ic_combat = ic_df.Combat.std()
ic_pearson = ic_covariance/(ic_intelligence * ic_combat)
print("Pearson's correlation coefficient between Strength & Combat: ", sc_pearson)
print("Pearson's correlation coefficient between Intelligence & Combat: ", ic_pearson)


# --------------
#Code starts here
total_high = data["Total"].quantile(q = 0.99)
super_best = data[data['Total']>total_high]
super_best_names = list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here

#Setting up the subplots
fig, (ax_1, ax_2,ax_3) = plt.subplots(1,3, figsize=(20,8))

#Plotting box plot
ax_1.boxplot(super_best['Intelligence'])

#Setting the subplot axis title
ax_1.set(title='Intelligence')


#Plotting box plot
ax_2.boxplot(super_best['Speed'])

#Setting the subplot axis title
ax_2.set(title='Speed')


#Plotting box plot
ax_3.boxplot(super_best['Power'])

#Setting the subplot axis title
ax_3.set(title='Power')

#Code ends here   


