Sometimes you need to run Django test suites against a live database connection 
that you also use for development or production.

Django makes this very difficult: out of concern for your data's well-being,
the test runner will create a clean mirror of each of your databases before
running your tests, and run the tests against those test databases.

(See https://docs.djangoproject.com/en/dev/topics/testing/#the-test-database 
for more information about this feature.)

Best practices are great, but you might just need to disable this feature.
You might be on a shared server where you don't have permissions to create
and destroy new databases; you might have a large, complex legacy database
that you want to test against directly for convenience; you might have
configured a database connection with only read/select privileges
which you want to run querying tests against, since you know that you
can't accidentally mess up any live data with your tests anyway. 

In those situations, use the test runner provided by this library.

Usage
=====

First, make sure to configure the test runner in ``settings.py``:

  TEST_RUNNER = 'use_live_db.TestRunner'

Then, mark one or more of your DATABASES with a special attribute
`USE_LIVE_FOR_TESTS` which tells the test runner to use it as-is in
tests, instead of trying to create a copy:

  DATABASES = {
    'default': {
      'ENGINE': #...
      'NAME': #...
      # ...
      'USE_LIVE_FOR_TESTS': True
    },
  }

If you omit this value from any of the connections in your DATABASES,
then Django's default behavior will apply.  So, for example, you could
configure your default database to have tests run against a copy per
Django's typical behavior; and set ``USE_LIVE_FOR_TESTS`` on your
read-only connection to a supplemental legacy database which has data
that your tests depend on.
