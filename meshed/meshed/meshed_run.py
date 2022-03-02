def run_json_mesh_file(mesh, N):
    """reads json file and runs to find view spots and
        returns list of view spots

    Args:
        json_file: file containing json data

    Returns:
        sorted_spots: list of view spots
    """

    def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
        """reads two float values and checks if they are close
            to each other to a certain precision

        Args:
            a, b: float values

        Returns:
            True or False
        """
        return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

    def combine_lists_and_remove_duplicates(list1, list2):
        newlist = list1 + list(set(list2) - set(list1))
        return newlist

    elements = mesh.get_elements()
    nodes = mesh.get_nodes()
    values = mesh.get_values()

    # {element_id: element_id1, value: <number value>},
    spots = []

    # list of elementids not to be seen again
    donotlookAt = []

    for element in elements:

        # get element_id
        id = element['id']

        # get nodes from element
        element_nodes = element['nodes']
        #print(element_nodes)

        # for each of 3 nodes find neigbors = element IDs; append all in one list
        list_all_new = []
        for en in element_nodes:
            list_new = [ ele['id'] for ele in elements if ( en in ele['nodes'])]
            list_all_new=list(set().union(list_all_new,list_new))

        # element_id = id is also found, so remove that one
        list_all_new.remove(id)

        # get values for element IDs in second list
        values_new = [ {'element_id': val['element_id'], 'value' : val['value']}
                  for  val in values if (val['element_id'] in list_all_new)]

        # get value for element_id = id
        value_node =[ val['value'] for  val in values if (val['element_id'] == id)][0]

        # compare value in element (value_node) to max of all neigbor values (values_new)
        max_value_new = max([d['value'] for d in values_new])

        if (value_node > max_value_new):
            # setup output view spot dict
            spot = {'element_id': id, 'value': value_node}
            spots.append(spot)

            # all element ids cannot be maxima, so append to donotlookAt
            donotlookAt = combine_lists_and_remove_duplicates(donotlookAt, list_all_new)

        # put all elements smaller than max to donotlookAt
        else:
            # get index of max value
            max_value_new_id = [ val['element_id'] for  val in values if (val['value'] == max_value_new)][0]
            # remove index of max value from list_all_new
            #print(max_value_new_id, list_all_new)
            list_all_new.remove(max_value_new_id)
            # append all elements smaller than max to donotlookAt
            donotlookAt = combine_lists_and_remove_duplicates(donotlookAt, list_all_new)

            if (len(spots) == N):
                break

        #else :
        #    if (isclose(value_node, max(values_new))):
        #        print('2: ', id, ' ', value_node)

    sorted_spots = sorted(spots, key=lambda d: d['value'], reverse=True)
    return(sorted_spots)
