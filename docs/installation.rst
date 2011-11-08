.. index:: installation

.. _installation-chapter:


Installation
============

* Get the code - https://github.com/mozilla/socorro
* Read the INSTALL file https://github.com/mozilla/socorro/blob/master/INSTALL#L1

FIXME review the below older documentation, and either merge or remove:

Upgrading? See :ref:`upgrade-chapter`

* setup a file system available through NFS (or whatever). All
  machines running Socorro applications must have read/write access
* prepare an instance of PostgreSQL for use by the :ref:`monitor-chapter`,
  :ref:`processor-chapter` and :ref:`reporter-chapter`
* Get the code - https://github.com/mozilla/socorro
* Use the latest trunk version of the code.
* Any installation must have the socorro package available on the
  PYTHONPATH or in the appropriate .../site-packages directory
* Start configuration with :ref:`commonconfig-chapter`
* run the database setup script: :ref:`databasesetup-chapter`
* On the machine(s) to run collector, setup :ref:`collector-chapter`
* On the machine to run monitor, setup :ref:`monitor-chapter`
* On same machine that runs monitor, setup :ref:`deferredcleanup-chapter`
* On the machine(s) to run processor, setup :ref:`processor-chapter`
