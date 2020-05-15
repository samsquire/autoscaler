.. Read the Docs Template documentation master file, created by


Autoscaler
========

.. toctree::
  :maxdepth: 2
  :glob:

  *

Autoscaler is a simple tool to provide reactive scaling to your computer infrastructure at runtime.

Autoscaler watches CPU usage while on a given instance and makes the decision when to scale up. This is opposed to traditional autoscalers which look at clusters at a whole. This is meant to be far simpler than cluster scalers such as Kubernetes.

Configuration
=================

Use `autoscaler init` to place configuration file `autoscaler.ini` into `/etc/autoscaler/autoscaler.ini`

- Create a machine template file which is is a description of the AMI and machine size to use for scaling up.
- Place your AWS credentials
- Place the SSH command to log into HAProxy
- Place the comma separated list of HAProxy servers

Installation
===========

..
    pip3 install aws-autoscaler


Autoscaler needs to be installed on your Haproxy instance and all your machines that you will be scaling up.

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
