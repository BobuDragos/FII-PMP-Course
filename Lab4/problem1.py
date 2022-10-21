import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymc3 as pm
import arviz as az

model = pm.Model()

with model:
    clienti = pm.Poisson('C', 20)

    statieGatit = pm.exp('SG', 6)
    