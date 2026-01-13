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

<img width="560" height="452" alt="Screenshot 2026-01-13 at 1 49 01 PM" src="https://github.com/user-attachments/assets/45bc593b-1e28-4173-82b7-375f58d4a377" />

Galaxy colors were computed using standard SDSS indices:
- **u − g**
- **g − r**

A color–color diagram (u − g vs g − r) reveals a tight galaxy sequence rather than random scatter, reflecting differences in stellar age, dust, and star formation.

---

## Galaxy populations

<img width="560" height="449" alt="Screenshot 2026-01-13 at 1 50 40 PM" src="https://github.com/user-attachments/assets/beddd940-cadb-4eb3-a51b-058c56eb4a24" />

This below graph tells us tha the universe contains two fundamentally different kinds of galaxies.
<img width="561" height="452" alt="Screenshot 2026-01-13 at 1 53 21 PM" src="https://github.com/user-attachments/assets/4f645e18-0571-40c0-b460-c99c506be78c" />

A color–magnitude diagram (g − r vs r-band magnitude) shows two distinct galaxy populations.

Using unsupervised clustering, galaxies were separated into:
- a **blue, star forming population**
- a **red, passively evolving population**

This reproduces the classical **blue cloud** and **red sequence** seen in extragalactic astronomy.

---

## Population evolution

Galaxies were grouped into redshift bins and the fraction of each population was measured.

<img width="565" height="511" alt="Screenshot 2026-01-13 at 1 43 25 PM" src="https://github.com/user-attachments/assets/a8d8e832-860d-483c-aa4c-e73069937fc0" />

The above graph shows as redshift increases, one galaxy population becomes more dominant and the other fades out.
In other words, the mix of galaxies in the universe changes with cosmic time.

<img width="244" height="207" alt="Screenshot 2026-01-13 at 1 44 40 PM" src="https://github.com/user-attachments/assets/a9c781cf-c8dd-49d3-a0c5-78d7760c755e" />

As you go farther back in time:
1. One population becomes dominant
2. The other fades away

The relative abundance of the two populations varies systematically with redshift, demonstrating that the mix of galaxy types changes across cosmic time.

---

## Star formation history from colors

Star formation was estimated using the **u − r color index**, a standard proxy in observational astronomy.

Lower u − r values correspond to younger, star forming galaxies, while higher values indicate older, passive stellar populations.

<img width="562" height="450" alt="Screenshot 2026-01-13 at 1 38 30 PM" src="https://github.com/user-attachments/assets/66f3ba1f-d9f3-462f-ac28-315f2c4896ad" />

The above graph tells us that the galaxies in the distant universe were bluer and more actively forming stars than galaxies today.

<img width="253" height="131" alt="Screenshot 2026-01-13 at 1 36 05 PM" src="https://github.com/user-attachments/assets/1356ce13-4068-4d65-8af2-3ce025d8592d" />

Two key results were found:

- The two galaxy populations have significantly different u − r values, confirming that one group is genuinely star forming while the other is passive.  
- The mean u − r color decreases with increasing redshift, showing that galaxies were bluer and more actively forming stars in the early universe.

This reproduces the observed decline of cosmic star formation with time.

---

## Quantitative galaxy evolution

A linear regression was fitted to **u − r vs redshift** to measure how galaxy colors evolve.

<img width="368" height="49" alt="Screenshot 2026-01-13 at 1 33 56 PM" src="https://github.com/user-attachments/assets/c2636516-33c3-4f63-8e65-ece318653101" />

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
