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

class ConnectionZone:
    """
    Base class for any connectable area (Breadboard, PowerRail, etc.).
    Centralizes common plug, unplug, query, and lookup operations.
    Subclasses only need to implement `_resolve(target)` to map an input
    address (such as '3C' or port 0) to a (Node, pin_label) pair.
    """

    def _resolve(self, target):
        """
        Translates a physical address into (Node, pin_label).
        Must be implemented by subclasses. Returns (None, None) on validation failure.
        """
        raise NotImplementedError("Subclasses must implement _resolve()")

    def plug_in(self, target):
        """
        Physically occupy a pin hole or port.
        Returns the Node this connection belongs to, or None on failure.
        """
        node, label = self._resolve(target)
        if node is None:
            return None
        return node if node.occupy(label) else None

    def unplug(self, target):
        """Free a pin hole or port."""
        node, label = self._resolve(target)
        if node is not None:
            node.free(label)

    def is_occupied(self, target):
        """Check whether a specific hole or port is occupied."""
        node, label = self._resolve(target)
        if node is None:
            return False
        return node.is_occupied(label)

    def get_node(self, target):
        """Return the electrical Node that this target address connects to."""
        node, _ = self._resolve(target)
        return node


# =============================================================================

class PowerRail(ConnectionZone):
    """
    Represents a power rail — the long +/- strips on the sides of the breadboard.
    The entire rail is ONE electrical node (all ports are shorted together).
    Stores NO voltage — voltage is assigned externally by the Circuit Solver.
    """

    TOTAL_PORTS = 25

    def __init__(self, rail_id):
        self.rail_id = rail_id
        self.node = Node(node_id=f"rail_{rail_id}")

    def _resolve(self, port_no):
        """Maps a port number (0 to 24) to the rail's single Node."""
        if not (0 <= port_no < self.TOTAL_PORTS):
            print(f"Error: Rail '{self.rail_id}' - Port {port_no} invalid. Valid: 0 to {self.TOTAL_PORTS - 1}.")
            return None, None
        return self.node, port_no

    def __repr__(self):
        return f"PowerRail(id='{self.rail_id}', node={self.node})"


# =============================================================================

class Breadboard(ConnectionZone):
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

    def _resolve(self, pin_id):
        """
        Parses and validates a pin ID string like '4C' into (Node, pin_letter).
        Returns (None, None) if the address is invalid.
        """
        pin_id = str(pin_id).strip().upper()
        letter = pin_id[-1]         # last character  → pin letter
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

        return self.nodes[row], letter

    def __repr__(self):
        return f"Breadboard(rows={self.TOTAL_ROWS}, valid_pins={self.VALID_PINS})"
