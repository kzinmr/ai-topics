---
title: "Visualizing medical code hierarchy with treemaps"
url: "https://www.johndcook.com/blog/2026/07/17/visualizing-medical-code-hierarchy/"
fetched_at: 2026-07-18T07:00:46.891967+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Visualizing medical code hierarchy with treemaps

Source: https://www.johndcook.com/blog/2026/07/17/visualizing-medical-code-hierarchy/

Quick follow up to the previous two posts on ICD-10 codes and HCPCS codes. This post uses Python’s squarify library to create treemaps visualizing how many codes begin with each letter.
Here’s the treemap for HCPCS codes.
And here’s the treemap for ICD-10 codes.
The sizes of the squares are proportional to the number of codes beginning with that letter. Note that they are not necessarily proportional to how often codes are used.
The HCPCS map omits R and U because these are tiny relative to the rest. The ICD-10 map omits U for the same reason.
Here’s the code that was used to create the HCPCS map.
import matplotlib.pyplot as plt
import squarify

# HCPCS
data = {
    "G": 2010,
    "J": 1232,
    "L": 940,
    "A": 862,
    "E": 671,
    "Q": 639,
    "C": 619,
    "S": 533,
    "M": 506,
    "V": 212,
    "K": 175,
    "T": 114,
    "H": 94,
    "P": 59,
    "B": 51,
  # "U": 5,
  # "R": 3,
}

labels = list(data.keys())
sizes = list(data.values())

# Labels are just the letters (no counts)
display_labels = labels

# Color map — one distinct color per box
colors = plt.cm.tab20.colors[: len(labels)]

fig, ax = plt.subplots(figsize=(12, 8))
squarify.plot(
    sizes=sizes,
    label=display_labels,
    color=colors,
    alpha=0.85,
    ax=ax,
    text_kwargs={"fontsize": 30, "weight": "bold"},
    pad=True,
)
ax.axis("off")

plt.tight_layout()
plt.savefig("treemap.png", dpi=72)
plt.show()
The code to create the ICD-10 map differs only in its data.
# ICD-10
data = {
    "S": 31052, 
    "T": 10090, 
    "M":  6665, 
    "V":  4086, 
    "H":  3330, 
    "O":  2437, 
    "Y":  1590, 
    "I":  1427, 
    "Z":  1411, 
    "W":  1290, 
    "C":  1226, 
    "L":  1000, 
    "E":   971, 
    "Q":   894, 
    "F":   871, 
    "K":   857, 
    "N":   836, 
    "D":   824, 
    "R":   773, 
    "G":   700, 
    "A":   573, 
    "X":   495, 
    "B":   495, 
    "P":   463, 
    "J":   360, 
  # "U":     3,
}
