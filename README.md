# Galaxy Properties and Population Evolution from SDSS

This project analyzes real observational data from the Sloan Digital Sky Survey (SDSS) to study how galaxies differ in brightness, color, distance, and star-formation activity, and how galaxy populations evolve across cosmic time.

The goal is to treat SDSS as a physical survey of the universe and extract real astrophysical trends using data-driven and statistical analysis.

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

## Methods

The SDSS catalog was first filtered to include only objects classified as **GALAXY**.  
Rows with missing or non-physical values in magnitudes or redshift were removed to ensure reliable photometric and distance measurements.

Galaxy colors were computed from the SDSS photometric bands using standard color indices (e.g., **u − r**, **u − g**, **g − r**).

For population and evolution analysis, galaxies were grouped into **redshift bins** of fixed width to trace how average properties change with cosmic time.  
Within each bin, the **mean u − r color** was calculated along with its **standard error**, providing an estimate of the uncertainty in the mean.

To quantify color evolution, a **weighted linear regression** was performed on the binned data, using the inverse variance of each bin as weights.  
This ensures that bins with better statistics have a stronger influence on the fitted relation, producing a physically meaningful estimate of the color–redshift evolution law.

---

## What this project studies

Using galaxy photometry and redshift, this project investigates:

- How galaxy brightness changes with distance  
- How galaxy colors trace stellar populations  
- How galaxies separate into red and blue populations  
- How the relative abundance of these populations evolves with redshift  
- How galaxy star-formation activity changes across cosmic time  
- How fast galaxy properties evolve with redshift using statistical measurements and uncertainty estimates
- How fast galaxy color (and therefore star formation) changes with cosmic time.
- How to quantify galaxy evolution using binned averages, uncertainties, and weighted regression 

This reproduces the core workflow of modern observational galaxy-evolution studies.

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
This reflects differences in stellar age, dust content, and star-formation activity across galaxies.

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

This reproduces the observed decline of cosmic star formation over time.

---

## Quantitative galaxy evolution

A linear regression was fitted to **u − r vs redshift** to measure how galaxy colors evolve quantitatively.

<img width="368" height="49" alt="Screenshot 2026-01-13 at 1 33 56 PM" src="https://github.com/user-attachments/assets/c2636516-33c3-4f63-8e65-ece318653101" />

The fitted slope shows that galaxy color changes systematically with redshift, providing a direct numerical measure of stellar-population evolution.

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
- At low redshift (z ≈ 0), mean u − r ≈ **2.2**  
- At high redshift (z ≈ 0.7), mean u − r ≈ **0.9**

This is a large, systematic shift.  
Because the error bars do not overlap, the trend is **statistically significant**.

Since bluer u − r indicates higher star-formation activity, this directly shows that galaxies in the past were forming stars much more rapidly than galaxies today.

This is a data-driven measurement of the **cosmic star-formation history** from SDSS photometry.

## Measured evolution law

The same binned SDSS data with a weighted fit:

<img width="573" height="451" alt="Screenshot 2026-01-13 at 4 29 52 PM" src="https://github.com/user-attachments/assets/04d5c7a5-8790-41eb-be88-43316f89a1e3" />

This gives the physical law:

**u − r ≈ 2.10 + 0.78 z**

---

## Connection to published astronomy

The statistically significant trends measured in this project are consistent with multiple well-established results in the astronomical literature.

**1. Bimodal color distributions in SDSS galaxies**  
Baldry et al. (2004) used tens of thousands of SDSS galaxies to show that the galaxy color–magnitude distribution can be modeled as two distinct populations (red sequence and blue cloud) across a range of environments. This supports the interpretation of the two populations seen in this project. [https://arxiv.org/abs/astro-ph/0410603]

**2. Redshift evolution of galaxy color and environment**  
Studies using large spectroscopic samples such as the DEEP2 Galaxy Redshift Survey find that the fraction of red galaxies increases toward lower redshift (more recent times), and that color–density relations evolve across cosmic time. This aligns with your measured decrease in mean u − r color with increasing redshift. [https://academic.oup.com/mnras/article/376/4/1445/1013797]

**3. Modeling the color evolution of galaxies**  
Work by Maraston et al. (2008, 2009) on modeling the color evolution of luminous red galaxies in the SDSS shows how observed colors (e.g., g − r) change with redshift and can be matched by population synthesis models. This connects to quantitative color evolution and underlying stellar population changes measured in your project. [https://academic.oup.com/mnrasl/article/394/1/L107/1081702]

**4. Cosmic star-formation history**  
The decline of cosmic star formation with time, which you infer from the changing mean u − r color, matches the broader picture compiled observationally by Madau & Dickinson (2014), showing that the global star-formation rate density peaked at intermediate redshifts and declines toward the present. [https://en.wikipedia.org/wiki/Butcher%E2%80%93Oemler_Effect]

---

## Conclusions

From real SDSS data, this project shows that:

- Distant galaxies appear fainter with increasing redshift, consistent with cosmological expansion and survey sensitivity limits  
- Galaxies separate into two physically distinct populations in color–magnitude space: a blue, star-forming population and a red, passively evolving population  
- These populations reproduce the classical **blue cloud** and **red sequence** seen in professional extragalactic surveys  
- The relative fractions of red and blue galaxies change systematically with redshift, demonstrating that the mix of galaxy types evolves over cosmic time  
- Galaxy colors (u − r) act as a reliable tracer of stellar populations and star-formation activity across the sample  
- The average galaxy color becomes bluer at higher redshift, showing that galaxies in the past were forming stars more actively  
- The mean u − r decreases from about **2.2 at z ≈ 0** to about **0.9 at z ≈ 0.7**  
- This change is **statistically significant**, with non-overlapping uncertainties in the binned averages  
- A weighted regression yields the empirical evolution law  
  **u − r ≈ 2.10 + 0.78 z**,  
  providing a quantitative measurement of how galaxy stellar populations evolve with cosmic time  
- Red and blue galaxies follow different evolutionary tracks, with blue galaxies showing much stronger color evolution than red galaxies  

Together, these results show that the universe has transitioned from a blue, actively star-forming phase to a red, more passive phase as it has aged, reproducing the key observational picture of galaxy evolution seen in large professional surveys.

---

## Why this matters

All results in this project are based on real SDSS telescope observations and the same statistical and photometric techniques used in professional observational cosmology.

By combining galaxy colors, redshifts, population statistics, and weighted regression, this project goes beyond visualization and makes **quantitative measurements of galaxy evolution**.

In particular, measuring an explicit evolution law  
**u − r ≈ 2.10 + 0.78 z**  
demonstrates how large sky surveys can be used to recover the cosmic history of star formation directly from data.

This is the same type of analysis used in modern galaxy surveys to study how galaxies form, evolve, and eventually stop forming stars, making this project a small but authentic example of real extragalactic astronomy in practice.

