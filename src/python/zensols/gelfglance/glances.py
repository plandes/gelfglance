import logging
import math
import json
from xmlrpc import client

logger = logging.getLogger('zensols.gelfglance.glances')

class GlancesClient(object):
    """
    Make the xmlrpc request to the glances server and facade out the response.

    See https://github.com/nicolargo/glances/wiki/The-Glances-2.x-API-How-to
    """
    def __init__(self, host='localhost', port=61208):
        self.host = host
        self.port = port

    @property
    def proxy(self):
        if not hasattr(self, '_proxy'):
            self._proxy = client.ServerProxy('http://{}:{}'.format(self.host, self.port))
        return self._proxy

    @property
    def plugins(self):
        res = self.proxy.getAllPlugins()
        return json.loads(res)

    @property
    def sensors(self):
        res = self.proxy.getSensors()
        return json.loads(res)

    @property
    def cpu(self):
        res = self.proxy.getCpu()
        return json.loads(res)

    @property
    def system(self):
        res = self.proxy.getSystem()
        return json.loads(res)

    def format_system(self):
        return '{hostname} ({hr_name})'.format(**self.system)

    def _col_sensors(self, sensors, data):
        for td in sensors:
            name = 'sensor_' + td['label'].replace(' ', '_').lower()
            val = td['value']
            # argument '--fahrenheit' has no affect
            if td['unit'] == 'C':
                val = 9.0/5.0 * val + 32
                # round errors
                val = math.floor(val * 100) / 100
            data[name] = val

    def _col(self, gdict, name, data):
        for k, v in gdict.items():
            k = '{}_{}'.format(name, k)
            data[k] = v

    def get(self, plugins=None):
        if plugins is None:
            plugins = {'sensors', 'cpu'}
        data = {}
        if 'sensors' in plugins:
            self._col_sensors(self.sensors, data)
        if 'cpu' in plugins:
            self._col(self.cpu, 'cpu', data)
        return data

    def pprint(self, obj):
        import pprint
        pprint.PrettyPrinter().pprint(obj)
