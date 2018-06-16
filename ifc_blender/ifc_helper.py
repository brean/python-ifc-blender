import itertools

def flatten(lst):
    return list(itertools.chain.from_iterable(lst))

def elements_by_type(project, ifc_type):
    if ifc_type == 'project':
        return project
    elif ifc_type == 'site':
        return [s for s in project.sites]
    elif ifc_type == 'building':
        buildings = flatten([s.buildings for s in project.sites])
        return buildings
    elif ifc_type == 'storey':
        buildings = flatten([s.buildings for s in project.sites])
        storeys = flatten([b.storeys for b in buildings])
        return storeys
    elif ifc_type == 'space':
        buildings = flatten([s.buildings for s in project.sites])
        storeys = flatten([b.storeys for b in buildings])
        spaces = flatten([s.spaces for s in storeys])
        return spaces
    elif ifc_type == 'product':
        buildings = flatten([s.buildings for s in project.sites])
        storeys = flatten([b.storeys for b in buildings])
        spaces = flatten([s.spaces for s in storeys])
        products = []
        products += flatten([s.products for s in storeys])
        products += flatten([s.products for s in spaces])
        return products
