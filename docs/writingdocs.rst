.. index:: writingdocs

.. _writingdocs-chapter:

Writing documentation
=====================

To contribute with your documentation follow these steps to be able to
modify the git repo, build a local copy and deploy on `ReadTheDocs.org`_.


.. _`ReadTheDocs.org`: https://readthedocs.org/


Installing Sphinx
--------------------

`Sphinx`_ is an external tool that compiles these `reStructuredText`_ into
HTML. Since it's a python tool you can install it with
``easy_install`` or ``pip`` like this::

 pip install sphinx
 

.. _Sphinx: http://sphinx.pocoo.org/
.. _reStructuredText: http://sphinx.pocoo.org/rest.html
 
Making the HTML
---------------

Now you can build the docs with this simple command::

 cd docs
 make html
 
This should update the revelant HTML files in ``socorro/docs/_build``
and you can preview it locally like this (on OS X for example)::

 open _build/html/index.html
 
Making it appear on ReadTheDocs
-------------------------------

`ReadTheDocs.org`_ is wired to build the documentation nightly from
this git repository but if you want to make documentation changes
appear immediately you can use their `webhooks`_ to re-create the
build and update the documentation right away. 

.. _webhooks: http://readthedocs.org/docs/read-the-docs/latest/webhooks.html

Or, just send the pull request
------------------------------

If you have a relevant update to the documentation but don't have time
to set up your Sphinx and git environment you can just edit these
files in raw mode and send in a pull request.



 
