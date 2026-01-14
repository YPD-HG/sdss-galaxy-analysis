# Galaxy Population Evolution from the Sloan Digital Sky Survey

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
- How fast galaxy color (and therefore star formation) changes with cosmic time  
- How to quantify galaxy evolution using binned averages, uncertainties, and weighted regression  
- How observational selection effects bias galaxy-evolution measurements  
- How a volume-limited sample recovers the true physical evolution of galaxies
- How blue galaxies evolve and how red galaxies evolve separately inside the volume limited sample

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

This shows that the mix of galaxy types in the universe evolves across cosmic time.

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

The fitted slope shows that galaxy color changes systematically with redshift in the **flux-limited SDSS sample**, providing a direct numerical measure of the observed color evolution.

When the same fit is applied separately to the two galaxy populations, the raw slopes suggest different trends for blue and red galaxies. However, after correcting for selection effects and estimating uncertainties using bootstrap resampling, neither population shows a statistically significant color–redshift slope in the **volume-limited sample**.

This means that the strong global color evolution seen in SDSS does not come from galaxies rapidly changing color within each population. Instead, it is driven primarily by a changing **mixture of red and blue galaxies** with redshift, with blue galaxies becoming more common at earlier cosmic times.

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

This provides a data-driven estimate of the cosmic star-formation history from SDSS photometry.

---

## Measured evolution law (raw SDSS)

The binned SDSS data with a weighted fit:

<img width="573" height="451" alt="Screenshot 2026-01-13 at 4 29 52 PM" src="https://github.com/user-attachments/assets/04d5c7a5-8790-41eb-be88-43316f89a1e3" />

This gives the observed color–redshift relation in the flux-limited SDSS sample:

**u − r ≈ 2.10 + 0.78 z**

Because SDSS is flux-limited, this relation is affected by selection bias and does not yet represent the true physical evolution of galaxies.

---

## Selection effects and volume-limited correction

The SDSS survey is **flux-limited**, meaning it only detects bright galaxies at large distances, while faint galaxies drop out of the sample at higher redshift. This introduces a systematic bias: distant galaxy samples are artificially skewed toward intrinsically luminous and typically redder systems.

To remove this bias, absolute magnitudes were computed and a **volume-limited galaxy sample** was constructed, keeping only galaxies that would be observable across the full redshift range of the survey. This ensures that the same intrinsic galaxy population is compared at all cosmic epochs.

<img width="270" height="48" alt="Screenshot 2026-01-14 at 1 12 48 PM" src="https://github.com/user-attachments/assets/0c3751f7-5c77-42af-8f97-d2cf0793f732" />

This correction is standard practice in observational cosmology and is required to measure physically meaningful galaxy-evolution trends.

---

## Bias-corrected galaxy evolution

Repeating the binned color analysis and weighted regression using the volume-limited sample yields a new, physically meaningful evolution law:

<img width="254" height="112" alt="Screenshot 2026-01-14 at 1 20 57 PM" src="https://github.com/user-attachments/assets/e1644d00-1609-4477-ae4c-15c742cc89e9" />

**u − r ≈ 2.72 − 3.11 z**

This relation shows that the mean color of the volume limited galaxy population becomes bluer with increasing redshift, even after removing all observational selection effects. Since bluer u − r indicates higher star-formation activity, this indicates that galaxies in the past were forming stars more rapidly than galaxies today.

This bias-corrected evolution law approximates the intrinsic cosmic evolution of galaxy stellar populations, rather than a trend dominated by telescope sensitivity.

---

## Population-resolved evolution in the volume-limited sample

To test whether different types of galaxies evolve in the same way, the volume-limited SDSS sample was split into two physically distinct populations using a standard **u − r color cut**:

- **Blue galaxies**: actively star-forming systems  
- **Red galaxies**: passively evolving systems  

The evolution of each population was then measured separately in the **volume-limited catalog**, ensuring that all observational selection effects were removed.

Bootstrap resampling was used to estimate the uncertainty on the color–redshift slope for each population.

### Blue galaxies

<img width="280" height="79" alt="Screenshot 2026-01-14 at 3 01 48 PM" src="https://github.com/user-attachments/assets/e73a0543-49de-46e8-9b17-b513cd860eba" />

The fitted color–redshift slope is:

**b ≈ 1.83 ± 2.44**

This corresponds to a statistical significance of only **0.75σ**, meaning the slope is not significantly different from zero.

Within the redshift range probed (z ≤ 0.3), the average color of blue galaxies is therefore consistent with being approximately constant once selection effects are removed.

### Red galaxies

<img width="288" height="77" alt="Screenshot 2026-01-14 at 3 04 46 PM" src="https://github.com/user-attachments/assets/ccee33fa-32b3-4eb3-929a-8bebac7ba7ca" />

The fitted color–redshift slope is:

**b ≈ 1.08 ± 3.74**

This corresponds to a statistical significance of only **0.29σ**, again fully consistent with no measurable evolution.

Red galaxies are already dominated by old stellar populations, and within this redshift range their colors show no statistically significant change.

### Physical meaning

These results show that the strong color evolution seen in the full SDSS sample does **not** come from galaxies changing color rapidly within each population.

Instead, it arises primarily from a changing **mixture of populations** with redshift:
- At higher redshift, the SDSS sample contains a higher fraction of blue, star-forming galaxies
- At lower redshift, red, passive galaxies become more dominant

This population mixing produces the apparent global color evolution seen in the flux-limited SDSS catalog.

Once selection bias is removed and populations are separated, both blue and red galaxies are approximately stable in color over z ≤ 0.3, consistent with standard models of galaxy evolution.

---

