#!/usr/bin/env python
r"""
Equation of state
=================

Flow to compute the equation of state by fitting E(V) at T = 0.
"""
import sys
import os
import abipy.data as abidata
import abipy.abilab as abilab
import abipy.flowtk as flowtk
import abipy.core.abinit_units as abu
import numpy as np

def make_input(structure, pseudos):

   scf_input = abilab.AbinitInput(structure, pseudos)

   scf_input.set_vars(
         ecut=42.0,
         nstep=500,
         nsppol=1,
         occopt=3,
         shiftk=[0.0,    0.0,    0.0],
         tolvrs=1e-10,
         ngkpt=[84, 84, 84],
         kptopt=1,
         nshiftk=1,
         ##############################################
         ####                SECTION: files
         ##############################################
         #pseudos "H.psp8"
         #pp_dirpath "./pseudo/"
         ##############################################
         ####               SECTION: gstate
         ##############################################
         fband=1.5,
         tsmear=0.00225,
         chkprim=0,
         nspinor=1,
         rmm_diis=0,
         chksymbreak=0,
         ##############################################
         ####                SECTION: paral
         ##############################################
         #autoparal 1
         ##############################################
         ####                 SECTION: rlx
         ##############################################
         ecutsm=0.0,
         ionmov=0,
         tolmxf=5e-05,
         dilatmx=1.0,
         optcell=0,
         restartxf=0
         ##############################################
         ####                  STRUCTURE
         ##############################################
         #natom 2
         #ntypat 1
         #typat 1 1
         #znucl 1
         #xred
         #   0.0000000000    0.0000000000    0.0000000000
         #   0.5000000000    0.5000000000    0.5000000000
         #acell    1.0    1.0    1.0
         #rprim
         #   3.4200402307    0.0000000000    0.0000000000
         #   0.0000000000    3.4200402307    0.0000000000
         #   0.0000000000    0.0000000000    3.4200402307
   )

   return scf_input


def build_flow(options):
    # Set working directory (default is the name of the script with '.py' removed and "run_" replaced by "flow_")
    if not options.workdir:
        options.workdir = os.path.basename(sys.argv[0]).replace(".py", "").replace("run_", "flow_")

    pseudos = "H.psp8"

    structure = abilab.Structure.from_abistring("""
         natom 2
         ntypat 1
         typat 1 1
         znucl 1
         xred
            0.0000000000    0.0000000000    0.0000000000
            0.5000000000    0.5000000000    0.5000000000
         acell    1.0    1.0    1.0
         rprim
            3.4200402307    0.0000000000    0.0000000000
            0.0000000000    3.4200402307    0.0000000000
            0.0000000000    0.0000000000    3.4200402307"""
    )

    #print(structure)
    #print("volume / natom:", structure.lattice.volume / len(structure))
    #print("volume:", structure.lattice.volume * abu.Ang_Bohr ** 3)

    ae_vols = np.array([
        2.7860886995203789e+00,
        2.8453674250933840e+00,
        2.9046447700159037e+00,
        2.9639258864197213e+00,
        3.0232019324332353e+00,
        3.0824810521279016e+00,
        3.1417596643230516e+00,
    ]) * len(structure)

    struct_list = [structure.scale_lattice(vol) for vol in ae_vols]

    # from abipy.flowtk.gs_works import EosWork
    flow = flowtk.Flow(options.workdir, manager=options.manager)
    work = flow.new_work()

    for i, s in enumerate(struct_list):
        #print(s)
        print("volume    / natom:", s.lattice.volume / len(s))
        print("ae volume / natom:", ae_vols[i] / len(s))
        if i  == 3:
            print(s.abi_string)
            print(structure.abi_string)
        work.register_scf_task(make_input(s, pseudos))

    #sys.exit(1)

    return flow


@flowtk.flow_main
def main(options):
    """
    This is our main function that will be invoked by the script.
    flow_main is a decorator implementing the command line interface.
    Command line args are stored in `options`.
    """
    return build_flow(options)


if __name__ == "__main__":
    sys.exit(main())
