

class CheckerRouter:
    """
    A router to control all database operations on models in the
    user application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read user models go to users_db.
        """
        if model.__meta.app_label == 'node1':
            return 'node1'
        elif model.__meta.app_label == 'node2':
            return 'node2'
        elif model.__meta.app_label == 'node3':
            return 'node3'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write user models go to users_db.
        """
        print(model.__meta.app_label)
        if model.__meta.app_label == 'node1':
            return 'node1'
        elif model.__meta.app_label == 'node2':
            return 'node2'
        elif model.__meta.app_label == 'node3':
            return 'node3'
        return None

    def allow_relation(self, obj1, obj2, obj3,**hints):
        """
        Allow relations if a model in the user app is involved.
        """
        if obj1._meta.app_label == 'node1' or \
           obj2._meta.app_label == 'node2' or \
           obj3._meta.app_label == 'node3':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'users_db'
        database.
        """
        if app_label == 'node1':
            return db == 'node1'
        elif app_label == 'node2':
            return db == 'node2'
        elif app_label == 'node3':
            return db == 'node3'
        return None