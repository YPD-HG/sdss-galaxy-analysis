# Galaxy Properties and Population Evolution from SDSS

This project analyzes real observational data from the Sloan Digital Sky Survey (SDSS) to study how galaxies differ in brightness, color, distance, and star formation activity, and how galaxy populations evolve across cosmic time.

The goal is to treat SDSS as a physical survey of the universe and extract real astrophysical trends using data driven analysis.

---

## Dataset

The dataset contains 10,000 astronomical objects observed by the Sloan telescope.
Each object includes:
- Photometric brightness in five bands (u, g, r, i, z)
- Spectroscopic redshift (a measure of cosmic distance)
- Object classification (STAR, GALAXY, QUASAR)

Only objects classified as **GALAXY** were used, producing a final sample of **4,998 galaxies**.

All measurements come from real SDSS telescope observations.

---

## What this project studies

Using galaxy photometry and redshift, this project investigates:

- How galaxy brightness changes with distance  
- How galaxy colors trace stellar populations  
- How galaxies separate into red and blue populations  
- How the relative abundance of these populations evolves with redshift  
- How galaxy star formation changes across cosmic time  
- How fast these changes occur quantitatively  

This reproduces the core workflow of modern observational galaxy evolution studies.

---

## Brightness and distance

A scatter plot of r-band magnitude versus redshift shows that more distant galaxies appear fainter.
This is consistent with an expanding universe and the sensitivity limits of the SDSS telescope, confirming that the dataset behaves like a real cosmological survey.

---

## Galaxy colors

Galaxy colors were computed using standard SDSS indices:
- **u − g**
- **g − r**

A color–color diagram (u − g vs g − r) reveals a tight galaxy sequence rather than random scatter, reflecting differences in stellar age, dust, and star formation.

---

## Galaxy populations

A color–magnitude diagram (g − r vs r-band magnitude) shows two distinct galaxy populations.

Using unsupervised clustering, galaxies were separated into:
- a **blue, star forming population**
- a **red, passively evolving population**

This reproduces the classical **blue cloud** and **red sequence** seen in extragalactic astronomy.

---

## Population evolution

Galaxies were grouped into redshift bins and the fraction of each population was measured.

The relative abundance of the two populations varies systematically with redshift, demonstrating that the mix of galaxy types changes across cosmic time.

---

## Star formation history from colors

Star formation was estimated using the **u − r color index**, a standard proxy in observational astronomy.

Lower u − r values correspond to younger, star forming galaxies, while higher values indicate older, passive stellar populations.

Two key results were found:

- The two galaxy populations have significantly different u − r values, confirming that one group is genuinely star forming while the other is passive.  
- The mean u − r color decreases with increasing redshift, showing that galaxies were bluer and more actively forming stars in the early universe.

This reproduces the observed decline of cosmic star formation with time.

---

## Quantitative galaxy evolution

A linear regression was fitted to **u − r vs redshift** to measure how galaxy colors evolve.

The slope shows that galaxy color changes systematically with redshift, providing a quantitative measurement of stellar population evolution.

When fitted separately for the two galaxy populations:
- One population shows slow color evolution  
- The other shows much stronger color evolution  

This demonstrates that red and blue galaxies follow different evolutionary paths, a key result in galaxy evolution studies.

---

## Conclusions

From real SDSS data, this project shows that:

- Distant galaxies appear fainter, consistent with cosmological expansion  
- Galaxies separate into red and blue populations  
- The fractions of these populations change with redshift  
- Galaxies were more actively forming stars in the early universe  
- Red and blue galaxies evolve at different rates  

These results are consistent with the modern picture of galaxy evolution.

---

## Why this matters

All results are based on real SDSS telescope observations and standard analysis techniques used in observational cosmology.

This project demonstrates how large sky surveys can be used to extract physical information about galaxy populations and the history of star formation in the universe using data driven methods.
