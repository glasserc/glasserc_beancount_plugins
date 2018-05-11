==========================
glasserc Beancount Plugins
==========================

Some beancount plugins of my own


* Free software: MIT license
* Documentation: https://glasserc-beancount-plugins.readthedocs.io.


Plugins
-------

* add_payee_from_narration: a quick hack to auto-add payees based on a
  string in the narration. This is useful when dealing with
  transactions imported from a credit card company, where you may have
  semi-garbled company names as the only narration.

  Usage::

    plugin "glasserc_beancount_plugins.add_payee_from_narration" "AMZN: Amazon"

  This will automatically add "Amazon" as the payee for any
  transactions which contain "AMZN" in the narration. This might be
  convenient when you want to tag a whole bunch of transactions with
  the same billing descriptor as going to the same payee. (Be careful!
  Some merchants may have several billing descriptors, and the string
  you choose, in this case AMZN, may match several different lines of
  business, such as Amazon Payments as well as Amazon.com.)


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
