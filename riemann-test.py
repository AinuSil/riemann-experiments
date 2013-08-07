#! /usr/bin/env python

import flask, bernhard
app = flask.Flask(__name__)

@app.route('/')
def dashboard():
    c = bernhard.Client ()
    q = c.query("true")
    events = {}
    services = []
    for e in q:
    	if e.event.host in events:
    		events[e.event.host].update ({e.event.service: e.event.metric_d or e.event.metric_f or e.event.metric_sint64})
    	else:
    		events[e.event.host] = {e.event.service: e.event.metric_d or e.event.metric_f or e.event.metric_sint64}

    	if e.event.service in services:
   		pass
    	else:
    		services.append (e.event.service)
    	
    return flask.render_template("dashboard.html", 
    				 riemann = events,
    				 services = services,
    				 config = {"riemann_host": "localhost",
    				           "riemann_port": 3306}) 

if __name__ == '__main__':
    app.run()


