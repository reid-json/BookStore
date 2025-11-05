class DBConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DBConfig, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        self.config = {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': "bookstoredb",
            'USER': "root",
            'PASSWORD': "rootmaster",
            'HOST': "bookstoredb.c5qaa0406cvn.us-east-2.rds.amazonaws.com",
            'PORT': "3306",
            'OPTIONS':{
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
            }
        }

    def get_config(self):
        return self.config