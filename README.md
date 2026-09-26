# Brutus-Pell Connected Spectrum

Author: Gabriel St-Pierre

High-precision computational study of the pair-normalized connected interaction spectrum arising in the Brutus-Pell prime corridor.

## Core objects

`S_Q(u)=E[prod_q(1+u Z_q)]`

`K_Q(u)=log S_Q(u)-sum_{q<r}log(1+p_qr u^2)`

with `p_qr=E[Z_q Z_r]` and `E[Z_q]=0`.

The coefficients `K3,K4,...` isolate connected contributions after exact removal of the pairwise logarithmic level.

## Contents

- `study/BRUTUS_PELL_CONNECTED_SPECTRUM.md` - archival numerical note.
- `data/high_precision_summary.csv` - 2M/4M/8M summary for Q=199 and Q=997.
- `scripts/connected_spectrum.py` - reproducibility implementation used by the five-post control-plane run.
- `artifacts/first_five_post_run_summary.json` - first ASTRAEUM five-role verification artifact.
- `zenodo/zenodo_metadata.json` - manual Zenodo dataset/software-study metadata template.

## Important correction

Earlier float64 evaluations of `D_Q` at ppm-scale residuals were numerically unstable.
The archived summary uses the 70-digit Decimal values as the high-precision reference.

## Status

Finite-sample numerical study and reproducibility package.
No general asymptotic law for `n*K_j` is claimed.
