#!/usr/bin/env python3
"""Generate synthetic point clouds for project previews."""

import numpy as np
import os

def write_pcd(filename, points):
    """Write points to PCD file."""
    n = len(points)
    with open(filename, 'w') as f:
        f.write("VERSION .7\n")
        f.write("FIELDS x y z rgb\n")
        f.write("SIZE 4 4 4 4\n")
        f.write("TYPE F F F U\n")
        f.write("COUNT 1 1 1 1\n")
        f.write(f"WIDTH {n}\n")
        f.write("HEIGHT 1\n")
        f.write("VIEWPOINT 0 0 0 1 0 0 0\n")
        f.write(f"POINTS {n}\n")
        f.write("DATA ascii\n")
        for p in points:
            f.write(f"{p[0]:.6f} {p[1]:.6f} {p[2]:.6f} {int(p[3])}\n")

def rgb_to_int(r, g, b):
    """Pack RGB into single int for PCD."""
    return (int(r) << 16) | (int(g) << 8) | int(b)

def generate_noise_sphere(n_points=8000, radius=1.0):
    """Generate a sphere with surface noise — looks like a scanned object."""
    phi = np.pi * (3 - np.sqrt(5))
    indices = np.arange(0, n_points)
    y = 1 - (indices / (n_points - 1)) * 2
    r = np.sqrt(1 - y*y)
    x = np.cos(phi * indices) * r
    z = np.sin(phi * indices) * r
    
    # Surface noise for "scanned" look
    noise = np.random.normal(0, 0.03, n_points)
    points = np.column_stack([x, y, z]) * (radius + noise[:, None])
    
    # Green color with slight variation
    rgb = rgb_to_int(0, 255, 106)
    return np.column_stack([points, np.full(n_points, rgb)])

def generate_terrain(n_points=10000, size=1.0):
    """Generate terrain-like point cloud — architectural/landscape scan."""
    # Grid with Perlin-ish noise
    x = np.random.uniform(-size, size, n_points)
    z = np.random.uniform(-size, size, n_points)
    
    # Height based on noise
    y = (np.sin(x * 3) * np.cos(z * 3) * 0.2 + 
         np.sin(x * 8) * 0.05 + 
         np.cos(z * 6) * 0.05 +
         np.random.normal(0, 0.02, n_points))
    
    # Color by height — green gradient
    y_norm = (y - y.min()) / (y.max() - y.min() + 0.001)
    r = np.zeros(n_points)
    g = 150 + 105 * y_norm  # 150-255
    b = np.full(n_points, 80)
    rgb = np.array([rgb_to_int(r[i], g[i], b[i]) for i in range(n_points)])
    
    return np.column_stack([x, y, z, rgb])

def generate_mechanical_part(n_points=8000):
    """Generate gear-like mechanical part — engineering project."""
    points = []
    
    # Central hub
    for _ in range(n_points // 3):
        theta = np.random.uniform(0, 2*np.pi)
        r = np.random.uniform(0, 0.3)
        z = np.random.uniform(-0.1, 0.1)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        points.append([x, y, z])
    
    # Gear teeth
    n_teeth = 8
    for i in range(n_points * 2 // 3):
        tooth = i % n_teeth
        theta = (tooth / n_teeth) * 2 * np.pi + np.random.uniform(-0.1, 0.1)
        r = np.random.uniform(0.35, 0.5)
        z = np.random.uniform(-0.05, 0.05)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        points.append([x, y, z])
    
    points = np.array(points)
    rgb = rgb_to_int(0, 220, 120)
    return np.column_stack([points, np.full(len(points), rgb)])

def generate_particle_aggregation(n_points=7000):
    """Generate organic blob from particle aggregation — design/art project."""
    # Random walk aggregation
    points = [[0, 0, 0]]
    
    for _ in range(n_points - 1):
        # Pick random existing point as attractor
        attractor = points[np.random.randint(len(points))]
        # Random direction
        direction = np.random.normal(0, 1, 3)
        direction = direction / np.linalg.norm(direction)
        # New point nearby
        distance = np.random.uniform(0.02, 0.08)
        new_point = attractor + direction * distance
        points.append(new_point.tolist())
    
    points = np.array(points)
    # Normalize to center
    points[:, :3] -= points[:, :3].mean(axis=0)
    
    # Blue-green color
    rgb = rgb_to_int(0, 200, 150)
    return np.column_stack([points, np.full(len(points), rgb)])

if __name__ == "__main__":
    output_dir = "/Users/milesbrooks/.openclaw/workspace/pointcloud-viewer/previews"
    os.makedirs(output_dir, exist_ok=True)
    
    print("Generating project preview point clouds...")
    
    # Project 1: Scanned object
    p1 = generate_noise_sphere(8000, 1.0)
    write_pcd(f"{output_dir}/project1.pcd", p1)
    print(f"  project1.pcd — {len(p1)} points (scanned sphere)")
    
    # Project 2: Terrain/landscape
    p2 = generate_terrain(10000, 1.2)
    write_pcd(f"{output_dir}/project2.pcd", p2)
    print(f"  project2.pcd — {len(p2)} points (terrain)")
    
    # Project 3: Mechanical part
    p3 = generate_mechanical_part(8000)
    write_pcd(f"{output_dir}/project3.pcd", p3)
    print(f"  project3.pcd — {len(p3)} points (mechanical gear)")
    
    # Project 4: Organic design
    p4 = generate_particle_aggregation(7000)
    write_pcd(f"{output_dir}/project4.pcd", p4)
    print(f"  project4.pcd — {len(p4)} points (organic blob)")
    
    print(f"\nDone! Files in: {output_dir}/")
