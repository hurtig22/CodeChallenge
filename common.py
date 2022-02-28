def read_json_mesh_file(json_file):
    """reads json file and returns dictionaries of nodes, elements and values
    
    Args:
        json_file: file containing json data
        
    Returns:
        mesh: Mesh object
    """
    import mesh
    import json
 
    # Opening JSON file
    f = open(json_file)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    mesh = Mesh()
    mesh.nodes = data['nodes']
    mesh.elements = data['elements']
    mesh.values = data['values']

    # Closing file
    f.close()
    
    return mesh