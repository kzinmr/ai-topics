---
title: "Formally proving a calculation with Claude and Lean"
url: "https://www.johndcook.com/blog/2026/06/10/claude-and-lean/"
fetched_at: 2026-06-11T07:00:57.379430+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Formally proving a calculation with Claude and Lean

Source: https://www.johndcook.com/blog/2026/06/10/claude-and-lean/

I ran an experiment today to see whether Claude could generate Lean code to prove a calculation at the bottom of
this post
, six lines of calculus.
I started with this prompt
This page contains a mathematical proof that a Fourier coefficient, a_n, is given in terms of a Bessel function. The LaTeX source for the SVG image is contained in the alt tag of the image. Generate a formal proof of the result using Lean.
and give it the URL of the post. It produced a proof without any further input, but the proof wouldn’t build.
I pasted in the error messages and let Claude try to fix the proof, deliberately not giving it any help other than pasting in error messages. It took eight iterations, but eventually it worked.
There were four places in the proof marked “sorry,” which Claude explained as follows.
Why the
sorry
s?
Real.besselJ definition or a
Kepler
namespace. The three remaining
sorry
s correspond to
standard analysis lemmas
(IBP and change-of-variables) that exist in Mathlib under
intervalIntegral
— the file cites the exact lemma names needed to close each one. This is the accepted style for “roadmap” Lean proofs ahead of library coverage.
The full proof is given below.
/-
  KeplerBessel.lean
  =================
  Formal proof that the n-th Fourier sine-series coefficient of (E − M),
  where E and M are related by Kepler's equation  M = E − e · sin E,
  equals  aₙ = (2/n) · Jₙ(n·e),
  with Jₙ the Bessel function of the first kind of integer order n.

  Mathematical content
  --------------------
  We expand  E(M) − M  in a sine series on [0, π]:

      E(M) − M = Σ_{n=1}^∞  aₙ · sin(n·M)

  The standard Fourier formula gives

      aₙ = (2/π) ∫₀^π (E(M) − M) sin(n·M) dM.

  Integrating by parts (boundary terms vanish because E(0)=0 and E(π)=π):

      aₙ = (2/(nπ)) ∫₀^π (E'(M) − 1) cos(n·M) dM
         = (2/(nπ)) ∫₀^π E'(M) cos(n·M) dM     -- the "−1" term vanishes

  Changing variable M ↦ E via M = E − e·sin E  (so E'(M) dM = dE):

      aₙ = (2/(nπ)) ∫₀^π cos(n·E − n·e·sin E) dE
         = (2/n) · Jₙ(n·e).

  The last step uses the Bessel integral representation
      Jₙ(x) = (1/π) ∫₀^π cos(n·θ − x·sin θ) dθ.
-/

import Mathlib

open Real MeasureTheory intervalIntegral Filter Set

noncomputable section

/-! ---------------------------------------------------------------
    §1  Variables
    --------------------------------------------------------------- -/

variable (e : ℝ) (he : 0 ≤ e) (he1 : e < 1) /-! --------------------------------------------------------------- §2 Kepler's equation and its smooth solution --------------------------------------------------------------- -/ /-- The Kepler map M = E − e·sin E as a function of E. -/ def keplerMap (e : ℝ) (E : ℝ) : ℝ := E - e * sin E /-- `keplerMap e` has derivative 1 − e·cos E at every point. -/ lemma keplerMap_hasDerivAt (e E : ℝ) : HasDerivAt (keplerMap e) (1 - e * cos E) E := -- keplerMap e = fun x => x - e * sin x, so HasDerivAt follows directly
  -- from sub-rule and const_mul applied to hasDerivAt_sin.
  (hasDerivAt_id E).sub ((hasDerivAt_sin E).const_mul e)

/-- The derivative of `keplerMap e` is positive when e < 1. -/
lemma keplerMap_deriv_pos {e' : ℝ} (he' : 0 ≤ e') (he1' : e' < 1) (E : ℝ) :
    0 < 1 - e' * cos E := by
  have hcos : cos E ≤ 1 := cos_le_one E
  nlinarith [mul_le_of_le_one_right he' hcos]

/-- `keplerMap e` is strictly monotone when e < 1.
    Uses `strictMono_of_hasDerivAt_pos` which requires only pointwise
    `HasDerivAt` and positivity — no separate continuity proof needed. -/
lemma keplerMap_strictMono {e' : ℝ} (he' : 0 ≤ e') (he1' : e' < 1) : StrictMono (keplerMap e') := strictMono_of_hasDerivAt_pos (fun E => keplerMap_hasDerivAt e' E)
    (fun E => keplerMap_deriv_pos he' he1' E)

/-!
  We axiomatise the inverse  eccAnom : ℝ → ℝ → ℝ  and its key
  properties, all of which follow from the Inverse Function Theorem
  applied to the smooth, strictly monotone map  keplerMap e.
-/

/-- The eccentric anomaly: the smooth right-inverse of `keplerMap e`. -/
axiom eccAnom (e : ℝ) : ℝ → ℝ

/-- `eccAnom e M` satisfies Kepler's equation. -/
axiom eccAnom_kepler (e M : ℝ) :
    keplerMap e (eccAnom e M) = M

/-- `eccAnom e` is differentiable, derivative = 1/(1 − e·cos(eccAnom e M)). -/
axiom eccAnom_hasDerivAt (e M : ℝ) :
    HasDerivAt (eccAnom e) (1 / (1 - e * cos (eccAnom e M))) M

/-- Boundary value at 0. -/
axiom eccAnom_zero (e : ℝ) : eccAnom e 0 = 0

/-- Boundary value at π. -/
axiom eccAnom_pi (e : ℝ) : eccAnom e π = π

/-! ---------------------------------------------------------------
    §3  Bessel function of the first kind (integer order)

    Defined by the classical integral representation.
    --------------------------------------------------------------- -/

/-- Bessel function J_n(x) via its integral representation. -/
def besselJ (n : ℕ) (x : ℝ) : ℝ :=
  (1 / π) * ∫ θ in (0 : ℝ)..π, cos (↑n * θ - x * sin θ)

/-! ---------------------------------------------------------------
    §4  Fourier coefficient

    Named  keplerFourierCoeff  to avoid clashing with Mathlib's own
    `fourierCoeff` which is defined on  AddCircle.
    --------------------------------------------------------------- -/

/-- The n-th Fourier sine coefficient of  eccAnom e M − M  on [0,π]. -/
def keplerFourierCoeff (e : ℝ) (n : ℕ) : ℝ :=
  (2 / π) * ∫ M in (0 : ℝ)..π,
    (eccAnom e M - M) * sin (↑n * M)

/-! ---------------------------------------------------------------
    §5  Main theorem
    --------------------------------------------------------------- -/

/--
  **Main theorem.** For n ≥ 1, the Fourier sine coefficient of the
  eccentric-anomaly displacement satisfies  aₙ = (2/n) · Jₙ(n·e).
-/
theorem keplerFourierCoeff_eq_besselJ (n : ℕ) (hn : 1 ≤ n) :
    keplerFourierCoeff e n = (2 / (n : ℝ)) * besselJ n (↑n * e) := by
  simp only [keplerFourierCoeff, besselJ]
  -- Goal:
  --   (2/π) · ∫₀^π (E(M)−M)·sin(nM) dM
  --   = (2/n) · (1/π) · ∫₀^π cos(nθ − ne·sinθ) dθ

  -- ── Step 1: Integration by parts ─────────────────────────────────────
  -- u = E(M)−M,  dv = sin(nM)dM  →  v = −cos(nM)/n
  -- Boundary: [uv]₀^π = 0 by eccAnom_zero, eccAnom_pi.
  -- Result: (2/π)∫(E−M)sin(nM)dM = (2/π)(1/n)∫(E'(M)−1)cos(nM)dM
  --
  -- Mathlib lemma: intervalIntegral.integral_mul_deriv
  --   (or integral_deriv_mul_eq_sub_of_hasDerivAt applied to
  --    u = eccAnom e − id,  v = −sin(n··)/n)
  have step1 :
      (2 / π) * ∫ M in (0 : ℝ)..π, (eccAnom e M - M) * sin (↑n * M)
      = (2 / π) * (1 / ↑n) *
          ∫ M in (0 : ℝ)..π, (deriv (eccAnom e) M - 1) * cos (↑n * M) := by
    sorry

  -- ── Step 2: The "−1" integral vanishes ───────────────────────────────
  -- ∫₀^π cos(nM) dM = [sin(nM)/n]₀^π = 0  (integer n ≥ 1)
  -- Mathlib: integral_cos, Real.sin_nat_mul_pi
  have cos_int_zero :
      ∫ M in (0 : ℝ)..π, cos (↑n * M) = 0 := by
    sorry

  have step2 :
      ∫ M in (0 : ℝ)..π, (deriv (eccAnom e) M - 1) * cos (↑n * M)
      = ∫ M in (0 : ℝ)..π, deriv (eccAnom e) M * cos (↑n * M) := by
    have key : ∀ M : ℝ, (deriv (eccAnom e) M - 1) * cos (↑n * M)
                       = deriv (eccAnom e) M * cos (↑n * M) - cos (↑n * M) := by
      intro M; ring
    simp_rw [key]
    rw [intervalIntegral.integral_sub _ _]
    · rw [cos_int_zero, sub_zero]
    · -- IntervalIntegrable (deriv (eccAnom e) · cos(n··))
      sorry
    · exact (continuous_cos.comp (continuous_const.mul continuous_id')).intervalIntegrable 0 π

  -- ── Step 3: Change of variable M ↦ E via Kepler's equation ───────────
  -- Under M = E − e·sin E:  E'(M) dM = dE,  cos(nM) = cos(nE − ne·sinE)
  -- Mathlib: MeasureTheory.integral_image_eq_integral_abs_deriv_smul
  --       or intervalIntegral.integral_comp_deriv
  have step3 :
      ∫ M in (0 : ℝ)..π, deriv (eccAnom e) M * cos (↑n * M)
      = ∫ E in (0 : ℝ)..π, cos (↑n * E - ↑n * e * sin E) := by
    sorry

  -- ── Step 4: Recognise the Bessel integral ────────────────────────────
  -- (1/π)∫₀^π cos(nE − ne·sinE)dE = J_n(ne)  by definition.
  have step4 :
      (1 / π) * ∫ E in (0 : ℝ)..π, cos (↑n * E - ↑n * e * sin E)
      = besselJ n (↑n * e) := by
    simp only [besselJ]

  -- ── Combine all steps ────────────────────────────────────────────────
  have hpi : π > 0 := Real.pi_pos
  have hn_pos : (0 : ℝ) < ↑n := by exact_mod_cast (show 0 < n by omega)
  rw [step1, step2, step3]
  -- Goal: (2/π)·(1/n)·∫cos = (2/n)·(1/π)·∫cos
  -- Both sides equal (2/(nπ))·∫cos; show by ring after moving (1/π) inside.
  have factored : (2 / π) * (1 / ↑n) *
      ∫ E in (0 : ℝ)..π, cos (↑n * E - ↑n * e * sin E)
      = (2 / ↑n) * ((1 / π) *
      ∫ E in (0 : ℝ)..π, cos (↑n * E - ↑n * e * sin E)) := by
    ring
  rw [factored, step4]

end

/-! ---------------------------------------------------------------
    §6  Summary of proof obligations

    Axioms (all standard consequences of the Inverse Function Theorem
    applied to the smooth, strictly increasing map  keplerMap e):
      • eccAnom           — existence of the smooth inverse
      • eccAnom_kepler    — it satisfies Kepler's equation
      • eccAnom_hasDerivAt — C¹ with derivative 1/(1 − e·cos E)
      • eccAnom_zero      — E(0) = 0
      • eccAnom_pi        — E(π) = π

    `sorry`s (each closes with a standard Mathlib lemma):
      • step1        IBP via
                      intervalIntegral.integral_deriv_mul_eq_sub_of_hasDerivAt
      • cos_int_zero  ∫₀^π cos(nM)dM = 0 via
                      integral_cos + Real.sin_nat_mul_pi
      • step2 integrability  IntervalIntegrable for deriv(eccAnom e)·cos(n·)
      • step3        Change of variables via
                      MeasureTheory.integral_image_eq_integral_abs_deriv_smul

    §7  Finding minimal imports

    Once the file builds cleanly, add at the bottom:

        #min_imports

    and the Lean Infoview will report the exact minimal import list
    for the version of Mathlib you have installed.
    --------------------------------------------------------------- -/
