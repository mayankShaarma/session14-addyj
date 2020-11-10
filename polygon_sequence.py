from polygon import Polygon
from functools import lru_cache

class Polygon_Sequence:
    '''
    Polygon Sequence which is both iterable and subcriptable
    '''
    def __init__(self, largest_edge_count, common_circumradius):
        self.largest_edge_count = largest_edge_count
        self.common_circumradius = common_circumradius

    @property
    def largest_edge_count(self):
        return self._largest_edge_count

    @property
    def largest_vertice_count(self):
        return self._largest_edge_count

    @largest_edge_count.setter
    def largest_edge_count(self, largest_edge_count):
        if not isinstance(largest_edge_count, int):
            raise TypeError("Edge count must be integer...")
        elif largest_edge_count <=2:
            raise ValueError("Edge count must be greater than 2...")
        else:
            self._largest_edge_count = largest_edge_count
            self._polygon_max_efficiency = None

    @property
    def common_circumradius(self):
        return self._common_circumradius

    @common_circumradius.setter
    def common_circumradius(self, common_circumradius):
        if not isinstance(common_circumradius, int) and not isinstance(common_circumradius, float):
            raise TypeError("Common circumradius must be int/float...")
        elif common_circumradius <=0:
            raise ValueError("Common circumradius must be positive and in meters...")
        else:
            self._common_circumradius = common_circumradius
            self._polygon_max_efficiency = None

    @property
    def polygon_max_efficiency(self):
        if self._polygon_max_efficiency is None:
            print("Running polygon_max_efficiency")
            valid_polys = []
            for i in range(3, self._largest_edge_count + 1):
                valid_polys.append(Polygon(i, self._common_circumradius))
            self._polygon_max_efficiency = sorted(valid_polys, key= lambda x : x.polygon_area/x.polygon_perimeter)[-1]
        return self._polygon_max_efficiency

    def __iter__(self):
        return self.PolySeqIterator(self.__len__(), self._common_circumradius)

    def __reversed__(self):
        return self.PolySeqIterator(self.__len__(), self._common_circumradius, reverse=True)

    class PolySeqIterator:
        def __init__(self, length, common_circumradius, reverse=False):
            self._index = 0
            self._length = length
            self._common_circumradius = common_circumradius
            self._reverse = reverse

        def __iter__(self):
            return self

        def __next__(self):
            if self._index >= self._length:
                raise StopIteration
            else:
                if self._reverse:
                    idx_element = self._length -1 - self._index
                else:
                    idx_element = self._index

                self._index += 1
                return Polygon_Sequence._sequence_element(idx_element, self._common_circumradius)

    def __len__(self):
        return self._largest_edge_count - 2

    def __repr__(self):
        return f'Polygon Sequence (Vertices of largest polygon) = {self._largest_edge_count}, Common Circumradius = {self._common_circumradius}'

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0:
                index = self.__len__() + index
            if index < 0 or index >= self.__len__():
                raise IndexError("Index Not Found...")
            else:
                return Polygon_Sequence._sequence_element(index, self._common_circumradius)
        else:
            start, stop, step = index.indices(self.__len__())
            elements = range(start, stop, step)
            return [Polygon_Sequence._sequence_element(index, self._common_circumradius) for index in elements]
    

    @staticmethod
    @lru_cache(2**10)
    def _sequence_element(idx, com_rad):
        return Polygon(idx + 3, com_rad)
