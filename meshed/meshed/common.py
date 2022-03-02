def read_json_mesh_file(json_file):
    """reads json file and returns dictionaries of nodes, elements and values

    Args:
        json_file: file containing json data

    Returns:
        mesh: Mesh object
    """
    from pathlib import Path
    from mesh import Mesh
    import json

    # Opening JSON file
    try:
        f = open(json_file)
    except FileNotFoundError:
        # doesn't exist
        raise SystemExit(f"<Mesh file was not found!>")

    # returns JSON object as
    # a dictionary
    try:
        data = json.load(f)
    except:
        f.close()
        raise SystemExit(f"<Data from mesh file could not be loaded!>")

    # check if json files contains all data types
    try:
        mesh = Mesh()
        mesh.nodes = data['nodes']
        mesh.elements = data['elements']
        mesh.values = data['values']
    except:
        f.close()
        raise SystemExit(f"<There is something wrong with the mesh file!>")

    # Closing file
    f.close()

    return mesh
