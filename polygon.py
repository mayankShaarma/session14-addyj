import math

class Polygon:
    '''
    Polygon class with lazy execution of properties.
    '''
    def __init__(self, edge_count, circumradius):
        self.edge_count = edge_count
        self.circumradius = circumradius

    @property
    def edge_count(self):
        return self._edge_count

    @edge_count.setter
    def edge_count(self, edge_count):
        if not isinstance(edge_count, int):
            raise TypeError("Edge count must be integer...")
        elif edge_count <= 2:
            raise ValueError("Edge count must be greater than 2...")
        else:
            self._edge_count = edge_count
            self._interior_angle = None
            self._edge_length = None
            self._polygon_apothem = None
            self._polygon_area = None
            self._polygon_perimeter = None

    @property
    def vertice_count(self):
        return self._edge_count

    @property
    def circumradius(self):
        return self._circumradius

    @circumradius.setter
    def circumradius(self, circumradius):
        if not isinstance(circumradius, int) and not isinstance(circumradius, float):
            raise TypeError("Circumradius must be int/float...")
        elif circumradius <=0:
            raise ValueError("Circumradius must be positive and in meters...")
        else:
            self._circumradius = circumradius
            self._edge_length = None
            self._polygon_apothem = None

    @property
    def interior_angle(self):
        if self._interior_angle is None:
            print("Running interior_angle")
            self._interior_angle = (self._edge_count - 2) * (180 / self._edge_count)
        return self._interior_angle

    @property
    def edge_length(self):
        if self._edge_length is None:
            print("Running edge_length")
            self._edge_length = 2 * self._circumradius * math.sin(math.pi / self._edge_count)
        return self._edge_length

    @property
    def polygon_apothem(self):
        if self._polygon_apothem is None:
            print("Running polygon_apothem")
            self._polygon_apothem = self._circumradius * math.cos(math.pi / self._edge_count)
        return self._polygon_apothem

    @property
    def polygon_area(self):
        if self._polygon_area is None:
            print("Running polygon_area")
            self._polygon_area = 0.5 * self._edge_count * self.edge_length * self.polygon_apothem
        return self._polygon_area

    @property
    def polygon_perimeter(self):
        if self._polygon_perimeter is None:
            print("Running polygon_perimeter")
            self._polygon_perimeter = self._edge_count * self.edge_length
        return self._polygon_perimeter

    def __str__(self):
        return f'Polygon defined: Vertices={self._edge_count}, Circumradius={self._circumradius}'

    def __repr__(self):
        return f'Polygon defined: Vertices={self._edge_count}, Circumradius={self._circumradius}'

    def __gt__(self, other):
        if not isinstance(other, Polygon):
            raise TypeError("Comparision with non polygon type not allowed...")
        else:
            if self._edge_count > other._edge_count:
                return True
            else:
                return False

    def __eq__(self, other):
        if not isinstance(other, Polygon):
            raise TypeError("Comparision with non polygon type not allowed...")
        else:
            if self._edge_count == other._edge_count and self._circumradius == other._circumradius:
                return True
            else:
                return False
