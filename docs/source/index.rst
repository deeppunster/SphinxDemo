Welcome to The Sphinx Documentation Tool!
==============================================

This is a sample project to demonstrate how easy it is to create **Sphinx
Documentaton** for Python code.  Included here is a module with classes and
another with bare functions.

**CleanIO** is a module containing two classes for minimizing the cruft
needed to read or write plain text files.  It can be installed from `PyPi <https://pypi.org/>`_.

-   *CleanRead* is a class to read a text file.  It includes code to check
    that the file name is a valid string or path, that it exists, is a file,
    and is readable.  This class returns a line at a time until the end of
    file is reached.  It handles empty lines and automatically closes the file
    regardless of whether the file is read to the end or not.

-   *CleanWrite* - is a class to write a text file.  It includes code to
    check that the file name is a string or a path, that the file does not
    previously exist.  This class accepts a line at a time until a call to
    close the file is made.

**Lumache** (/lu'make/) is a Python library for cooks and food lovers that
creates recipes mixing random ingredients.

Check out the :doc:`usage` section for further information, , including how to
:ref:`install <installation>` the project.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Contents
--------

.. toctree::

   CleanIO
   usage
   sample_markdown

.. note::

   This project is under active development.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
