RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
PAGINATION = False
lookup_url = 'regex("[\w-]+")'

machine_schema = {
    'hostname': {
        'type': 'string',
        'required': True,
        'unique': True,
    },
    'owner': {
        'type': 'string'
    },
    'state': {
        'type': 'string',
        'allowed': ["pxe", "pxe_failed","idle","needs_repair"]
    }
}

address_schema = {
    'address': {
        'type': 'string',
        'required': True,
        'unique': True,
    },
    'owner': {
        'type': 'string'
    }
}

machines = {
    'item_title': 'machine',
    'additional_lookup': {
        'url': lookup_url,
        'field': 'hostname'
    },
    'schema': machine_schema
}

public_addresses = {
    'item_title': 'public-address',
    'additional_lookup': {
        'url': lookup_url,
        'field': 'address'
    },
    'schema': address_schema
}

private_addresses = {
    'item_title': 'private-address',
    'additional_lookup': {
        'url': lookup_url,
        'field': 'address'
    },
    'schema': address_schema
}

DOMAIN = {
    'machines': machines,
    'public-addresses': public_addresses,
    'private-addresses': private_addresses
}