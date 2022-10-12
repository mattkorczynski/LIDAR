import pandas as pd
import matplotlib.pyplot as plt
import pathlib
import os
import numpy as np
# Functions from @Mateen Ulhaq and @karlo
def set_axes_equal(ax: plt.Axes):
    """Set 3D plot axes to equal scale.

    Make axes of 3D plot have equal scale so that spheres appear as
    spheres and cubes as cubes.  Required since `ax.axis('equal')`
    and `ax.set_aspect('equal')` don't work on 3D.
    """
    limits = np.array([
        ax.get_xlim3d(),
        ax.get_ylim3d(),
        ax.get_zlim3d(),
    ])
    origin = np.mean(limits, axis=1)
    radius = 0.5 * np.max(np.abs(limits[:, 1] - limits[:, 0]))
    _set_axes_radius(ax, origin, radius)

def _set_axes_radius(ax, origin, radius):
    x, y, z = origin
    ax.set_xlim3d([x - radius, x + radius])
    ax.set_ylim3d([y - radius, y + radius])
    ax.set_zlim3d([z - radius, z + radius])

# load data to dataframe
path = os.path.join(pathlib.Path(__file__).parent.resolve(), '2022-10-12-08-25-25_Velodyne-VLP-16-Data.csv')
print(pathlib.Path(__file__).parent.resolve())
data = pd.read_csv(
    path, 
    sep=',',
    error_bad_lines=False)
data['azimuth']=data['azimuth'].astype(int)
print(data['azimuth'].dtypes)
data_limited = data[(data['laser_id']==15)]
print(data_limited.tail())
# prepare plot
fig_3d = plt.figure(figsize=(7, 7), dpi=100)
ax_3d= fig_3d.add_subplot(111, projection='3d')
# ax_3d_1= fig_3d.add_subplot(111, projection='3d')
# ax_3d_1.scatter(data['Points_m_XYZ:0'], 
#     data['Points_m_XYZ:1'], 
#     data['Points_m_XYZ:2'], 
#     c=data['intensity'], 
#     cmap="seismic", 
#     marker='o',
#     s=2)
# ax_3d_1.set_box_aspect([1,1,1])
# set_axes_equal(ax_3d_1)

ax_3d.scatter(data_limited['Points_m_XYZ:0'], 
    data_limited['Points_m_XYZ:1'], 
    data_limited['Points_m_XYZ:2'], 
    c=data_limited['intensity'], 
    cmap="gist_rainbow", 
    marker='o',
    s=2)
ax_3d.set_box_aspect([1,1,1]) # IMPORTANT - this is the new, key line

# ax.set_proj_type('ortho') # OPTIONAL - default is perspective (shown in image above)
set_axes_equal(ax_3d) # IMPORTANT - this is also required

print(data.head(n=20))
plt.show()

