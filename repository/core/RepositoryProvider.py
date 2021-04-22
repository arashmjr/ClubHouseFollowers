from repository.core.CoreDatabase import CoreDatabase

class RepositoryProvider:
    database = CoreDatabase.get_instance()