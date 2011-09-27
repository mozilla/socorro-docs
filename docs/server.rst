.. index:: server

.. _server-chapter:

Server
======

The Socorro Server is a collection of Python applications and a Python
package ([[SocorroPackage]]) that runs the backend of the Socorro system.


The Applications
----------------

Executables for the applications are generally found in the
.../scripts directory.

* ../scripts/startCollector.py - :ref:`collector-chapter`
* ../scripts/startDeferredCleanup.py - [[SocorroDeferredCleanup]]
* ../scripts/startMonitor.py - [[SocorroMonitor]]
* ../scripts/startProcessor.py - :ref:`processor-chapter`
* ../scripts/startTopCrashes.py - TopCrashersBySignature
* ../scripts/startBugzilla.py - BugzillaAssociations
* ../scripts/startMtfb.py - MeanTimeBeforeFailure
* ../scripts/startServerStatus.py - server status
* ../scripts/startTopCrashByUrl.py - TopCrashersByUrl
