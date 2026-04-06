"""
DIGM 131 - Assignment 1: Procedural Scene Builder
==================================================

OBJECTIVE:
    Build a simple 3D scene in Maya using Python scripting.
    You will practice using maya.cmds to create and position geometry,
    and learn to use descriptive variable names.

REQUIREMENTS:
    1. Create a ground plane (a large, flat polygon plane).
    2. Create at least 5 objects in your scene.
    3. Use at least 2 different primitive types (e.g., cubes AND spheres,
       or cylinders AND cones, etc.).
    4. Position every object using descriptive variable names
       (e.g., house_x, tree_height -- NOT x1, h).
    5. Add comments explaining what each section of your code does.

GRADING CRITERIA:
    - [20%] Ground plane is created and scaled appropriately.
    - [30%] At least 5 objects are created using at least 2 primitive types.
    - [25%] All positions/sizes use descriptive variable names.
    - [15%] Code is commented clearly and thoroughly.
    - [10%] Scene is visually coherent (objects are placed intentionally,
            not overlapping randomly).

TIPS:
    - Run this script from Maya's Script Editor (Python tab).
    - Use maya.cmds.polyCube(), maya.cmds.polySphere(), maya.cmds.polyCylinder(),
      maya.cmds.polyCone(), maya.cmds.polyPlane(), etc.
    - Use maya.cmds.move(x, y, z, objectName) to position objects.
    - Use maya.cmds.scale(x, y, z, objectName) to resize objects.
    - Use maya.cmds.rename(oldName, newName) to give objects meaningful names.
"""

import maya.cmds as cmds

# ---------------------------------------------------------------------------
# Clear the scene so we start fresh each time the script runs.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# ---------------------------------------------------------------------------
# Ground Plane
# ---------------------------------------------------------------------------
# Descriptive variables for the ground plane dimensions and position.
ground_width = 50
ground_depth = 50
ground_y_position = 0

ground = cmds.polyPlane(
    name="ground_plane",
    width=ground_width,
    height=ground_depth,
    subdivisionsX=1,
    subdivisionsY=1,
)[0]
cmds.move(0, ground_y_position, 0, ground)

# ---------------------------------------------------------------------------
# Example Object 1 -- a simple building (cube)
# This is provided as an example. Study it, then add your own objects below.
# ---------------------------------------------------------------------------
building_width = 4
building_height = 6
building_depth = 4
building_x = -8
building_z = 5

building = cmds.polyCube(
    name="building_01",
    width=building_width,
    height=building_height,
    depth=building_depth,
)[0]
# Raise the building so its base sits on the ground plane.
cmds.move(building_x, building_height / 2.0, building_z, building)

epic_sphere_width = 5
epic_sphere_height = 8
epic_sphere_depth = 3
epic_sphere_radius = 1
epic_sphere_x = -10
epic_sphere_z = 10

epic_sphere = cmds.polySphere(
    name_="epic_sphere",
    radius=epic_sphere_height,
    depth=epic_sphere_depth,
    height=epic_sphere_height,
    width=epic_sphere_width,
)[0]

cmds.move(
    epic_sphere_x, epic_sphere_height / 2.0, epic_sphere_z, epic_sphere
)

cylinder_building_width = 3
cylinder_building_height = 10
cylinder_building_depth = 4
cylinder_building_radius =5
cylinder_building_x = 8
cylinder_building_z = -5

cylinder_building = cmds.polyCylinder(
    name_="cylinder_building",
    radius=cylinder_building_radius,
    depth=cylinder_building_depth,
    height=cylinder_building_height,
    width=cylinder_building_width,
)[0]

cmds.move(
    cylinder_building_x, cylinder_building_height / 2.0, cylinder_building_z, cylinder_building
)

building_02_width = 6
building_02_height = 12
building_02_depth = 4
building_x = 2
building_z = 3

building_02 = cmds.polyCube(
    name_="building_02",
    width=building_02_width,
    height=building_02_height,
    depth=building_02_depth,
)[0]

cmds.move(
    building_02, building_02_height / 2.0, building_z, building_02
)

magical_cone_radius = 1
magical_cone_width = 2
magical_cone_depth = 3
magical_cone_height = 4
magical_cone_x = 1
magical_cone_z = -1

magical_cone = cmds.polyCone(
    name_="magical_cone",
    radius=magical_cone_radius,
    depth=magical_cone_depth,
    height=magical_cone_height,
    width=magical_cone_width,
)[0]

cmds.move(
    magical_cone, magical_cone_height / 2.0, magical_cone_z, magical_cone
)

# ---------------------------------------------------------------------------
# Frame All -- so the whole scene is visible in the viewport.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.viewFit(allObjects=True)
print("Scene built successfully!")
