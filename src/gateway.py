#!/usr/bin/python

//Init : Protocol Handler, MQ Connection, ZK Connection

//loop1 : Connection Accept, receive messages from clients -> send to MQ

//loop2 : receive messages from MQ -> sen to clients

//loop3 : If clients cut connection, then decrease client count

