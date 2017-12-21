httpie-vimond-auth
===============

Vimond API SUMO auth plugin for `HTTPie <https://httpie.org/>`_.

Sign requests with a SUMO header, specific for Vimond API.

.. image:: https://travis-ci.org/dewe/httpie-vimond-auth.svg?branch=master
    :target: https://travis-ci.org/dewe/httpie-vimond-auth

Installation
------------

.. code-block:: bash

    $ pip install git+https://github.com/dewe/httpie-vimond-auth

You should now see ``vimond`` under ``--auth-type`` in ``$ http --help`` output.

Usage
-----

.. code-block:: bash

    $ http --auth-type=vimond --auth='api_key:secret_key' <host>

Dev setup
---------

.. code-block:: bash

    $ virtualenv --no-site-packages env
    $ source env/bin/activate
    $ pip install -r requirements.dev.txt
