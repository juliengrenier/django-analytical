"""
=========================
Optimizely -- A/B testing
=========================

Optimizely_ is an easy way to implement A/B testing.  Try different
decisions, images, layouts, and copy without touching your website code
and see exactly how your experiments are affecting pageviews,
retention and sales.

.. _Optimizely: http://www.optimizely.com/


.. optimizely-installation:

Installation
============

You only need to do perform these steps if you are not using the
generic :ttag:`analytical.*` tags.  If you are, skip to
:ref:`optimizely-configuration`.

In order to use the template tag, you need to add
:mod:`analytical.optimizely` to the installed applications list in the
project :file:`settings.py` file::

    INSTALLED_APPS = [
        ...
        'analytical.optimizely',
        ...
    ]

The Optimizely Javascript code is inserted into templates using a
template tag.  Load the :mod:`mixpanel` template tag library and insert
the :ttag:`optimizely` tag.  Because every page that you want to track
must have the tag, it is useful to add it to your base template.
Insert the tag at the top of the HTML head::

    {% load optimizely %}
    <html>
    <head>
    {% optimizely %}
    ...


.. _optimizely-configuration:

Configuration
=============

Before you can use the Optimizely integration, you must first set your
account number.


.. _optimizely-account-number:

Setting the account number
--------------------------

Optimizely gives you a unique account number, and the :ttag:`optimizely`
tag will include it in the rendered Javascript code.  You can find your
account number by clicking the `Implementation` link in the top
right-hand corner of the Optimizely website.  A pop-up window will
appear containing HTML code looking like this::

    <script src="//cdn.optimizely.com/js/XXXXXXX.js"></script>

The number ``XXXXXXX`` is your account number.  Set
:const:`OPTIMIZELY_ACCOUNT_NUMBER` in the project :file:`settings.py`
file::

    OPTIMIZELY_ACCOUNT_NUMBER = 'XXXXXXX'

If you do not set an account number, the Javascript code will not be
rendered.


.. _optimizely-internal-ips:

Internal IP addresses
---------------------

Usually you do not want to use A/B testing on your development or
internal IP addresses.  By default, if the tags detect that the client
comes from any address in the :const:`INTERNAL_IPS` setting, the
tracking code is commented out.  See :const:`ANALYTICAL_INTERNAL_IPS`
for important information about detecting the visitor IP address.
"""

optimizely_service = {
    'head_top': 'analytical.optimizely.templatetags.optimizely.OptimizelyNode',
}