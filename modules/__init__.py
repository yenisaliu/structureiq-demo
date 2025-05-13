from . import bridge, building

def get_asset_module(name):
    return {
        'bridge': bridge,
        'building': building
    }.get(name, bridge)