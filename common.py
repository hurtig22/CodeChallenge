def read_json_mesh_file(json_file):
    """reads json file and returns dictionaries of nodes, elements and values
    
    Args:
        json_file: file containing json data
        
    Returns:
        nodes: dictionary
        elements: dictionary
        values: dictionary
    """
    import json
    # get file handle
    f = open(json_file)
    # load data
    data = json.load(f)
    
    # get dicts from data
    nodes = data['nodes']
    elements = data['elements']
    values = data['values']
    
    # close filehandle
    f.close()
    
    return (nodes,elements,values)