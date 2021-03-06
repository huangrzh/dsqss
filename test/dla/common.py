import os
import subprocess as sub
import sys

import dsqss
import dsqss.dla_pre
import numpy as np
import scipy.stats as stats


def p_value(X, E, N, Y):
    if E == 0.0:
        if X == Y:
            t = 0.0
        else:
            t = float("inf")
    else:
        t = (X - Y) / E
    return 2 * stats.t.cdf(-np.abs(t), N - 1)


def cleanup(name=""):
    if name != "":
        name = "_{0}".format(name)
    for prefix, suffix in [
        ("hamiltonian", ".xml"),
        ("algorithm", ".xml"),
        ("lattice", ".xml"),
        ("wavevector", ".xml"),
        ("displacement", ".xml"),
        ("res", ".dat"),
        ("sf", ".dat"),
        ("cf", ".dat"),
        ("ck", ".dat"),
        ("cjob.res", ".dat"),
    ]:
        fname = "{0}{1}{2}".format(prefix, name, suffix)
        if os.path.exists(fname):
            os.remove(fname)


def geninp(param, seed, simtime=0.0, name=""):
    if name != "":
        name = "_{0}".format(name)
    p = param["parameter"]
    p["latfile"] = "lattice{0}.xml".format(name)
    p["algfile"] = "algorithm{0}.xml".format(name)
    p["outfile"] = "res{0}.dat".format(name)
    p["wvfile"] = "wv{0}.xml".format(name)
    p["dispfile"] = "dp{0}.xml".format(name)
    p["sfoutfile"] = "sf{0}.dat".format(name)
    p["cfoutfile"] = "cf{0}.dat".format(name)
    p["ckoutfile"] = "ck{0}.dat".format(name)
    p["seed"] = seed
    p["simulationtime"] = simtime

    dsqss.dla_pre.dla_pre(param, "qmc{0}.inp".format(name))


def run(exename, BINDIR=".", name=""):
    if name != "":
        name = "_{0}".format(name)

    retval = sub.call(["{0}/{1}".format(BINDIR, exename), "qmc{0}.inp".format(name)])
    if retval != 0:
        sys.exit(retval)


def read_result(filename):
    res = {}
    with open(filename) as f:
        for line in f:
            if not line.startswith("R"):
                continue
            words = line.split()
            res[words[1]] = tuple(map(float, words[3:5]))
    return res
