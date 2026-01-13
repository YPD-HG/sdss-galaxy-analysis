# Galaxy Properties and Population Evolution from SDSS

This project analyzes real observational data from the Sloan Digital Sky Survey (SDSS) to study how galaxies differ in brightness, color, and distance, and how galaxy populations evolve across cosmic time.

The goal is to treat SDSS as an astronomical survey, not just a generic dataset, and extract physically meaningful trends about the universe.

---

## Dataset

The dataset contains 10,000 astronomical objects observed by the Sloan telescope.
Each object includes:
- Brightness in five optical bands (u, g, r, i, z)
- Spectroscopic redshift (a measure of distance)
- Object classification (STAR, GALAXY, QUASAR)

For this project, only objects classified as **GALAXY** were used, giving a final sample of **4,998 galaxies**.

---

## What we study

From basic photometric measurements, astronomers can infer:
- How far galaxies are
- Whether they contain young or old stars
- How galaxy populations change as the universe ages

This project explores these ideas using simple but real astronomical analysis.

---

## Brightness and distance

We first examined how galaxy brightness changes with redshift.
A scatter plot of r-band magnitude versus redshift shows that more distant galaxies appear fainter, as expected from the expansion of the universe and observational limits.

This confirms that the dataset behaves like a real cosmological sample.

---

## Galaxy colors

Galaxy colors were computed using:
- **u − g**
- **g − r**

A color color diagram (u − g vs g − r) reveals a tight galaxy sequence, reflecting differences in stellar age, dust, and star formation activity.

---

## Galaxy populations

A color magnitude diagram (g − r vs r-band brightness) shows that galaxies form two main populations.
Using unsupervised clustering, these were separated into two groups that correspond to:
- A red, older population
- A blue, star forming population

This reproduces the well known red sequence and blue cloud seen in extragalactic astronomy.

---

## Population evolution

To study how galaxies change across cosmic time, galaxies were grouped into redshift bins and the fraction of each population was measured.

The results show a clear trend:
the relative fractions of the two galaxy populations vary systematically with redshift.

This indicates that the mix of galaxy types in the universe changes over time, consistent with the picture that galaxies evolve from active, star forming systems into older, redder systems.

---

## Why this matters

All results in this project come from real SDSS telescope data and use the same types of plots and techniques used in professional observational astronomy.

This small study demonstrates how large sky surveys can be used to explore galaxy structure, color, and evolution using data driven methods.
