# Forward glance statistics as gelf logs

This command line utility forwards [Glances] statistics and forwards the data
to [Graylog].  The program runs in a loop for an (optional) given number of
times in a timeout.  Each loop cycle collects data from the [Glances] server
and forwards the data as a "first class" (descrete fields) Graylog message.

With this data you can configured dashboards to report statistics based on
system health, temperatures etc.

The program currently records the following:

* CPU temperature (sensors)
* CPU load

Other data from [Glances] is very easy to add, I just haven't had a lot of time
to add them but I'd be glad to if someone asked for more.  If so, create an
issue and I'll look into your request.

![Screenshot](doc/snap.png?raw=true "Dashboard Example")

## Installing

You need Python 3 to run the program and the *pip* installer.

Install the library and program:
```bash
pip install gelfglance
```

For *systemd* operating systems, the example [systemd service] file might be
useful.


## Usage

Here's the usage for convenience (use `--help`):

```pony
Usage: gelfglance <list|...> [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -w NUMBER, --whine=NUMBER
                        add verbosity to logging
  -x, --short           short output for list


Usage: gelfglance server [additional options]

Start in server mode

Options:
  -g STRING, --gelfserver=STRING
                        Graylog host name (defaults to localhost)
  -p INTEGER, --gelfport=INTEGER
                        Graylog port (defaults to 12201)
  -s STRING, --glancesserver=STRING
                        Glances server port (defaults to localhost)
  -l INTEGER, --glancesport=INTEGER
                        Graylog port (defaults to 61208)
  -r STRING, --source=STRING
                        Graylog port (defaults to 12201)
  -c STRING, --count=STRING
                        Number of messages to send (default to infinite)
  -t STRING, --timeout=STRING
                        Timeout between each sent message in seconds (defaults to 10)
  -h, --help            show this help message and exit
```


## Changelog

An extensive changelog is available [here](CHANGELOG.md).


## License

Copyright © 2018 Paul Landes

Apache License version 2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


<!-- links -->

[Glances]: https://nicolargo.github.io/glances/
[Graylog]: https://www.graylog.org
[systemd service]: config/glancesgelf.service
