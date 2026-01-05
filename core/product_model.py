class Product:
    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self._data

    def get(self, key, default=None):
        return self._data.get(key, default)

    def set(self, key, value):
        self._data[key] = value

    def mark_deleted(self):
        self._data['deleted'] = True

    def is_deleted(self):
        return self._data.get('deleted') is True or self._data.get('deleted') == 'True'

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def keys(self):
        return self._data.keys()

    def __str__(self):
        return str(self._data)