## Physical interpretation

The two fitted relations, the raw SDSS relation  
u − r ≈ 2.10 + 0.78 z  
and the bias-corrected relation  
u − r ≈ 2.72 − 3.11 z  
describe two different things. The raw relation reflects the observed trend in the flux-limited SDSS catalog, which is affected by telescope selection effects. The bias-corrected relation is obtained from the volume-limited sample and removes this observational bias.

The negative slope in the volume-limited fit indicates that, on average, galaxies at higher redshift are bluer than galaxies at lower redshift. Since u − r is a proxy for stellar population age and star formation activity, this means that galaxies were forming stars more actively in the past than they are today.

However, when the volume-limited sample is split into blue and red galaxies and each population is analyzed separately, neither population shows a statistically significant color–redshift slope within z ≤ 0.3. This shows that the strong global slope in the combined sample does not come from galaxies rapidly changing color within each population. Instead, it is driven mainly by a changing mixture of blue and red galaxies with redshift.

Physically, this implies that galaxy evolution over this redshift range is dominated by population transformation, with galaxies moving from the blue, star-forming population to the red, passive population as star formation shuts down, rather than by uniform aging within each group.

---

## Connection to published astronomy

The trends measured in this project are consistent with well established results from large galaxy surveys and modern galaxy evolution studies.

**1. Bimodal galaxy populations in SDSS**  
Baldry et al. (2004) showed that SDSS galaxies form two distinct populations in u − r color space, corresponding to a blue, star-forming population and a red, passive population. The red sequence and blue cloud recovered in this project from SDSS color–magnitude diagrams are consistent with this established bimodality.  
https://arxiv.org/abs/astro-ph/0410603

**2. Evolution of red and blue galaxy fractions**  
Martínez et al. (2006) used SDSS group catalogs to show that the fraction of red galaxies increases toward lower redshift, demonstrating that galaxy populations evolve with cosmic time. This agrees with the population fraction trends measured here, where one population becomes increasingly dominant as redshift decreases.  
https://arxiv.org/abs/astro-ph/0607273

**3. Quantitative evolution of galaxy colors**  
Maraston et al. (2009) modeled the redshift evolution of SDSS galaxy colors using stellar population synthesis and showed that observed color changes with redshift trace aging stellar populations and declining star formation. This provides a physical framework for interpreting the SDSS color–redshift trends measured in this project, including both the raw relation (**u − r ≈ 2.10 + 0.78 z**) and the bias corrected relation derived from the volume limited sample (**u − r ≈ 2.72 − 3.11 z**).  
https://academic.oup.com/mnrasl/article/394/1/L107/1081702

**4. Cosmic star-formation history**  
The decrease of mean u − r color toward lower redshift found here is consistent with the global cosmic star-formation history compiled by Madau and Dickinson (2014), which shows that the star-formation rate density of the universe peaked at intermediate redshift and declined toward the present day.  
https://arxiv.org/abs/1403.0007

---

## Conclusions

Using real SDSS galaxy data, this project finds that:

- Distant galaxies appear fainter with increasing redshift, consistent with cosmological expansion and survey sensitivity limits  
- Galaxies separate into two distinct populations in color–magnitude space: a blue, star-forming population and a red, passively evolving population  
- These populations correspond to the classical **blue cloud** and **red sequence** seen in large extragalactic surveys  
- The relative fractions of red and blue galaxies change systematically with redshift, indicating that the mix of galaxy types evolves over cosmic time  
- Galaxy colors (u − r) provide a useful tracer of stellar populations and star formation activity across the sample  
- In the flux limited SDSS catalog, the average galaxy color becomes bluer at higher redshift, indicating higher star formation activity in the past  
- Binned measurements show that the mean u − r decreases from about **2.2 at z ≈ 0** to about **0.9 at z ≈ 0.7**, a statistically significant change  
- A weighted regression of the flux limited sample yields  
  **u − r ≈ 2.10 + 0.78 z**,  
  describing the observed color evolution in the raw SDSS catalog  

After correcting for SDSS selection effects using a **volume limited galaxy sample**, the global color–redshift relation becomes

**u − r ≈ 2.72 − 3.11 z**

Bootstrap uncertainty analysis shows that this strong global slope does not arise from galaxies rapidly changing color within each population. Instead, it reflects a changing **mixture of galaxy populations**:

- At higher redshift, blue star-forming galaxies are more common  
- At lower redshift, red passive galaxies become more dominant  

When blue and red galaxies are analyzed separately in the volume limited sample, their color–redshift slopes are consistent with zero within uncertainty:

- Blue galaxies: **b ≈ 1.83 ± 2.44**  
- Red galaxies: **b ≈ 1.08 ± 3.74**

This indicates that over z ≤ 0.3, individual galaxies within each population do not show statistically significant color evolution. The apparent evolution in the combined sample is driven mainly by galaxies moving between populations rather than by strong color changes within a population.

Taken together, these results indicate that galaxy evolution in SDSS over this redshift range is dominated by **population transformation**, with galaxies transitioning from the blue, star-forming population to the red, passive population as star formation shuts down.

---

## Why this matters

This project uses real SDSS galaxy data to separate what is physically happening to galaxies from what is caused by how a telescope samples the universe.

By building a volume-limited sample and splitting galaxies into blue and red populations, the analysis shows that the strong color evolution seen in the raw SDSS catalog is largely driven by changing population fractions, not by galaxies rapidly changing color within each group. Blue and red galaxies behave differently, and understanding that difference is essential for interpreting any large sky survey.

This makes the project a realistic example of how modern observational astronomy extracts physical meaning from biased, incomplete data, using statistics rather than just plots.

