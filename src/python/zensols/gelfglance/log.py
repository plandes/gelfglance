import logging
import syslog
import time
import traceback
from gelfclient import UdpClient
from zensols.gelfglance import GlancesClient

logger = logging.getLogger('zensols.gelfglance.log')

class LogSender(object):
    """
    Get glances data from server and forward it on to Graylog 2.

    :gelf_server: the Graylog host name
    :gelf_port: the Graylog port (defaults to 12201)
    :source: used in the source field of the gelf message (defaults to host name)
    :timeout_sec: timeout in seconds before the Glances data is queried and sent to graylog (defaults to 10)
    :count: number of messages to send (defaults to infinity)
    """
    def __init__(self, gelf_server='localhost', gelf_port=12201, source=None,
                 glances_server='localhost', glances_port=61208,
                 timeout_secs=10, count=10):
        self.gelf_server = gelf_server
        self.gelf_port = gelf_port
        self.glances_server = glances_server
        self.glances_port = glances_port
        self.source = source
        self.count = count
        self.timeout_secs = timeout_secs
        self.mtu = 8000

    @property
    def gelf(self):
        "Return the Graylog logger client."
        if not hasattr(self, '_gelf'):
            self._gelf = UdpClient(self.gelf_server, port=self.gelf_port, mtu=self.mtu, source=self.source)
        return self._gelf

    @property
    def glances(self):
        "Return the Glances client."
        if not hasattr(self, '_glances'):
            self._glances = GlancesClient(self.glances_server, self.glances_port)
        return self._glances

    def send_message(self, message, additional_data, level=syslog.LOG_INFO):
        "Send a Gelf message with Glances statistics."
        data = {'short_message': message,
                'program': 'glances',
                'level': level}
        if self.source:
            data['host'] = self.source
        data.update(additional_data)
        logger.debug('sending message to {}:{} -> <{}>'.
                     format(self.gelf_server, self.gelf_port, additional_data))
        self.gelf.log(data)

    def collect_and_send(self):
        "Collect glances data and send to Graylog."
        data = self.glances.get()
        msg = 'System statistics for {}'.format(self.glances.format_system())
        self.send_message(msg, data)

    def start(self):
        "Start the logger as a /server/ by looping on a timeout."
        logger.info('starting gelf_server {gelf_server} on {gelf_port} from source \'{source}\', timeout(s)={timeout_secs}, count={count}'.format(**vars(self)))
        while self.count is None or self.count > 0:
            logger.debug('timeout_secs ({}) up'.format(self.timeout_secs))
            try:
                self.collect_and_send()
            except Exception as e:
                traceback.print_exc()
            if not self.count is None:
                self.count -= 1
            time.sleep(self.timeout_secs)
