from migrations.migration_0003_191223_simple_structure import queries_0003_191223

def migrate(config):
    # Run migrations
    queries_0003_191223(config)