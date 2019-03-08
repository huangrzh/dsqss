import numpy as np

from .lattice import Interaction, Lattice, Site
from .util import coord2index, get_as_list, index2coord


class HyperCubicLattice(Lattice):
    def __init__(self, param):
        self.dim = param["dim"]
        self.name = "{0} dimensional hypercubic lattice".format(self.dim)
        self.size = get_as_list(param, "L", extendto=self.dim)
        self.sites = []
        self.ints = []

        pbc = get_as_list(param, "periodic", default=True, extendto=self.dim)
        self.bc = list(map(int, pbc))
        bondalt = False

        N = 1
        for L in self.size:
            N *= L
        P = [2] * self.dim
        nboundary = 0
        nstype = 0
        nitype = 0
        for i in range(N):
            ir = index2coord(i, self.size)
            parities = [x % 2 for x in ir]
            if bondalt:
                stype = coord2index(parities, P)
            else:
                stype = 0
            nstype = max(nstype, stype)
            self.sites.append(Site(i, stype, ir))

            for d in range(self.dim):
                jr = ir[:]
                jr[d] += 1
                if jr[d] == self.size[d]:
                    if not pbc[d]:
                        continue
                    jr[d] = 0
                    eid = 1
                else:
                    eid = 0
                j = coord2index(jr, self.size)

                if bondalt:
                    itype = stype * self.dim + d
                else:
                    itype = 0
                nitype = max(nitype, itype)
                Int = Interaction(
                    int_id=len(self.ints),
                    int_type=itype,
                    nbody=2,
                    site_indices=[i, j],
                    edge_flag=eid,
                    direction=d,
                )
                self.ints.append(Int)
        self.latvec = np.eye(self.dim)
        self.directions = []
        for d in range(self.dim):
            latvec = [0] * self.dim
            latvec[d] = 1
            self.latvec[:, d] = latvec
            self.directions.append(latvec)
        self.ndir = len(self.directions)
        self.nsites = len(self.sites)
        self.nints = len(self.ints)
        self.nstypes = nstype + 1
        self.nitypes = nitype + 1
        self.nboundary = nboundary
        self.dirs = np.eye(self.dim).tolist()

        self.update()
