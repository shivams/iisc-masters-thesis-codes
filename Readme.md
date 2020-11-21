This repo contains various programs I wrote during my Masters thesis on "Reaction Solvability Analysis of Overconstrained Mechanisms using Natural Coordinates":
* `MathematicaNBs` : Mathematica Notebooks which implemented the RSA algorithm on several mechanisms
* `cad_generate.py` : Python code for generating CAD models using FreeCAD, based on the given DH parameters
* `Natural Constraints Formulation.ipynb` : Python code for generating mathematical constraint equations using Natural Coordinates Formulation
* `sympy_quaternions.py` : Sympy based Python library for quaternions (converted from the Numpy based version). This is used in the following notebook for solving the loop closure equation (forward kinematics) of over-constrained mechanisms
* `SymPy Kinematics.ipynb` : Doing kinematics with SymPy. This notebook also demonstrates using the above Sympy-based quaternion library to solve the loop closure equations symbolically 
* `Loop Closure Solving.ipynb` : Solving loop-closure equations numerically using `fsolve`

Bennett Mechanism example generated using Python and rendered in Solidworks:
![Bennett Mechanism generated using Python and rendered in Solidworks](BennettAssembly2.jpg "Bennett Mechanism generated using Python and rendered in Solidworks")
