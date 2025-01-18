#####################################
Sphinx Documentation Tool and Example
#####################################

Contents:

    `Welcome`_

    `Features`_

        `Documentation From Code`_

        `Type Hints`_

        `Markdown`_

        `Multiple Outputs`_

        `Multiple Themes`_

    `Installation`_

    `Code of Conduct`_

    `Contributors`_

    `License`_




Welcome
============

Welcome to the Sphinx Documentation Tool open source project!

This project is designed to help you get started using Sphinx as a documentation tool for your project.

In addition to the example code given in this project, there is a step-by-step `presentation <Sphinx Presentation.pptx>`_ available. See the `installation  <Installation>`_ section for details.

Features
========

A number of Sphinx features are illustrated in the included example code.

Documentation From Code
-----------------------

Sphinx can extract documentation from your code.  Sphinx can include undocumented functions and members so you can benefit immediately with search capability and indexing while fleshing out documentation in your code gradually.

Type Hints
----------

Recent libraries allow you to document type hints (PEP 484).  This example shows how to use one of those libraries to enhance your documentation.

Markdown
--------

Is markdown your markup language of choice?  This project shows you how to add support for markdown so you can use it instead of, or in addition to, ReStructured Text.  Author in reStructuredText or MyST Markdown to create highly structured technical documents, including tables, highlighted code blocks, mathematical notations, and more.

Multiple Outputs
----------------

Sphinx provides support for building multiple outputs from single set of source markup files and code.  Support for building HTML (multiple pages or a single HTML page), PDF, applehelp, htmlhelp, qthelp, devhelp, ePub, MAN pages, LaTeX, texinfo, plain text, and XML are all built in.  (Producing Apple Help or Windows Help require tools available on their respective systems).  More kinds of output are also available.  See the `extensions <https://www.sphinx-doc.org/en/master/usage/extensions/index.html>`_ page for details.

Multiple Themes
---------------

Sphinx has numerous themes available. Examples of each of the major themes can be seen `here <https://www.sphinx-doc.org/en/master/examples.html>`_.

Installation
============

There is a step-by-step `presentation <Sphinx Presentation.pptx>`_ available which walks through how to add full Sphinx support to your project.

If you want to make this project a fully functioning example, follow these steps:

1.  Download the zip file for the main branch of this project.

2.  Unpack the zip file in a convenient directory.

3.  Create a python virtual environment for this project and activate it.

4.  Install the various libraries needed from the `requirements <requirements.txt>`_ file.

    ``pip3 install -r requirements.txt``

5.  Change to the ``docs`` subdirectory.

6.  Run the ``make html`` command.

7.  Invoke a web browser on the file ``./build/html/index.html``.


Code of Conduct
===============

Contributor code of conduct for this project is given in `Code of Conduct <Code_of_Conduct.md>`_.

Contributors
============

The original contributors to this project are given in `Contributors <Contributors.md>`_.

Pull requests with improvements are welcome.

License
=======

``Sphinx Documentation Tool``  is distributed under the terms of the `MIT <https://mit-license.org/>`_ license.