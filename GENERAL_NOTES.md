# General notes

Conventions:

- Extension for NWChem input file: `.nw`
- Extension for NWChem log file: `.nwo`

Running NWChem:
```
nwchem INPUT.nw
```

## Installation

It is convenient to compile NWChem in the directory where NWChem is going to
be installed rather than compile it in some temporary directory than moving it.
The path for basis set is set using absolute path. Although it is possible to
set the path for basis set in the input file, I found it convenient to leave it
to the default value.


The following script can be used to configure compilation process of NWChem.
This script is intended to be called under NWChem source directory.

```bash
export NWCHEM_TOP=`pwd`
export LARGE_FILES=TRUE
export TCGRSH=/usr/bin/ssh
export NWCHEM_TOP=`pwd`
export NWCHEM_TARGET=LINUX64
export NWCHEM_MODULES="all"
export PYTHONVERSION=2.7
export PYTHONHOME=/usr


# It is important to note that by default nwchem uses 8-bit integers, so we need to use
# -lmkl_intel_ilp64 instead of -lmkl_intel_lp64
export BLASOPT="-L/home/efefer/intel/mkl/lib/intel64/ -lmkl_core -lmkl_sequential -lmkl_intel_ilp64"
#export LIBRARY_PATH="$LIBRARY_PATH:/usr/lib/openmpi/lib:/home/efefer/intel/mkl/lib/intel64/"

export USE_MPI=y
export USE_MPIF=y
export USE_MPIF4=y
export MPI_LOC=/usr/lib/openmpi/lib
export MPI_INCLUDE=/usr/lib/openmpi/include


export LIBMPI="-lmpi -lopen-rte -lopen-pal -ldl -lpthread"
export ARMCI_NETWORK=SOCKETS

cd $NWCHEM_TOP/src

make clean
make nwchem_config
make FC=mpifort 1> make.log 2>make.err

cd $NWCHEM_TOP/contrib
export FC=mpifort
./getmem.nwchem
```

This configuration is tested using `ifort` 17.0.1 and Open MPI 1.10.2.

## DFT options

```
DFT
  direct
  grid nodisk
  noprint "final vectors analysis"
  maxiter 200
  xc b3lyp
end
```

The double quotes sign is important for `noprint` directive to have effect. Without
double quotes, NWChem will still print final vectors analysis (symmetries and
coefficients).

Using the option `grid nodisk` can reduce disk usage, however, it results in slower
calculation (if reading disk is not a bottleneck in the calculation).

Getting total energy (in single-point calculation):
```
grep "DFT energy" LOG
```

### Open shell DFT

Use keyword `odft`.



