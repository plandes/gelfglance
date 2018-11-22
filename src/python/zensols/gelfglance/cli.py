from zensols.actioncli import OneConfPerActionOptionsCli
from zensols.actioncli import SimpleActionCli
from zensols.gelfglance import LogSender

VERSION='0.1'

# recommended app command line
class ConfAppCommandLine(OneConfPerActionOptionsCli):
    def __init__(self):
        server_action = 'server'
        cnf = {'executors':
               [{'name': 'hello',
                 'executor': lambda params: LogSender(**params),
                 'actions':[{'name': server_action,
                             'meth': 'start',
                             'doc': 'start in server mode',
                             'opts': [['-g', '--gelfserver', True,
                                       {'dest': 'gelf_server', 'metavar': 'STRING',
                                        'default': 'localhost',
                                        'help': 'Graylog host name (defaults to localhost)'}],
                                      ['-p', '--gelfport', True,
                                       {'dest': 'gelf_port', 'metavar': 'INTEGER',
                                        'default': 12201,
                                        'type': 'int',
                                        'help': 'Graylog port (defaults to 12201)'}],
                                      ['-s', '--glancesserver', True,
                                       {'dest': 'glances_server', 'metavar': 'STRING',
                                        'default': 'localhost',
                                        'help': 'Glances server port (defaults to localhost)'}],
                                      ['-l', '--glancesport', True,
                                       {'dest': 'glances_port', 'metavar': 'INTEGER',
                                        'default': 61208,
                                        'type': 'int',
                                        'help': 'Graylog port (defaults to 61208)'}],
                                      ['-r', '--source', True,
                                       {'metavar': 'STRING',
                                        'default': 'glances',
                                        'help': 'Glances port (defaults to 12201)'}],
                                      ['-c', '--count', False,
                                       {'metavar': 'STRING',
                                        'type': 'int',
                                        'help': 'Number of messages to send (default to infinite)'}],
                                      ['-t', '--timeout', True,
                                       {'metavar': 'STRING',
                                        'dest': 'timeout_secs',
                                        'default': 10,
                                        'type': 'int',
                                        'help': 'Timeout between each sent message in seconds (defaults to 10)'}]]
                 }]}],
               'whine': 1}
        super(ConfAppCommandLine, self).__init__(cnf, version=VERSION, default_action=server_action)

    def config_parser(self):
        super(ConfAppCommandLine, self).config_parser()
        parser = self.parser
        # parser.remove_option('-s')
        parser.add_option('-x', '--short', dest='short',
                          help='short output for list', action='store_true')

def main():
    cl = ConfAppCommandLine()
    cl.invoke()
