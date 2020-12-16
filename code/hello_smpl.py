'''
Copyright 2015 Matthew Loper, Naureen Mahmood and the Max Planck Gesellschaft.  All rights reserved.
This software is provided for research purposes only.
By using this software you agree to the terms of the SMPL Model license here http://smpl.is.tue.mpg.de/license

More information about SMPL is available here http://smpl.is.tue.mpg.
For comments or questions, please email us at: smpl@tuebingen.mpg.de


Please Note:
============
This is a demo version of the script for driving the SMPL model with python.
We would be happy to receive comments, help and suggestions on improving this code
and in making it available on more platforms.


System Requirements:
====================
Operating system: OSX, Linux

Python Dependencies:
- Numpy & Scipy  [http://www.scipy.org/scipylib/download.html]
- Chumpy [https://github.com/mattloper/chumpy]


About the Script:
=================
This script demonstrates a few basic functions to help users get started with using
the SMPL model. The code shows how to:
  - Load the SMPL model
  - Edit pose & shape parameters of the model to create a new body in a new pose
  - Save the resulting body as a mesh in .OBJ format


Running the Hello World code:
=============================
Inside Terminal, navigate to the smpl/webuser/hello_world directory. You can run
the hello world script now by typing the following:
>	python hello_smpl.py

'''

import trimesh
import pyrender
import numpy as np

from smpl_webuser.serialization import load_model

## Load SMPL model (here we load the female model)
m = load_model( './models/basicModel_f_lbs_10_207_0_v1.0.0.pkl' )

## Assign random pose and shape parameters
m.pose[:]  = np.random.rand(m.pose.size) * .2
m.betas[:] = np.random.rand(m.betas.size) * .03

vertices   = m
faces      = m.f

vertex_colors = np.ones([vertices.shape[0], 4]) * [0.3, 0.3, 0.3, 0.9]
tri_mesh = trimesh.Trimesh(vertices, faces, vertex_colors=vertex_colors)

# adding body meshs
mesh = pyrender.Mesh.from_trimesh(tri_mesh)
scene = pyrender.Scene()
scene.add(mesh)

# adding obeserving camera
camera = pyrender.PerspectiveCamera(yfov=np.pi / 3.0, aspectRatio=1.414)
camera_pose = np.eye(4)
camera_pose[:3, 3] = np.array([0, 0, 5])
scene.add(camera, pose=camera_pose)

pyrender.Viewer(scene, use_raymond_lighting=True)

