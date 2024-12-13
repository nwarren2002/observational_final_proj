# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:20:35 2024

@author: naiya
"""

import pint
import matplotlib.pyplot as plt
import astropy.units as u
import numpy as np
from pint.models import get_model_and_toas
from pint.fitter import WLSFitter
from pint.residuals import Residuals

# Load .par and .tim files
parfile = "C:/Users/naiya/Downloads/J1643-1224_PINT_20220305.nb.par"
timfile = "C:/Users/naiya/Downloads/J1643-1224.Rcvr1_2.GUPPI.15y.x.nb.tim"

model, toas = get_model_and_toas(parfile, timfile)
model.find_empty_masks(toas, freeze=True)

# Weighted least squares fit
fitter = WLSFitter(toas, model)
fitter.fit_toas()

# Calculate residuals
resids = Residuals(toas, fitter.model).time_resids.to(u.us)

# Outliers 
threshold = 200  # Threshold in µs
mask = np.abs(resids.value) < threshold

# Filter TOAs and residuals
filtered_toas = toas[mask]

# Refit the model with filtered TOAs
fitter_filtered = WLSFitter(filtered_toas, model)
fitter_filtered.fit_toas()

# Calculate residuals for filtered TOAs
resids_filtered = Residuals(filtered_toas, fitter_filtered.model).time_resids.to(u.us)

# Plot the filtered residuals
plt.figure(figsize=(10, 6))
plt.errorbar(filtered_toas.get_mjds(), resids_filtered.value, yerr=filtered_toas.get_errors().to(u.us).value, fmt='o')
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('MJD')
plt.ylabel('Residual (µs)')
plt.title('Pulsar Timing Residuals (Outliers Removed)')
plt.grid(True)
plt.show()

#Investigating the spike right before MJD 56000
subset_mask = (filtered_toas.get_mjds().value > 55500) & (filtered_toas.get_mjds().value < 56500)
subset_toas = filtered_toas[subset_mask]
resids_subset = Residuals(subset_toas, fitter_filtered.model).time_resids.to(u.us)

plt.figure(figsize=(10, 6))
plt.errorbar(subset_toas.get_mjds(), resids_subset.value, yerr=subset_toas.get_errors().to(u.us).value, fmt='o')
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('MJD')
plt.ylabel('Residual (µs)')
plt.title('Residuals Between MJD 55500 and 56500')
plt.grid(True)
plt.show()

