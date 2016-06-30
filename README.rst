===================
scrapy-querycleaner
===================

.. image:: https://travis-ci.org/scrapy-plugins/scrapy-querycleaner.svg?branch=master
    :target: https://travis-ci.org/scrapy-plugins/scrapy-querycleaner

.. image:: https://codecov.io/gh/scrapy-plugins/scrapy-querycleaner/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/scrapy-plugins/scrapy-querycleaner

This is a Scrapy spider middleware to clean up the request URL GET query parameters
at the output of the spider in accordance with the patterns provided by the user.


Installation
============

Install scrapy-querycleaner using ``pip``::

    $ pip install scrapy-querycleaner


Configuration
=============

1. Add ``QueryCleanerMiddleware`` by including it in ``SPIDER_MIDDLEWARES``
   in your ``settings.py`` file::

      SPIDER_MIDDLEWARES = {
          'scrapy_querycleaner.QueryCleanerMiddleware': 100,
      }

   Here, priority ``100`` is just an example.
   Set its value depending on other middlewares you may have enabled already.

2. Enable the middleware using either ``QUERYCLEANER_REMOVE``
   or ``QUERYCLEANER_KEEP`` (or both) in your ``setting.py``.


Usage
=====

At least one of the following settings needs to be present for the
middleware to be enabled.


.. note::
    You can specify a list of parameter names by using the ``|`` (*OR*) regex operator.

    For example, the pattern ``search|login|postid`` will match query parameters *search*,
    *login* and *postid*.
    This is by far the most common usage case.

    And by setting ``QUERYCLEANER_REMOVE`` value to ``.*``
    you can completely remove all URL query parameters.


Supported settings
------------------

``QUERYCLEANER_REMOVE``
    a pattern (regular expression) that a query parameter name must match
    in order to be removed from the URL. (All the others will be accepted.)

``QUERYCLEANER_KEEP``
    a pattern that a query parameter name must match in order to be kept in the URL.
    (All the others will be removed.)

You can combine both if some query parameters patterns should be kept and some should not.

The **remove** pattern has precedence over the *keep* one.


Example
-------

Let's suppose that the spider extracts URLs like::

    http://www.example.com/product.php?pid=135&cid=12&ttda=12

and we want to leave only the parameter ``pid``.

To achieve this objective we can use either ``QUERYCLEANER_REMOVE``
or ``QUERYCLEANER_KEEP``:

- In the first case, the pattern would be ``cid|ttda``::

    QUERYCLEANER_REMOVE = 'cid|ttda'

- In the second case, ``pid``::

    QUERYCLEANER_KEEP = 'pid'


The best solution depends on a particular case, that is,
how the query filters will affect any other URL that the spider is expected to extract.
