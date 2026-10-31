# =============================================================================
# lab.py  —  Master Interface: Electronics Lab
# =============================================================================
# The top-level API for the simulation game.
# Ties all three layers together and exposes simple methods for the game engine.
#
# The game only talks to this file — it never touches breadboard.py,
# components.py or solver.py directly.
# =============================================================================


# TODO: Build lab.py — Master Interface
#
# Planned class:
#
#   ElectronicsLab
#       Owns:
#           - one Breadboard  (from breadboard.py)
#           - four PowerRails (from breadboard.py)
#           - a list of placed Components (from components.py)
#           - one CircuitSolver (from solver.py)
#
#       Game-facing API:
#
#           place_component(pin_a, pin_b, component)
#               → plugs component between two pin IDs on the breadboard
#               → e.g. place_component("3C", "5A", Resistor(1000))
#
#           remove_component(component_id)
#               → unplugs and removes a component
#
#           connect_rail(rail_id, port_no, pin_id)
#               → connects a power rail port to a breadboard pin via a wire
#
#           solve()
#               → triggers CircuitSolver to analyse the full circuit
#               → updates all node voltages and component currents
#
#           get_voltage(pin_id)
#               → returns computed voltage at a pin (after solve())
#
#           get_current(component_id)
#               → returns current through a component (after solve())
#
#           get_circuit_state()
#               → returns full snapshot of the circuit for the game UI

