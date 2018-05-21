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


## Obtaining

```bash
pip install gelfglance
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
