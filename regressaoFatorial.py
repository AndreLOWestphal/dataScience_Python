import numpy as np
import statsmodels.api as sm

x1 = np.random.normal(size=100)
x2 = np.random.normal(size=100)
x3 = np.random.normal(size=100)
y = 2+3*x1+4*x2+5*x3+np.random.normal(size=100)

x = sm.add_constant(np.column_stack((x1,x2,x3,x1*x2,x1*x3,x2*x3,x1*x2*x3)))

modelo = sm.OLS(y,x).fit()

print(modelo.summary())