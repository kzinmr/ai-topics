---
title: "Poe, Bessel, and Drones"
url: "https://www.johndcook.com/blog/2026/10/14/poe-bessel-and-drones/"
fetched_at: 2026-10-15T10:01:36.229770+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Poe, Bessel, and Drones

Source: https://www.johndcook.com/blog/2026/10/14/poe-bessel-and-drones/

What’s a connection between Edgar Allan Poe and Friedrich Wilhelm Bessel?
Poe’s story The Pit and the Pendulum describes a pendulum with a semicircular blade being lowered on a cable. This is an interesting variation on the usual harmonic oscillator because the length
L
of the pendulum is not constant but rather an increasing function of time
L
(
t
).
Using the
small angle
approximation sin(θ) ≈ θ, the equation of motion is
L
θ″ +
L
′ θ′ +
g
θ = 0.
If we assume the length is increasing at a constant rate, then with a change of variables described in [1], this differential equation becomes Bessel’s equation and its solutions are Bessel functions.
The authors of [1] state that their primary interest is whether a pendulum can have the motion that Poe describes. But as they indicate in their opening sentence,
The study of the motion of a steadily descending pendulum has practical applications (e.g., to the oscillations of a load being lowered by a crane).
A more recent application would be describing the motion of a package being delivered by a Zipline drone.
Related posts
[1] Robert L. Borrelli, Courtney S. Coleman, and Dana D. Hobson. Poe’s Pendulum. Mathematics Magazine, Vol. 58, No. 2 (Mar., 1985), pp. 78–83
