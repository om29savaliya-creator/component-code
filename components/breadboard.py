class PowerRail:
    def __init__(self, total_ports=25):
        self.total_ports = total_ports
        self.voltage = 0.0          # શરુઆતમાં બોર્ડ બંધ છે એટલે 0V
        self.supply_port = None     # કયા પોર્ટમાં સપ્લાય લાગ્યો તે યાદ રાખવા

    def connect_supply(self, port_no, voltage):
        # User 0 થી 24 માંથી ગમે તે પોર્ટમાં પાવર સપ્લાય જોડી શકે છે
        if 0 <= port_no < self.total_ports:
            self.voltage = voltage
            self.supply_port = port_no
        else:
            print(f"Error: Port {port_no} ખોટો છે. (0 થી {self.total_ports - 1} હોવો જોઈએ)")

    def get_voltage_from(self, port_no):
        #User બાકીના કોઈપણ પોર્ટમાંથી પાવર લઈ શકે છે
        if port_no == self.supply_port:
            print(f"Port {port_no} પહેલેથી સપ્લાય માટે રોકાયેલો છે")
        elif 0 <= port_no < self.total_ports:
            return self.voltage
        else:
            print(f"Error: Port {port_no} અસ્તિત્વમાં નથી!")
            return 0.0


rail1 = PowerRail()
rail2 = PowerRail()
rail3 = PowerRail()
rail4 = PowerRail() 


class TerminalRow:
    VALID_PINS = ['A', 'B', 'C', 'D', 'E']

    def __init__(self, row_no):
        self.row_no = row_no
        self.voltage = 0.0
        self.supply_pin = None

    def connect_supply(self, pin, voltage):
        pin = str(pin).upper()

        if pin not in self.VALID_PINS:
            print(f"Error: Row {self.row_no} - Invalid pin '{pin}'. Valid pins are A, B, C, D, E.")
            return False

        if pin == self.supply_pin:
            print(f"Error: Row {self.row_no} - Pin '{pin}' is already connected to the power supply.")
            return False

        self.voltage = voltage
        self.supply_pin = pin
        return True

    def get_voltage_from(self, pin):
        pin = str(pin).upper()

        if pin not in self.VALID_PINS:
            print(f"Error: Row {self.row_no} - Pin '{pin}' does not exist.")
            return None

        if pin == self.supply_pin:
            print(f"Error: Row {self.row_no} - Pin '{pin}' is already occupied by the supply.")
            return None

        return self.voltage


class WorkingBoard:
    def __init__(self, total_rows=30):
        self.total_rows = total_rows
        self.rows = {r: TerminalRow(row_no=r) for r in range(1, total_rows + 1)}

    def connect_supply(self, row, pin, voltage):
        if 1 <= row <= self.total_rows:
            return self.rows[row].connect_supply(pin, voltage)
        else:
            print(f"Error: Row {row} does not exist. Valid rows are 1 to {self.total_rows}.")
            return False

    def get_voltage_from(self, row, pin):
        if 1 <= row <= self.total_rows:
            return self.rows[row].get_voltage_from(pin)
        else:
            print(f"Error: Row {row} does not exist. Valid rows are 1 to {self.total_rows}.")
            return None