---
title: "Computing polar triangles with linear algebra"
url: "https://www.johndcook.com/blog/2026/10/24/computing-polar-triangles/"
fetched_at: 2026-10-25T10:01:22.654732+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Computing polar triangles with linear algebra

Source: https://www.johndcook.com/blog/2026/10/24/computing-polar-triangles/

The
previous post
defined the polar triangle of a spherical triangle in terms of its sides and angles, but it doesn’t construct the triangle. It only specifies one of a family of triangles located anywhere on the sphere.
How do we know that polar triangles exist? There is a geometric construction that starts with a spherical triangle and constructs a unique new spherical triangle, and one can show that this new triangle has the angles and sides described in the previous post.
There is also a linear algebraic construction of polar triangles, and that’s the topic of this post. In a nutshell, take your sphere to be the unit sphere in 3D. Write the coordinates of each vertex as the columns of a matrix. Invert that matrix and normalize each row. Then the rows are the coordinates of the polar vertices.
This process is an involution: the polar of the polar of a triangle is the original triangle.
The following Python code illustrates the process described above. It begins with a triangle on the globe with vertices
A
,
B
, and
C
at Chicago, Quito, and Paris respectively. It computes the polar triangle, then computes the polar of that, and shows that the result is the original triangle.
In case you’re curious,
A
′ is at 40.77° N, 168.33° W
B
′ is at 34.53° S, 35.70° W
C
′ is at 10.00° N, 11.43° E
import numpy as np

def latlon_to_cartesian(lat_deg, lon_deg):
    lat = np.radians(lat_deg)
    lon = np.radians(lon_deg)
    x = np.cos(lat) * np.cos(lon)
    y = np.cos(lat) * np.sin(lon)
    z = np.sin(lat)
    return np.array([x, y, z])

def cartesian_to_latlon(v):
    v = v / np.linalg.norm(v)
    lat = np.degrees(np.arcsin(np.clip(v[2], -1, 1)))
    lon = np.degrees(np.arctan2(v[1], v[0]))
    return lat, lon

def polar_triangle(M):
    """
    Polar triangle via matrix inversion.
    M: 3×3 matrix with columns = unit vectors of the original vertices.
    Returns 3×3 matrix whose columns are the polar unit vectors.
    """
    Minv = np.linalg.inv(M)
    # Normalize each row of the inverse (rows are parallel to the polar directions)
    polar_rows = Minv / np.linalg.norm(Minv, axis=1, keepdims=True)
    return polar_rows.T          # columns = polar vertices

# Original vertices (Chicago, Quito, Paris)
A = latlon_to_cartesian(41.85003, -87.65005)
B = latlon_to_cartesian(-0.22985, -78.52495)
C = latlon_to_cartesian(48.85341,  2.3488)

M = np.column_stack([A, B, C])
print("M (columns = original vertices):\n", M)
print("det(M) =", np.linalg.det(M))

# Polar triangle
M_prime = polar_triangle(M)
print("\nM' (columns = polar vertices):\n", M_prime)

print("\nPolar geographic coordinates (lat, lon):")
for name, col in zip(["A'", "B'", "C'"], range(3)):
    print(name, cartesian_to_latlon(M_prime[:, col]))

# Polar of the polar
M_double = polar_triangle(M_prime)
print("\nPolar-of-polar matrix:\n", M_double)
print("max |difference from original M| =",
      np.max(np.abs(M_double - M)))
