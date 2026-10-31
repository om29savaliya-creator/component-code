# =============================================================================
# breadboard.py  —  Layer 1: Connectivity Model
# =============================================================================
# Defines the physical structure and node connectivity of the breadboard.
# This layer answers ONE question only:
#   "Which physical pins are electrically connected to which node?"
#
# NO voltage, NO current, NO component logic lives here.
# Voltage is computed by the Circuit Solver (solver.py — Layer 3).
# =============================================================================


class Node:
    """
    Represents a single electrical node on the breadboard.
    A node is any group of points directly connected together (zero resistance).
    Tracks which physical holes are occupied (have a wire/leg plugged in).
    """

    def __init__(self, node_id):
        self.node_id = node_id
        self.occupied_pins = set()      # physical holes currently in use

    def occupy(self, pin_label):
        """Mark a hole as physically occupied (wire or component leg plugged in)."""
        if pin_label in self.occupied_pins:
            print(f"Error: Pin '{pin_label}' on node '{self.node_id}' is already occupied.")
            return False
        self.occupied_pins.add(pin_label)
        return True

    def free(self, pin_label):
        """Free a hole (wire or component leg removed)."""
        self.occupied_pins.discard(pin_label)

    def is_occupied(self, pin_label):
        """Check if a specific hole is currently occupied."""
        return pin_label in self.occupied_pins

    def __repr__(self):
        return f"Node(id='{self.node_id}', occupied={self.occupied_pins})"


# =============================================================================

class PowerRail:
    """
    Represents a power rail — the long +/- strips on the sides of the breadboard.
    The entire rail is ONE electrical node (all ports are shorted together).
    Stores NO voltage — voltage is assigned externally by the Circuit Solver.
    """

    TOTAL_PORTS = 25

    def __init__(self, rail_id):
        self.rail_id = rail_id
        self.node = Node(node_id=f"rail_{rail_id}")

    def plug_in(self, port_no):
        """
        Physically occupy a port (plug a wire or component leg into this rail).
        Returns the Node this port belongs to, or None on error.
        """
        if not (0 <= port_no < self.TOTAL_PORTS):
            print(f"Error: Rail '{self.rail_id}' - Port {port_no} invalid. Valid: 0 to {self.TOTAL_PORTS - 1}.")
            return None
        success = self.node.occupy(port_no)
        return self.node if success else None

    def unplug(self, port_no):
        """Free a port (remove wire or component leg from this rail)."""
        self.node.free(port_no)

    def get_node(self):
        """Return the electrical node this entire rail represents."""
        return self.node

    def __repr__(self):
        return f"PowerRail(id='{self.rail_id}', node={self.node})"


# =============================================================================

class Breadboard:
    """
    Represents the main working area of the breadboard.
    Maps pin IDs like '3C' or '14A' to their electrical nodes (rows).

    Physical rule:
        All 5 pins in a row (A, B, C, D, E) belong to the SAME node.
        '3A', '3B', '3C', '3D', '3E' → all same node → row_3

    This class stores NO voltage — it is a pure connectivity model.
    """

    VALID_PINS = ['A', 'B', 'C', 'D', 'E']
    TOTAL_ROWS = 30

    def __init__(self):
        # Each row is an independent electrical node
        self.nodes = {
            r: Node(node_id=f"row_{r}")
            for r in range(1, self.TOTAL_ROWS + 1)
        }

    # ------------------------------------------------------------------
    # Internal helper
    # ------------------------------------------------------------------

    def _parse_pin_id(self, pin_id):
        """
        Parse a pin ID string like '4C' into (row=4, pin='C').
        Returns (None, None) if the pin ID is invalid.
        """
        pin_id = str(pin_id).strip().upper()
        letter   = pin_id[-1]       # last character  → pin letter
        row_part = pin_id[:-1]      # everything else → row number

        if not row_part.isdigit():
            print(f"Error: '{pin_id}' — '{row_part}' is not a valid row number.")
            return None, None

        row = int(row_part)

        if row not in self.nodes:
            print(f"Error: Row {row} does not exist. Valid rows: 1 to {self.TOTAL_ROWS}.")
            return None, None

        if letter not in self.VALID_PINS:
            print(f"Error: '{pin_id}' — '{letter}' is not a valid pin. Valid: A, B, C, D, E.")
            return None, None

        return row, letter

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def plug_in(self, pin_id):
        """
        Physically occupy a pin hole (plug a wire or component leg in).
        Returns the Node this pin belongs to, or None on failure.
        """
        row, pin = self._parse_pin_id(pin_id)
        if row is None:
            return None
        node = self.nodes[row]
        success = node.occupy(pin)
        return node if success else None

    def unplug(self, pin_id):
        """Free a pin hole (remove a wire or component leg)."""
        row, pin = self._parse_pin_id(pin_id)
        if row is None:
            return
        self.nodes[row].free(pin)

    def get_node(self, pin_id):
        """
        Return the electrical Node that this pin ID belongs to.
        Used by the Circuit Solver to build the network.
        """
        row, pin = self._parse_pin_id(pin_id)
        if row is None:
            return None
        return self.nodes[row]

    def is_occupied(self, pin_id):
        """Check whether a specific pin hole is physically occupied."""
        row, pin = self._parse_pin_id(pin_id)
        if row is None:
            return False
        return self.nodes[row].is_occupied(pin)

    def __repr__(self):
        return f"Breadboard(rows={self.TOTAL_ROWS}, valid_pins={self.VALID_PINS})"
