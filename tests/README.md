Functional tests
================

This directory contains pytest-based functional tests.

For dev unit tests, see `../iotlabsshcli/tests`.

Note: dev unit tests can be run with py.test as well.


Setting up you virtualenv for tests
-----------------------------------

	pip install pytest


Running the tests
-----------------

	py.test


Running the dev unit tests
--------------------------

	pip install mock
	cd ..
	py.test


The travis-ci setup
-------------------

The `secure` sections in `../.travis.yml` allow to pass
sensitive user/password information into the travis build
via encrypted environment variables.

This is how the `secure` sections were generated:

	cd ssh-cli-tools        # the travis tool needs to know the repo
	. ../source.me.travis   # export the vars
	travis encrypt IOTLAB_USER="$IOTLAB_USER"
	travis encrypt IOTLAB_PASS="$IOTLAB_PASS"


To install the travis tool:

	sudo apt-get install gem
	sudo apt-get install ruby
	sudo apt-get install ruby-dev
	sudo gem install travis
