# This example is meant to be used from within the CadQuery module of FreeCAD.
import cadquery as cq
from Helpers import show

#DH Parameters
a = 10.0
alpha = 30 #Angle in Degrees
d = 2.0 #0 for Bennett mechanism

joint_radius = a/50.0
joint_length = a/10.0
link_radius = a/100.0

#.faces selects using local axis, I think
if d > 0:
    result = cq.Workplane("front").workplane() \
                .circle(joint_radius) \
                .extrude(joint_length) \
                .workplane() \
                .transformed(rotate=(0, 90, 0)) \
                .circle(link_radius) \
                .extrude(a) \
                .faces(">X") \
                .workplane() \
                .transformed(rotate=(0, 90, 0)) \
                .transformed(rotate=(alpha, 0, 0)) \
                .circle(link_radius) \
                .extrude(d) \
                .faces(">X") \
                .workplane() \
                .transformed(offset=(0, 0, -d)) \
                .circle(joint_radius) \
                .extrude(joint_length/2, both=True)

else:
    result = cq.Workplane("front").workplane() \
                .circle(joint_radius) \
                .extrude(joint_length) \
                .workplane() \
                .transformed(rotate=(0, 90, 0)) \
                .circle(link_radius) \
                .extrude(a) \
                .faces(">X") \
                .workplane() \
                .transformed(rotate=(0, 90, 0)) \
                .transformed(rotate=(alpha, 0, 0)) \
                .circle(joint_radius) \
                .extrude(joint_length/2, both=True)



'''
result = cadquery.Workplane("front").box(4.0, 4.0, 0.25).faces(">Z") \
                 .workplane() \
                 .transformed(offset=(0, -1.5, 1.0), rotate=(60, 0, 0)) \
                 .rect(1.5, 1.5, forConstruction=True).vertices().hole(0.25)
'''

# Render the solid
show(result)
