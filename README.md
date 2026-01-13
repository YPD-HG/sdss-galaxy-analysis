Exploring Galaxy Properties from the Sloan Digital Sky Survey

This project analyzes real galaxy data from the Sloan Digital Sky Survey (SDSS).
The goal is to study how galaxy brightness, color, and distance (redshift) are related using observational data.

Dataset
The dataset contains 10,000 astronomical objects observed by SDSS.
Each object includes brightness measurements in five optical bands (u, g, r, i, z), a spectroscopic redshift, and a classification.
For this project, only objects classified as GALAXY were used (4,998 galaxies).

Method
The analysis was performed in Python using pandas and matplotlib.
The steps were:
- Load the SDSS catalog
- Filter to galaxies only
- Select photometric magnitudes and redshift
- Compute galaxy colors (u−g and g−r)
- Visualize relationships using scatter plots

Results

1. Brightness vs Redshift  
A plot of r-band brightness against redshift shows that more distant galaxies appear fainter, as expected from cosmological expansion and observational limits.

2. Galaxy Colors  
A color-color diagram (u−g vs g−r) shows a clear galaxy sequence, separating bluer star-forming galaxies from redder older galaxies.

3. Color and Distance  
The correlation between galaxy color and redshift shows that more distant galaxies are slightly redder on average:
- corr(redshift, u−g) ≈ −0.08  
- corr(redshift, g−r) ≈ 0.18  

This reflects known effects of redshift and galaxy evolution.

Conclusion
This project demonstrates how real telescope data from SDSS can be used to explore the physical properties of galaxies using basic data analysis techniques.
It provides a small but realistic example of observational cosmology using public survey data.
