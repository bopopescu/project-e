#!/usr/bin/python
from kazoo.clinet import KazooClient

//Init - ZK connection, node watch
zk=KazooClient(hosts='127.0.0.1:2181') //default port
zk.start();

@zk.ChildrenWatch("/gateways/")
def watch_gw_children(children)
	print("Children are now: %s" % children)
# Above function called immediately, and from then on

@zk.DataWatch("gateways")
def watch_node(data,stat):
	print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))
//main loop - ZK Events Management - new ephemeral node,
//				ephemeral node change, scale in/out

#How to get CPU usage ratio?
#How to get Memory usage ratio?
#How to get the sum of connection?
