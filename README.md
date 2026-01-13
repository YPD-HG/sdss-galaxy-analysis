# Galaxy Properties and Population Evolution from SDSS

This project analyzes real observational data from the Sloan Digital Sky Survey (SDSS) to study how galaxies differ in brightness, color, and distance, and how galaxy populations and star formation evolve across cosmic time.

The goal is to treat SDSS as a physical survey of the universe, not just a generic dataset, and to extract real astrophysical trends from galaxy photometry and redshift measurements.

---

## Dataset

The dataset contains 10,000 astronomical objects observed by the Sloan telescope.
Each object includes:
- Brightness in five optical bands (u, g, r, i, z)
- Spectroscopic redshift (a measure of distance)
- Object classification (STAR, GALAXY, QUASAR)

Only objects classified as **GALAXY** were used in this study, giving a final sample of **4,998 galaxies**.

These measurements come directly from SDSS SkyServer and represent real telescope observations.

---

## What this project studies

From galaxy photometry and redshift, astronomers can infer:
- how luminous galaxies are
- how far away they are
- whether their stars are young or old
- how different types of galaxies populate the universe
- how galaxies evolve over cosmic time

In this project we specifically study:
- how galaxy brightness changes with distance
- how galaxy colors trace stellar populations
- how galaxies separate into red and blue populations
- how the fractions of these populations change with redshift
- how star formation activity evolves across cosmic time

---

## Brightness and distance

We first examined how galaxy brightness changes with redshift.

A scatter plot of r-band magnitude versus redshift shows that more distant galaxies appear systematically fainter, as expected from the expansion of the universe and observational limits of the telescope.

This confirms that the SDSS catalog behaves like a real cosmological survey.

---

## Galaxy colors

Galaxy colors were computed using the standard SDSS indices:
- **u − g**
- **g − r**

A color–color diagram (u − g vs g − r) reveals a tight galaxy sequence rather than random scatter.
This reflects physical differences in stellar age, dust content, and star formation activity across galaxies.

---

## Galaxy populations

A color–magnitude diagram (g − r vs r-band brightness) shows that galaxies form two main populations.

Using unsupervised clustering on color and brightness, galaxies were separated into two groups that correspond to:
- a **blue, star-forming population**
- a **red, passive population**

This reproduces the classical **blue cloud** and **red sequence** observed in extragalactic astronomy.

---

## Population evolution

To study how these populations change across cosmic time, galaxies were grouped into redshift bins and the fraction of each population was measured.

The results show a clear trend:
the relative abundance of the two galaxy populations varies systematically with redshift.

At low redshift (the nearby universe), both red and blue galaxies are common.
At higher redshift, one population becomes increasingly dominant.

This indicates that the composition of galaxy types in the universe evolves with time.

---

## Star formation history from colors

Galaxy star formation was estimated using the **u − r color index**, a standard proxy in observational astronomy.

Lower u − r values correspond to bluer, actively star-forming galaxies, while higher values indicate older, passive stellar populations.

Two key results were found:

**1. Validation of galaxy populations**  
The two clustered galaxy populations have significantly different u − r values, confirming that one group is genuinely star-forming while the other is passive.

**2. Evolution with redshift**  
The mean u − r color decreases with increasing redshift.
This means galaxies become bluer at larger distances, indicating higher star formation rates in the early universe.

This reproduces the observed decline of cosmic star formation with time using SDSS photometry alone.

---

## Conclusions

From real SDSS data, this project shows that:

- Distant galaxies appear fainter, as expected in an expanding universe  
- Galaxies form two physically distinct populations (red and blue)  
- The relative fractions of these populations change with redshift  
- Galaxies in the early universe were more actively forming stars than galaxies today  

These results are consistent with the modern picture of galaxy evolution.

---

## Why this matters

All results in this project are based on real SDSS telescope observations and standard analysis techniques used in observational cosmology.

This small study reproduces key features of galaxy populations and their evolution across cosmic time, demonstrating how large sky surveys can be used to understand the physical history of the universe through data driven analysis.
