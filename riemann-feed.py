#! /usr/bin/env python

import bernhard
c = bernhard.Client()
c.send({'host': 'myhost.foobar.com', 'service': 'myservice', 'metric': 12})

