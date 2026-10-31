# =============================================================================
# components.py  —  Layer 2: Component Definitions
# =============================================================================
# Defines all electronic components that can be placed on the breadboard.
# Each component connects between TWO electrical nodes and has its own
# physical/electrical properties.
#
# Components do NOT compute voltage or current themselves.
# They just describe WHAT they are and WHERE they connect.
# The Circuit Solver (solver.py — Layer 3) uses this info to run analysis.
# =============================================================================


# TODO: Build Layer 2 — Component Definitions
#
# Planned classes:
#
#   Component (base class)
#       - node_a      : first connection node
#       - node_b      : second connection node
#       - pin_a       : physical pin ID where node_a is plugged in  (e.g. "3C")
#       - pin_b       : physical pin ID where node_b is plugged in  (e.g. "5A")
#
#   ├── VoltageSource (e.g. battery, power supply)
#   │       - voltage    : supply voltage in Volts (e.g. 5.0)
#   │       - polarity   : which node is + and which is -
#   │
#   ├── Resistor
#   │       - resistance : value in Ohms (e.g. 1000 for 1kΩ)
#   │
#   ├── LED
#   │       - forward_voltage : voltage drop when conducting (e.g. 2.0V)
#   │       - color           : for game display purposes
#   │
#   ├── Capacitor
#   │       - capacitance : value in Farads (e.g. 0.0001 for 100µF)
#   │
#   ├── Switch
#   │       - is_closed   : True = wire, False = open circuit (no connection)
#   │
#   └── Wire
#           - zero resistance, directly connects two nodes

