#Game mechanics
board_modular = False

#Windowing
screen_size = [800,600]
multisample = 16

#Appearance

board_colors = [
    [1.0,0.0,0.0, 1.0],
    [0.8,0.3,0.0, 1.0],
    [0.2,0.0,1.0, 1.0],
    [0.0,0.5,0.8, 1.0]
]

which_camera = 3
if which_camera == 1:
    camera_radius_def = 15.0
    camera_fov = 45.0
    spacing = 2.0
elif which_camera == 2:
    camera_radius_def = 30.0
    camera_fov = 20.0
    spacing = 2.0
elif which_camera == 3:
    camera_radius_def = 30.0
    spacing = 4.0
camera_rot_def = [150.0,35.0]#[170.0,20.0]
camera_center_def = [2.0,1.5*spacing,2.0]

camera_radius = camera_radius_def
camera_rot = list(camera_rot_def)
camera_center = list(camera_center_def)
