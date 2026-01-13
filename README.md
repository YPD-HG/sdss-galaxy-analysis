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
- How fast galaxy properties evolve with redshift using statistical measurements and uncertainty estimates

This reproduces the core workflow of modern observational galaxy evolution studies.

---

## Brightness and distance

A scatter plot of r-band magnitude versus redshift shows that more distant galaxies appear fainter.  
This is consistent with an expanding universe and the sensitivity limits of the SDSS telescope, confirming that the dataset behaves like a real cosmological survey.

<img width="558" height="453" alt="Screenshot 2026-01-13 at 1 59 14 PM" src="https://github.com/user-attachments/assets/609b28d6-82b5-45ca-855b-4c6679b102a5" />

---

## Galaxy colors

<img width="560" height="452" alt="Screenshot 2026-01-13 at 1 49 01 PM" src="https://github.com/user-attachments/assets/45bc593b-1e28-4173-82b7-375f58d4a377" />

Galaxy colors were computed using standard SDSS indices:
- **u − g**
- **g − r**

The color–color diagram (u − g vs g − r) reveals a tight galaxy sequence rather than random scatter.  
This reflects differences in stellar age, dust content, and star formation activity across galaxies.

---

## Galaxy populations

<img width="560" height="449" alt="Screenshot 2026-01-13 at 1 50 40 PM" src="https://github.com/user-attachments/assets/beddd940-cadb-4eb3-a51b-058c56eb4a24" />

This plot shows that galaxies cluster into two main regions in color–magnitude space.

<img width="561" height="452" alt="Screenshot 2026-01-13 at 1 53 21 PM" src="https://github.com/user-attachments/assets/4f645e18-0571-40c0-b460-c99c506be78c" />

The clustering algorithm automatically separated galaxies into two physically distinct populations:

- A **blue, star-forming population**  
- A **red, passively evolving population**

This reproduces the classical **blue cloud** and **red sequence** seen in extragalactic astronomy.

---

## Population evolution

Galaxies were grouped into redshift bins and the fraction of each population was measured.

<img width="565" height="511" alt="Screenshot 2026-01-13 at 1 43 25 PM" src="https://github.com/user-attachments/assets/a8d8e832-860d-483c-aa4c-e73069937fc0" />

This plot shows how the relative fraction of the two galaxy populations changes with redshift.

<img width="244" height="207" alt="Screenshot 2026-01-13 at 1 44 40 PM" src="https://github.com/user-attachments/assets/a9c781cf-c8dd-49d3-a0c5-78d7760c755e" />

As we look farther back in time:
1. One population becomes increasingly dominant  
2. The other gradually fades  

This demonstrates that the mix of galaxy types in the universe evolves across cosmic time.

---

## Star formation history from colors

Star formation was estimated using the **u − r color index**, a standard proxy in observational astronomy.

Lower u − r values correspond to younger, actively star-forming galaxies, while higher values indicate older, passive stellar populations.

<img width="562" height="450" alt="Screenshot 2026-01-13 at 1 38 30 PM" src="https://github.com/user-attachments/assets/66f3ba1f-d9f3-462f-ac28-315f2c4896ad" />

This plot shows that galaxies at higher redshift are systematically bluer, meaning they were forming stars more actively in the early universe.

<img width="253" height="131" alt="Screenshot 2026-01-13 at 1 36 05 PM" src="https://github.com/user-attachments/assets/1356ce13-4068-4d65-8af2-3ce025d8592d" />

Two key results were found:

- The two galaxy populations have significantly different u − r values, confirming that one group is actively forming stars while the other is passive.  
- The mean u − r color decreases with increasing redshift, showing that galaxies were bluer and more star-forming in the past.

This reproduces the observed decline of cosmic star formation with time.

---

## Quantitative galaxy evolution

A linear regression was fitted to **u − r vs redshift** to measure how galaxy colors evolve quantitatively.

<img width="368" height="49" alt="Screenshot 2026-01-13 at 1 33 56 PM" src="https://github.com/user-attachments/assets/c2636516-33c3-4f63-8e65-ece318653101" />

The fitted slope shows that galaxy color changes systematically with redshift, providing a direct numerical measure of stellar population evolution.

When fitted separately for the two galaxy populations:
- One population shows slow color evolution  
- The other shows much stronger evolution  

This demonstrates that red and blue galaxies follow different evolutionary paths.

---

## Statistical measurement of galaxy evolution

Galaxies were grouped into redshift bins and the **mean u − r color** was computed in each bin along with its **statistical uncertainty**.

This allows us to move beyond visual trends and quantitatively measure how galaxy star formation changes with cosmic time.

Each point in the plot below represents the **average galaxy color** in a redshift slice, and the error bars show the **uncertainty in that average**.

<img width="574" height="448" alt="Screenshot 2026-01-13 at 2 45 18 PM" src="https://github.com/user-attachments/assets/6cc2d182-1090-4619-a501-6b52f47b59f7" />

The measured values show:

- At low redshift (z ≈ 0), mean u − r ≈ 2.2

- At high redshift (z ≈ 0.7), mean u − r ≈ 0.9

This is a large, systematic shift.
Because the error bars do not overlap, the trend is statistically significant.

Since bluer u − r means more active star formation, this directly shows that galaxies in the past were forming stars much more rapidly than galaxies today.

This is a direct data driven measurement of cosmic star formation history from SDSS photometry.

## Conclusions

From real SDSS data, this project shows that:

- Distant galaxies appear fainter, consistent with cosmological expansion  
- Galaxies separate into red and blue populations  
- The relative fractions of these populations change with redshift  
- The average galaxy color (u − r) decreases systematically with increasing redshift implying that galaxies were more actively forming stars in the early universe  
- Red and blue galaxies evolve at different rates  
- The mean u − r drops from about 2.2 at z ≈ 0 to about 0.9 at z ≈ 0.7  
- This change is *statistically significant*, with non-overlapping uncertainties  
- Galaxies were therefore forming stars much more actively in the past  

These results are consistent with the modern picture of galaxy evolution.

---

## Why this matters

All results are based on real SDSS telescope observations and standard analysis techniques used in observational cosmology.

This project demonstrates how large sky surveys can be used to extract physical information about galaxy populations and the history of star formation in the universe using data driven methods.
