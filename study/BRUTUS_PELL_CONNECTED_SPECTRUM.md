# Brutus-Pell Connected Spectrum: High-Precision Finite-Sample Study

**Gabriel St-Pierre**

Date: 2026-09-25

## Abstract

This record documents a connected-interaction expansion for a finite empirical ensemble associated with the prime corridor `p=72t^2+1`.
After normalizing local divisibility indicators and subtracting the complete pairwise logarithmic contribution, the residual dust is represented by coefficients `K3,K4,...` of a connected generator.
Calculations at X=2M,4M,8M and cutoffs Q=199,997 were recomputed using 70-digit Decimal arithmetic.
The high-precision audit reveals that earlier few-ppm residuals were dominated by float64 cancellation.
For the six archived finite samples, the truncation through K8 closes the connected dust to about `10^-11` relative or better.

## 1. Prime corridor

For odd `t`, define

`p=72t^2+1`.

The empirical population consists of those `t<=X` for which `p` is prime.

For each prime gate `q` in a fixed cutoff set, let `I_q(t)=1` if `q|t`, else 0.
Let `f_q=E[I_q]`, `w_q=1-I_q/q`, and `mu_q=1-f_q/q`.
Define the centered normalized variable

`Z_q = w_q/mu_q - 1`.

Then `E[Z_q]=0` exactly for the finite empirical sample.

## 2. Connected generator

Set

`S_Q(u)=E[prod_q(1+u Z_q)]`.

Write `p_qr=E[Z_q Z_r]` over the complete set of pairs under the fixed cutoff Q.

Define

`K_Q(u)=log S_Q(u)-sum_{q<r}log(1+p_qr u^2)`.

Because the linear term vanishes and `T2=sum p_qr`, the coefficients of degrees 1 and 2 cancel:

`K_Q(u)=K3*u^3+K4*u^4+K5*u^5+...`.

The first coefficients are

`K3=T3`

`K4=T4-T2^2/2+(1/2)sum p_qr^2`

`K5=T5-T2*T3`

`K6=T6-T2*T4-T3^2/2+T2^3/3-(1/3)sum p_qr^3`.

Orders K7 and K8 are generated algorithmically from the logarithmic power-series recurrence.

## 3. High-precision correction

At X=8M, Q=199, a float64 evaluation gave approximately

`D_float64=1.4012135944358927e-7`.

The 70-digit evaluation gives

`D_decimal=1.40121802258865131432897127425813608225178270215411040410573676752147e-7`.

The displacement is of the same scale as the previously interpreted ppm residual.
Therefore the old ppm-scale gap must not be treated as a mathematical tail estimate.

The same effect is visible in the first five-post run at X=2M,Q=199:

`D_decimal=6.74090794086069938339730573270919317986497315981983009090138e-7`

`D_float64=6.740911134950114e-7`.

The relative delta is about `4.73837e-7`.

## 4. Finite-sample closure

The file `data/high_precision_summary.csv` contains the six archived combinations:

- X=2M, Q=199 and Q=997;
- X=4M, Q=199 and Q=997;
- X=8M, Q=199 and Q=997.

For every row, the recorded relative residual

`(D-sum(K3..K8))/D`

is around `10^-11` in magnitude or smaller.

This is an empirical finite-sample statement, not an asymptotic convergence claim.

## 5. Analytic finite-sample certificate

For a fixed finite sample define

`B_Q(r)=E[prod_q(1+r|Z_q|)-1]`.

For `|u|<=r`,

`|S_Q(u)-1| <= B_Q(r)`.

Hence `B_Q(r)<1` implies that `S_Q` has no zeros in that disk and the logarithm branch anchored at `u=0` is analytic there.

In the first five-post run X=2M,Q=199, POSTE-03 verified `B_199(4)<1` using integer/rational comparison rather than floating arithmetic.
The recorded relative margin is

`0.07780929093461051160799336641`.

The same worker also verified that every pair factor `1+p_qr*u^2` is zero-free for `|u|<=4`.

Therefore, for that finite sample, the Taylor series of `K_Q` converges absolutely at `u=1`, and

`D_Q=K_Q(1)=sum_{k>=3}K_k`.

This statement is finite-sample and does not imply uniformity as X or Q grows.

## 6. Five-role reproducibility

The first archived control-plane run uses:

- PRIMARY: pattern aggregation + Decimal polynomial coefficients;
- MIRROR: row-wise factorization + Newton identities + independent logarithmic recurrence;
- COUNTERTEST: integer/rational finite-sample zero-free certificate;
- PRECISION: Decimal versus float64 audit;
- ARBITER: comparison of traces without authoring the primary result.

At X=2M,Q=199, PRIMARY and MIRROR agree on D to a relative difference of approximately `6.68e-62`.

## 7. Limitations

- no asymptotic value for `n*K_j` is established;
- no universal sign law for the coefficients is established;
- no physical interpretation is inferred from the arithmetic spectrum;
- bibliographic novelty is not claimed for classical Lucas/Pell tools.

## Reproducibility

Use `scripts/connected_spectrum.py` through the Brutus Control Plane / ASTRAEUM runner, or adapt its role functions for a standalone calculation.
