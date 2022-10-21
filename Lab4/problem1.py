import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd
import pymc3 as pm
import arviz as az

model = pm.Model()

alpha = 6

with model:
    clienti = pm.Poisson('C', 20)

    statieGatit = np.exp('SG', alpha)
