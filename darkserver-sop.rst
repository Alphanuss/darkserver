.. title: Darkserver SOP
.. slug: infra-darkserver
.. date: 2016-02-26
.. taxonomy: Contributors/Infrastructure

==============
Darkserver SOP
==============

To setup a http://darkserver.fedoraproject.org based on Darkserver project
to provide GNU_BUILD_ID information for packages. A devel instance can be
seen at http://darkserver01.dev.fedoraproject.org and staging instance is
http://darkserver01.stg.phx2.fedoraproject.org/.

This page describes how to set up the server.

Contents
========

1.  Contact Information
2.  Installing the server
3.  Setting up the database
4.  SELinux Configuration
5.  Setup the services on backend
6.  Setup the services on web frontends
7.  Debugging


Contact Information
===================

Owner: 
  Fedora Infrastructure Team
Contact: 
  #fedora-admin
Persons: 
  kushal mether
Sponsor: 
  nirik
Location: 
  phx2
Servers: 
  darkserver-backend,darkserver-web,darkserver-backend.stg,darkserver-web.stg
Purpose: 
  To host Darkserver


Installing the server
=======================

In the backend server we run the following command.
::

  root@localhost# yum install darkserver-importer

.. note:: Please make sure that the backend instance can reach koji,
            ppc.koji, and s390.koji, and arm.koji instances.

Next step is to setup configuration for the rabbitmq. The configuration should go
into the */etc/darkserver/rabbitmq.cfg* file with a *rabbitmq* section.

Start the fedmsg-hub and then darkserver service.

In the front end web nodes, we run the following command.
::

    root@localhost# yum install darkserver


Setting up the database
=======================

We will need a user with write access to the database for the backend, and one user with
only read access for the web frontends.

For backend update the `/etc/darkserver/darkjobworker.conf` file, and in for frontend(s)
update `/etc/darkserver/darkweb.cfg` with the database configurations.



SELinux Configuration
=====================

Do the follow to allow the webserver to connect to the database.::

  root@localhost# setsebool -P httpd_can_network_connect_db 1

Start the services on backend
=============================

First make sure your fedmsg-hub service can listen to koji rpm build
messages on fedmsg.
Enable and start fedmsg-hub, and darkserver service on the backend.

Start the services on web frontends
===================================

Enable and start `httpd` (Apache) service on the web frontends. The frontend is
now written in Flask.


Debugging
=========
To find the logs in the backend check the `fedmsg-hub` and `darkserver` service logs

