.. Read the Docs Template documentation master file, created by


Autoscaler
========

.. toctree::
  :maxdepth: 2
  :glob:

  *

Autoscaler is a simple tool to provide reactive scaling to your computer infrastructure at runtime.

Autoscaler watches CPU usage while on a given instance and makes the decision when to scale up. This is opposed to traditional autoscalers which look at clusters at a whole. This is meant to be far simpler than cluster scalers such as Kubernetes.


Requirements
============

* You can run ``autoscaler master`` on your load balancing proxies.
* You run one or more HAProxy instances on another machine and you are fine with autoscaler taking over configuration for it.
* Each Autoscaler node can SSH into the other autoscaler nodes.

Configuration
=================

Use `autoscaler init` to place configuration file `autoscaler.ini` into `/etc/autoscaler/autoscaler.ini`

- Create an AWS command used for scaling up.
- Place your AWS credentials
- Place the SSH command to log into HAProxy
- Place the comma separated list of HAProxy servers

Installation
===========

Autoscaler needs to be installed on your Haproxy instance and all your machines that you will be scaling up.

.. code-block:: console

    pip3 install aws-autoscaler

On your HAProxy instances, run:

.. code-block:: console

    autoscaler master

Connections to the master from web application servers is handled by SSH remote port forwarding so you don't need to open any firewall rules.

HAProxy Configuration
=====================

- ``autoscaler add-host <host> <port>`` will write a host entry to ``/etc/autoscaler/hosts.d/``.
- ``autoscaler generate`` will generate a HAProxy configuration file based on the hosts inside ``/etc/autoscaler/hosts.d``


Contribute
----------

- Issue Tracker: github.com/$project/$project/issues
- Source Code: github.com/$project/$project


License
-------

The project is licensed under the BSD license.






Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
