# These are the MongoDB settings
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
#MONGO_USERNAME = 'apiuser'
#MONGO_PASSWORD = 'apipass'
MONGO_DBNAME = 'opennote'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

schema = {
	# Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'email': {
    	'type': 'string',
    	'minlength': 1,
    	'maxlength': 255,
    	'required': True
    },
    'firstname': {
    	'type': 'string',
    	'minlength': 1,
    	'maxlength': 40
    },
    'lastname': {
    	'type': 'string',
    	'minlength': 1,
    	'maxlength': 40
    },
}

people = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'person',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    
    ''''additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'lastname'
    },'''
    

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': schema
}

# Other settings
SERVER_NAME = '127.0.0.1:5000'
DOMAIN = {
    'people': people,
}