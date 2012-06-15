from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='django-readonlydb_testrunner',
      version=version,
      description="Test against your live database connections with this custom Django testrunner",
      long_description="",
      classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
      ],
      keywords='',
      author='Ethan Jucovy',
      author_email='ethan@boldprogressives.org',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
      ],
      entry_points="""
      """,
      )
