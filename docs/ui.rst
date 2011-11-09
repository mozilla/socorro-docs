.. index:: ui

.. _ui-chapter:

Socorro UI
==========

The Socorro UI is a KohanaPHP implementation that will operate the
frontend website for the Crash Reporter website.
Coding Standards

Maintaining coding standards will encourage current developers and
future developers to implement clean and consistent code throughout
the codebase.

The PEAR Coding Standards
(http://pear.php.net/manual/en/standards.php) will serve as the basis
for the Socorro UI coding standards.

* Always include header documentation for each class and each method.
    * When updating a class or method that does not have header
      documentation, add header documentation before committing.
    * Header documentation should be added for all methods within
      each controller, model, library and helper class.
    * @param documentation is required for all parameters
    * Header documentation should be less than 80 characters
      in width.
* Add inline documentation for complex logic within a method.
* Use 4 character tab indentations for both PHP and Javascript
* Method names must inherently describe the functionality within that method.
    * Method names must be written in a camel-case format. e.g. getThisThing
    * Method names should follow the verb-noun format, such as a getThing, editThing, etc.
* Use carriage returns in if statements containing more than 2
  statements and in arrays containing more than 3 array members for
  readability.
* All important files, such as controllers, models and libraries,
  must have the Mozilla Public License at the top of the file.

