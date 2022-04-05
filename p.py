#!/usr/bin/env python
import sys
import json
import numpy as np

def main():

    ae_vols, ae_enes = np.loadtxt("ae_eos.txt").T
    #print(ae_vols)

    #eos_json = sys.argv[1]
    #with open(eos_json, "rt") as fh:
    #    data = json.load(fh)
    #    abi_vols = data["volumes_ang3"]
    #    abi_enes = data["energies_ev"]


    from abipy.tools.plotting import (set_axlims, add_fig_kwargs, get_ax_fig_plt, get_axarray_fig_plt)
    ax, fig, plt = get_ax_fig_plt()
    ax.plot(ae_vols, ae_enes - ae_enes.min(), color="red", marker="o", label="AE")

    #ax.plot(abi_vols, abi_enes - abi_enes.min(), color="blue", marker="x", label="Abinit")

    ax.set_ylabel('Energy (eV)')
    ax.set_xlabel('Volume')
    ax.legend(loc="best", shadow=True)
    ax.grid(True)
    plt.show()






if __name__ == "__main__":
    sys.exit(main())
