# Exploring Galaxy Properties and Populations from the Sloan Digital Sky Survey (SDSS)

This project uses real observational data from the Sloan Digital Sky Survey (SDSS) to study the physical and statistical properties of galaxies.  
The goal is to understand how galaxy brightness, color, and distance (redshift) are related, and how different galaxy populations evolve in the universe.

Rather than using SDSS as a generic machine learning table, this project treats it as an astronomical survey, similar to how professional astronomers analyze large sky catalogs.

---

## Dataset

The dataset contains 10,000 astronomical objects observed by the Sloan telescope.  
Each object includes:

- Sky position (RA, DEC)  
- Brightness in five optical bands (u, g, r, i, z)  
- Spectroscopic redshift (distance)  
- Object class (STAR, GALAXY, or QUASAR)  

For this project, only objects classified as **GALAXY** were used, giving a final sample of **4,998 galaxies**.

These measurements come directly from SDSS SkyServer and represent real telescope observations.

---

## What we want to learn

Modern astronomy is built on large sky surveys like SDSS.  
From simple measurements of brightness and color, astronomers can infer:

- How far galaxies are  
- How old their stars are  
- Whether galaxies are actively forming stars or are already “dead”  
- How galaxy populations change across cosmic time  

This project explores these ideas step by step using real data.

---

## Step 1: Galaxy brightness and distance

The first question is very basic:

**Do more distant galaxies look fainter?**

To test this, we plotted the r-band brightness of galaxies against their redshift (a measure of distance).

This plot shows a clear trend:
- Most galaxies are nearby at low redshift  
- A small number are much farther away  
- Distant galaxies appear fainter on average  

This is exactly what is expected from the expansion of the universe and the limits of telescope sensitivity.

---

## Step 2: Galaxy colors

Galaxies are not just bright or faint. Their color tells us about their stars.

We computed two standard astronomical color indices:

- **u − g**  
- **g − r**

These measure how blue or red a galaxy is.

When we plot **u − g vs g − r**, galaxies fall along a tight sequence rather than being randomly scattered.  
This is known as the **galaxy color sequence**, and it reflects differences in stellar age, dust, and star formation activity.

---

## Step 3: Color and distance

We then asked:

**Do distant galaxies look different in color than nearby ones?**

By measuring correlations between color and redshift, we found:

- corr(redshift, u − g) ≈ −0.08  
- corr(redshift, g − r) ≈ +0.18  

This shows that galaxies at higher redshift are slightly redder on average in g − r, consistent with known effects of redshift and galaxy evolution.

---

## Step 4: Galaxy populations (red vs blue)

One of the most important discoveries in modern astronomy is that galaxies fall into two main populations:

- **Blue cloud**: young, star-forming galaxies  
- **Red sequence**: old, passive galaxies  

To study this, we built a **color-magnitude diagram** (g − r vs r-band brightness).  
This diagram shows two overlapping but distinct galaxy populations.

To separate them automatically, we applied a simple clustering algorithm (K-Means) using galaxy color and brightness.  
This split the galaxies into two groups that closely match the red and blue populations seen in astronomy.

---

## Step 5: Galaxy evolution

Finally, we asked:

**Do red and blue galaxies live at different distances?**

By comparing their mean redshifts, we found:

- One population has a mean redshift ≈ 0.088  
- The other has a mean redshift ≈ 0.069  

The bluer, star-forming galaxies extend to higher redshift, while the redder, older galaxies are more common nearby.  
This matches what astronomers know about galaxy evolution: the universe used to have more actively star-forming galaxies, and many have since evolved into red, passive systems.

---

## Why this matters

This project shows how simple photometric measurements from a large sky survey can be used to study:

- The structure of the universe  
- The distribution of galaxies  
- The life cycle of galaxies across cosmic time  

All results here come from real SDSS telescope data and use the same types of plots and techniques found in observational cosmology research.

This notebook is meant to be a small but realistic example of how modern astronomy is done with data.
