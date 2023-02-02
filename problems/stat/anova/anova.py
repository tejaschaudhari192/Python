# Importing library
from scipy.stats import f_oneway

# Performance when each of the engine
# oil is applied
performance1 = [89, 89, 88, 78, 79]
performance2 = [93, 92, 94, 89, 88]
performance3 = [89, 88, 89, 93, 90]
performance4 = [81, 78, 81, 92, 82]

# Conduct the one-way ANOVA
f_oneway(performance1, performance2, performance3, performance4)






# Importing libraries
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Create a dataframe
dataframe = pd.DataFrame({'Fertilizer': np.repeat(['daily', 'weekly'], 15),
						'Watering': np.repeat(['daily', 'weekly'], 15),
						'height': [14, 16, 15, 15, 16, 13, 12, 11,
									14, 15, 16, 16, 17, 18, 14, 13,
									14, 14, 14, 15, 16, 16, 17, 18,
									14, 13, 14, 14, 14, 15]})


# Performing two-way ANOVA
model = ols('height ~ C(Fertilizer) + C(Watering) +\
C(Fertilizer):C(Watering)',
			data=dataframe).fit()
result = sm.stats.anova_lm(model, type=2)

# Print the result
print(result)
