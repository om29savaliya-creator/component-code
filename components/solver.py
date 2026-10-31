# =============================================================================
# solver.py  —  Layer 3: Circuit Solver (Analysis Engine)
# =============================================================================
# The brain of the simulation. Takes the full circuit (nodes + components)
# and computes voltage at every node and current through every component.
#
# Uses Nodal Analysis based on Kirchhoff's Current Law (KCL):
#   "The sum of all currents entering a node = 0"
#
# This is the same method used by professional circuit simulators like SPICE.
# =============================================================================


# TODO: Build Layer 3 — Circuit Solver
#
# Planned class:
#
#   CircuitSolver
#       Input:
#           - nodes      : all electrical nodes in the circuit
#           - components : all placed components with their connections
#           - ground     : one node designated as 0V reference (GND)
#
#       Process:
#           Step 1 → Build conductance matrix (G matrix) from all components
#           Step 2 → Build current source vector (I vector) from voltage sources
#           Step 3 → Solve the linear system:  G * V = I
#                    (using numpy or pure Python Gaussian elimination)
#           Step 4 → Extract node voltages from the solution vector V
#           Step 5 → Back-calculate current through each component
#
#       Output:
#           - node_voltages  : { node_id → voltage in Volts }
#           - branch_currents: { component_id → current in Amps }
#           - power          : { component_id → power in Watts }
#
#   Key rules applied:
#       - Kirchhoff's Voltage Law (KVL) : sum of voltages in any loop = 0
#       - Kirchhoff's Current Law (KCL) : sum of currents at any node = 0
#       - Ohm's Law                     : V = I * R

