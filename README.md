# beam bending stress calculator
this repository contains a python script designed to compute the normal bending stress, maximum bending moment, and area moment of inertia for a simply supported beam under a central point load.

## governing engineering equations
1. area moment of inertia (rectangular cross-section):
   i = (b * h^3) / 12
2. maximum bending moment:
   m_max = (f * l) / 4
3. maximum bending stress:
   sigma_max = (m * y) / i

## how to run
make sure you have python installed, then run the following command in your terminal:
python beam_stress_calculator.py

## input & output parameters
- inputs: applied force f (n), beam length l (mm), width b (mm), height h (mm)
- outputs: max bending moment m_max (n.m), moment of inertia i (mm^4), max stress sigma_max (mpa)
