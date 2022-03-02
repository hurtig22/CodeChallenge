# main.py
import sys
from pathlib import Path

from mesh import Mesh
from common import read_json_mesh_file
from meshed_run import run_json_mesh_file

if __name__ == "__main__":

    # read arguments from command line
    try:
        filename = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <Please provide mesh file!>")

    try:
        number = sys.argv[2]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <Please provide N - number of output view spots!>")

    # checks
    # check: is file available in path?

    my_file = Path(filename)

    try:
        my_abs_path = my_file.resolve(strict=True)
    except FileNotFoundError:
        # doesn't exist
        raise SystemExit(f"Usage: {sys.argv[0]} <Please provide an existing mesh file!>")

    # check: is number an integer?
    try:
        number = int(number)
    except:
        raise SystemExit(f"Usage: {sys.argv[0]} <Please provide N - number of output view spots as an integer!>")

    mesh = Mesh()
    mesh = read_json_mesh_file(my_file)

    view_spots = run_json_mesh_file(mesh, number)
    print(view_spots)
