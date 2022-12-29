plt.figure(figsize=(10, 5))
plt.title("Gender Distribution")
plt.pie(gender_counts, labels=gender_counts.index)

part = womenOlympics.groupby('Year')['Sex'].value_counts()
plt.figure(figsize=(20,10))
part.loc[:, 'F'].plot()
plt.title('Plot of Female Athletes Over Time')