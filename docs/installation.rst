.. index:: installation

.. _installation-chapter:


Installation
============

Upgrading? See :ref:`upgrade-chapter`

* setup a file system available through NFS (or whatever). All
  machines running Socorro applications must have read/write access
* prepare an instance of PostgreSQL for use by the [[SocorroMonitor]],
  :ref:`processor-chapter` and [[SocorroReporter]]
* Get the code - https://github.com/mozilla/socorro
* Use the latest trunk version of the code.
* Any installation must have the socorro package available on the
  PYTHONPATH or in the appropriate .../site-packages directory
* Start configuration with [[SocorroCommonConfig]]
* run the database setup script: [[SocorroDatabaseSetup]]
* On the machine(s) to run collector, setup :ref:`collector-chapter`
* On the machine to run monitor, setup [[SocorroMonitor]]
* On same machine that runs monitor, setup [[SocorroDeferredCleanup]]
* On the machine(s) to run processor, setup :ref:`processor-chapter`
