#ifndef SYSTEMPARAM_H
#define SYSTEMPARAM_H

#define VAL 10
#define INF 1.0e+14
#define EPS 1.0e-14

struct Size {
  int x;        //the number of lattice for x.
  int y;        //the number of lattice for y.
  int z;        //the number of lattice for z.
  int V;        //the total number of lattice.
  int d;        //dimension.
  double B;     //the inverse of temperature.
  double oldB;  //for annealing.
};

struct System {
  int nmax;    // the maximum number of bosons on a same site.
  double Ubb;  //on-site interaction.
  double Vb1;  // nearest-neighbor interaction.
  double tb;   // hopping
  double mu;   // chemical potential.
  int w_num;   //
  double Htr;  // the strenght of the transverse field for introducing worm.
  double Eu;   // arbitrary energy shift for Ubb.
  double Et;   // arbitrary energy shift for t-Vb1.
};

struct MC_p {
  int seed;
  int Nstep;
  int Nthermal;
  int Nsample;
  int Nbin;
  int Ntest;
  int nc;
  int runtype; //{0: normal, 1:restart, 2:annealing}
};

struct Parallel {
  int p_num;                       // the total number of processors.
  int my_rank;                     // the rank of each proseccor.
  int Ntdiv;                       // the number of the temporal decomposition.
  int Nsdiv, Nxdiv, Nydiv, Nzdiv;  // the number of the spatial decomposition. (total, x, y, z)
  int NtNs;                        // the number of domain decomposition.
  int Npara;                       // the number of trivial parallelization.
  double B;                        // beta of "a domain".
  double oldB;                     // for annealing.
  bool FlgAnneal;                  // for annealing.
  bool FlgRestart;                 // for restart.

  int x, y, z, V;  // the coordinate number.

  // process numbers
  int np; // index for random number parallelization
  int Rpara; // the number of replica (random system)
  int nq; // index for random system (random number parallelization)
  int nr; // index for random system (replica)

  /*
  // a random potential number (one of trivial parallelization)
    PR.nr = PR.np % PR.Rpara; 
  // a seed number of the trivial parallelization for the random potential (one of trivial parallelization)
    PR.nq = PR.np / PR.Rpara;  
        */

  // domain information
  int nst; // domain index
  int nt; // along imaginary time
  int ns; // along space
  int nx; // x
  int ny; // y
  int nz; // z

  // process id for origin domain
  int nst0; // sharing np
  int nt0;  // sharing np, ns
  int ns0;  // sharing np, nt
  int nx0;

  // process id for neighbor domains
  int upper;
  int lower;
  int right[3];
  int left[3];
};

#endif
