import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from astropy.coordinates import SkyCoord
from astropy import units as u
from astropy.coordinates import EarthLocation, AltAz, get_sun
from astropy.time import Time

# Define observer's location and observation time
observer_location = EarthLocation(lat=-20.0*u.deg, lon=20.0*u.deg, height=0.0*u.m)
observation_time = Time('2023-10-09T18:00:00', format='isot', scale='utc')
#elapsed = np.arange(0,24*60, 5)*u.min

# Define a set of equatorial coordinates (RA and Dec) for demonstration
ra_values = np.array([10, 20, 30, 40, 50])  # Right Ascension in degrees
dec_values = np.array([10, 20, 30, 40, 50])  # Declination in degrees

# Convert equatorial coordinates to horizontal coordinates (Altitude and Azimuth)
altaz_frame = AltAz(obstime=observation_time, location=observer_location)
equatorial_coordinates = SkyCoord(ra=ra_values*u.deg, dec=dec_values*u.deg, frame='icrs')
horizontal_coordinates = equatorial_coordinates.transform_to(altaz_frame)

# Create the sky map using Matplotlib
#plt.figure(figsize=(10, 6))
#plt.scatter(horizontal_coordinates.az, horizontal_coordinates.alt, s=20, c='b', marker='o')


# Create the sky map using Matplotlib
fig, ax = plt.subplots(figsize=(10, 10))
border = plt.Circle((0, 0), 100, color='navy', fill=True)
ax.add_patch(border)
ax.scatter(horizontal_coordinates.az, horizontal_coordinates.alt, s=20, c='w', marker='o')
horizon = plt.Circle((0, 0), radius=100, transform=ax.transData)
for col in ax.collections:
    col.set_clip_path(horizon)
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)

plt.xlabel('Azimuth (degrees)')
plt.ylabel('Altitude (degrees)')
plt.title('Sky Map')
plt.grid()

# Customize by adding labels for the plotted points
for i, label in enumerate(["Star 1", "Star 2", "Star 3", "Star 4", "Star 5"]):
    plt.annotate(label, (horizontal_coordinates.az[i].value, horizontal_coordinates.alt[i].value), textcoords="offset points", xytext=(0, 10), ha='center')

plt.show()