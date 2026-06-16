---
title: "Quaternion Rotations, Claude, and Lean"
url: "https://www.johndcook.com/blog/2026/06/15/quaternions-claude-lean/"
fetched_at: 2026-06-16T07:00:49.147548+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Quaternion Rotations, Claude, and Lean

Source: https://www.johndcook.com/blog/2026/06/15/quaternions-claude-lean/

I got an email message this afternoon reporting a typo in a blog post from about a year ago on
converting between quaternions and rotation matrices
[1]. The email said exactly where the typo was, but I decided to see whether Claude would find it. Specifically, I prompted Sonnet 4.6 Medium with the following.
Write Lean code to verify the two theorems at the top of this post:
https://www.johndcook.com/blog/2025/05/07/quaternions-and-rotation-matrices/
That is, prove that the expressions given in the two SVG files are correct.
The post included Python code to numerically verify the equations. However, the Python code differed from the LaTeX code for the image in one subscript [2]. Although I asked Claude to prove the expressions in the SVG file produced by the LaTeX code, it detected the conflict between the Python and LaTeX and correctly concluded that the former was correct.
The SVG is an image — let me rely on the Python code in the blog (which is the ground truth implementation) and the matrix entries in the alt text. … Note the alt text says row 1 col 2 is
2(q_1 q_3 - q_0 q_1)
— that’s a typo in the alt text; the Python code says
2*(q2*q3 - q0*q1)
which makes sense. I’ll use the Python code as the authoritative source.
The code did not run on first attempt. After four iterations of pasting in error messages and generating code again, it worked.
Here is the final Lean 4 code.
/-
  Lean 4 / Mathlib verification of the two theorems from:
    "Converting between quaternions and rotation matrices"
    ...

  Matrix entries (0-based, matching the post's Python code):
    R00 = 2(q0²+q1²)−1    R01 = 2(q1 q2−q0 q3)   R02 = 2(q1 q3+q0 q2)
    R10 = 2(q1 q2+q0 q3)  R11 = 2(q0²+q2²)−1     R12 = 2(q2 q3−q0 q1)
    R20 = 2(q1 q3−q0 q2)  R21 = 2(q2 q3+q0 q1)   R22 = 2(q0²+q3²)−1

  THEOREM 1  (quaternion → rotation matrix)
    If q0²+q1²+q2²+q3² = 1 then R is orthogonal (Rᵀ R = I),
    proved via the 9 scalar dot-product identities.

  THEOREM 2  (rotation matrix → quaternion, Chiaverini–Siciliano)
    With rᵢⱼ as above:
        1 + R00 + R11 + R22 = 4 q0²
        1 + R00 − R11 − R22 = 4 q1²
        1 − R00 + R11 − R22 = 4 q2²
        1 − R00 − R11 + R22 = 4 q3²
-/

import Mathlib.Tactic

set_option linter.style.whitespace false

variable (q0 q1 q2 q3 : ℝ)

/-! ## Theorem 1 : Rᵀ R = I -/

-- ── Column norms = 1 ─────────────────────────────────────────────────────────

theorem col0_norm (h : q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2 = 1) :
    (2 * (q0 ^ 2 + q1 ^ 2) - 1) ^ 2 + (2 * (q1 * q2 + q0 * q3)) ^ 2 +
    (2 * (q1 * q3 - q0 * q2)) ^ 2 = 1 := by
  nlinarith [sq_nonneg (q0 ^ 2 + q1 ^ 2 - q2 ^ 2 - q3 ^ 2),
             sq_nonneg (q0 * q2 + q1 * q3), sq_nonneg (q0 * q3 - q1 * q2),
             sq_nonneg q0, sq_nonneg q1, sq_nonneg q2, sq_nonneg q3]

theorem col1_norm (h : q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2 = 1) :
    (2 * (q1 * q2 - q0 * q3)) ^ 2 + (2 * (q0 ^ 2 + q2 ^ 2) - 1) ^ 2 +
    (2 * (q2 * q3 + q0 * q1)) ^ 2 = 1 := by
  nlinarith [sq_nonneg (q0 ^ 2 - q1 ^ 2 + q2 ^ 2 - q3 ^ 2),
             sq_nonneg (q0 * q1 + q2 * q3), sq_nonneg (q0 * q3 - q1 * q2),
             sq_nonneg q0, sq_nonneg q1, sq_nonneg q2, sq_nonneg q3]

theorem col2_norm (h : q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2 = 1) :
    (2 * (q1 * q3 + q0 * q2)) ^ 2 + (2 * (q2 * q3 - q0 * q1)) ^ 2 +
    (2 * (q0 ^ 2 + q3 ^ 2) - 1) ^ 2 = 1 := by
  nlinarith [sq_nonneg (q0 ^ 2 - q1 ^ 2 - q2 ^ 2 + q3 ^ 2),
             sq_nonneg (q0 * q1 - q2 * q3), sq_nonneg (q0 * q2 + q1 * q3),
             sq_nonneg q0, sq_nonneg q1, sq_nonneg q2, sq_nonneg q3]

-- ── Column orthogonality = 0 ─────────────────────────────────────────────────
-- These need h (the residuals shown by Lean are multiples of (q0²+q1²+q2²+q3²-1)).
-- We use linear_combination with the explicit witnesses.

theorem col0_col1_orth (h : q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2 = 1) :
    (2 * (q0 ^ 2 + q1 ^ 2) - 1) * (2 * (q1 * q2 - q0 * q3)) +
    (2 * (q1 * q2 + q0 * q3)) * (2 * (q0 ^ 2 + q2 ^ 2) - 1) +
    (2 * (q1 * q3 - q0 * q2)) * (2 * (q2 * q3 + q0 * q1)) = 0 := by
  linear_combination 4 * q1 * q2 * h

theorem col0_col2_orth (h : q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2 = 1) :
    (2 * (q0 ^ 2 + q1 ^ 2) - 1) * (2 * (q1 * q3 + q0 * q2)) +
    (2 * (q1 * q2 + q0 * q3)) * (2 * (q2 * q3 - q0 * q1)) +
    (2 * (q1 * q3 - q0 * q2)) * (2 * (q0 ^ 2 + q3 ^ 2) - 1) = 0 := by
  linear_combination 4 * q1 * q3 * h

theorem col1_col2_orth (h : q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2 = 1) :
    (2 * (q1 * q2 - q0 * q3)) * (2 * (q1 * q3 + q0 * q2)) +
    (2 * (q0 ^ 2 + q2 ^ 2) - 1) * (2 * (q2 * q3 - q0 * q1)) +
    (2 * (q2 * q3 + q0 * q1)) * (2 * (q0 ^ 2 + q3 ^ 2) - 1) = 0 := by
  linear_combination 4 * q2 * q3 * h

-- ── Row norms = 1 ────────────────────────────────────────────────────────────

theorem row0_norm (h : q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2 = 1) :
    (2 * (q0 ^ 2 + q1 ^ 2) - 1) ^ 2 + (2 * (q1 * q2 - q0 * q3)) ^ 2 +
    (2 * (q1 * q3 + q0 * q2)) ^ 2 = 1 := by
  nlinarith [sq_nonneg (q0 ^ 2 + q1 ^ 2 - q2 ^ 2 - q3 ^ 2),
             sq_nonneg (q0 * q2 - q1 * q3), sq_nonneg (q0 * q3 + q1 * q2),
             sq_nonneg q0, sq_nonneg q1, sq_nonneg q2, sq_nonneg q3]

theorem row1_norm (h : q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2 = 1) :
    (2 * (q1 * q2 + q0 * q3)) ^ 2 + (2 * (q0 ^ 2 + q2 ^ 2) - 1) ^ 2 +
    (2 * (q2 * q3 - q0 * q1)) ^ 2 = 1 := by
  nlinarith [sq_nonneg (q0 ^ 2 - q1 ^ 2 + q2 ^ 2 - q3 ^ 2),
             sq_nonneg (q0 * q1 - q2 * q3), sq_nonneg (q0 * q3 + q1 * q2),
             sq_nonneg q0, sq_nonneg q1, sq_nonneg q2, sq_nonneg q3]

theorem row2_norm (h : q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2 = 1) :
    (2 * (q1 * q3 - q0 * q2)) ^ 2 + (2 * (q2 * q3 + q0 * q1)) ^ 2 +
    (2 * (q0 ^ 2 + q3 ^ 2) - 1) ^ 2 = 1 := by
  nlinarith [sq_nonneg (q0 ^ 2 - q1 ^ 2 - q2 ^ 2 + q3 ^ 2),
             sq_nonneg (q0 * q1 + q2 * q3), sq_nonneg (q0 * q2 - q1 * q3),
             sq_nonneg q0, sq_nonneg q1, sq_nonneg q2, sq_nonneg q3]

-- ── Row orthogonality = 0 ────────────────────────────────────────────────────

theorem row0_row1_orth (h : q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2 = 1) :
    (2 * (q0 ^ 2 + q1 ^ 2) - 1) * (2 * (q1 * q2 + q0 * q3)) +
    (2 * (q1 * q2 - q0 * q3)) * (2 * (q0 ^ 2 + q2 ^ 2) - 1) +
    (2 * (q1 * q3 + q0 * q2)) * (2 * (q2 * q3 - q0 * q1)) = 0 := by
  linear_combination 4 * q1 * q2 * h

theorem row0_row2_orth (h : q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2 = 1) :
    (2 * (q0 ^ 2 + q1 ^ 2) - 1) * (2 * (q1 * q3 - q0 * q2)) +
    (2 * (q1 * q2 - q0 * q3)) * (2 * (q2 * q3 + q0 * q1)) +
    (2 * (q1 * q3 + q0 * q2)) * (2 * (q0 ^ 2 + q3 ^ 2) - 1) = 0 := by
  linear_combination 4 * q1 * q3 * h

theorem row1_row2_orth (h : q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2 = 1) :
    (2 * (q1 * q2 + q0 * q3)) * (2 * (q1 * q3 - q0 * q2)) +
    (2 * (q0 ^ 2 + q2 ^ 2) - 1) * (2 * (q2 * q3 + q0 * q1)) +
    (2 * (q2 * q3 - q0 * q1)) * (2 * (q0 ^ 2 + q3 ^ 2) - 1) = 0 := by
  linear_combination 4 * q2 * q3 * h

/-! ## Theorem 2 : Chiaverini–Siciliano square-root arguments -/

theorem cs_arg0 (h : q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2 = 1) :
    1 + (2 * (q0 ^ 2 + q1 ^ 2) - 1) + (2 * (q0 ^ 2 + q2 ^ 2) - 1) +
    (2 * (q0 ^ 2 + q3 ^ 2) - 1) = 4 * q0 ^ 2 := by linarith

theorem cs_arg1 (h : q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2 = 1) :
    1 + (2 * (q0 ^ 2 + q1 ^ 2) - 1) - (2 * (q0 ^ 2 + q2 ^ 2) - 1) -
    (2 * (q0 ^ 2 + q3 ^ 2) - 1) = 4 * q1 ^ 2 := by linarith

theorem cs_arg2 (h : q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2 = 1) :
    1 - (2 * (q0 ^ 2 + q1 ^ 2) - 1) + (2 * (q0 ^ 2 + q2 ^ 2) - 1) -
    (2 * (q0 ^ 2 + q3 ^ 2) - 1) = 4 * q2 ^ 2 := by linarith

theorem cs_arg3 (h : q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2 = 1) :
    1 - (2 * (q0 ^ 2 + q1 ^ 2) - 1) - (2 * (q0 ^ 2 + q2 ^ 2) - 1) +
    (2 * (q0 ^ 2 + q3 ^ 2) - 1) = 4 * q3 ^ 2 := by linarith

/-! ### Sign-correction identities (pure ring) -/

theorem sign_q1 : (2 * (q2 * q3 + q0 * q1)) - (2 * (q2 * q3 - q0 * q1)) = 4 * (q0 * q1) := by ring
theorem sign_q2 : (2 * (q1 * q3 + q0 * q2)) - (2 * (q1 * q3 - q0 * q2)) = 4 * (q0 * q2) := by ring
theorem sign_q3 : (2 * (q1 * q2 + q0 * q3)) - (2 * (q1 * q2 - q0 * q3)) = 4 * (q0 * q3) := by ring
[1] I very much appreciate error reports. Thank you to everyone who has helped improve this blog.
[2] It is awkward that math is written in LaTeX and implemented in, say, Python. Lately I’ve been generating one or the other to reduce the chance of error. When I’m using Mathematica, for example, I’ll use
TeXForm[]
to convert the Mathematica code to LaTeX.
