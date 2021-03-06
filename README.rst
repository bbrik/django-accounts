===========
Description
===========

This app extends the built-in views in ``django.contrib.auth.views``.
Instead of providing a page specific to tell the user his password has been changed
or reset, it sets a message on the request and redirects to a specified path,
``/`` by default.

It provides templates that render forms using bootstrap markup.
They extend ``base.html`` by default and expect blocks ``title`` and ``content``.


============
Installation
============

Installing django-accounts
~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Install using pip::

    pip install git+https://github.com/bbrik/django-accounts.git 

#. Install messages middleware to your project if it is not installed already,
please see django documentation

#. Add ``accounts`` to your ``INSTALLED_APPS`` in settings.py:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'accounts',
    )

#. Import ``accounts.urls`` in your global ``urls.py``:

.. code-block:: python

    urlpatterns = patterns('',
        url(r'^accounts/', include('accounts.urls', namespace='accounts')),
        ...
    )


Usage
~~~~~

Adding links in your templates
******************************

Use the following urls on your templates:

.. code-block:: html

    <a href="{% url 'accounts:login' %}">
      Login
    </a>
    <a href="{% url 'accounts:logout' %}">
      Logout
    </a>
    <a href="{% url 'accounts:password_change' %}">
      Logout
    </a>
    <a href="{% url 'accounts:password_reset' %}">
      Login
    </a>


Custom settings
***************

ACCOUNTS_BASE_TEMPLATE
++++++++++++++++++++++

Sets the base template name. Default is ``base.html``.

LOGOUT_REDIRECT_URL
+++++++++++++++++++

Sets url to redirect on logout, can be a view name. Default is ``/``.

PASSWORD_CHANGE_REDIRECT_URL
++++++++++++++++++++++++++++

Sets url to redirect on password change, can be a view name. Default is ``/``.

PASSWORD_RESET_REDIRECT_URL
+++++++++++++++++++++++++++

Sets url to redirect on password reset, can be a view name. Default is ``/``.
