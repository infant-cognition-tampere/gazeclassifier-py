==============
gazeclassifier
==============

The Python package *gazeclassifier* provides functions to decide if given gaze points represent a saccade, fixation, or some unknown pattern.

The package *gazeclassifier* is developed at `Infant Cognition Laboratory
<http://www.uta.fi/med/icl/index.html>`_ at University of Tampere.



1. Install
==========

With `pip
<https://pypi.python.org/pypi/gazeclassifier>`_::

    $ pip install gazeclassifier

Compatible with Python 2.6, 2.7, 3.3, 3.4, and 3.5.



2. Usage
========

Import the lib::

    >>> import gazeclassifier as gaze

Define gaze points as pointlists::

    >>> g1 = [[0,0], [0,0], [1,1], [2,2], [2,2]]  # a saccade
    >>> g2 = [[1,1], [1,1], [1,1], [1,1], [1,1]]  # a fixation
    >>> g3 = [[1,1], [2,2], [0,0], [4,4], [1,1]]  # an unknown

Create a classifier. It is already pretrained and therefore able to ``predict``::

    >>> gc = gaze.GazeClassifier()
    >>> gc.predict(g1)
    'saccade'
    >>> gc.predict(g2)
    'fixation'
    >>> gc.predict(g3)
    'unknown'

Internally, ``predict`` first extracts features from pointlists before classification. The features can be extracted explicitly with ``extract_features`` and ``extract_raw_features``::

    >>> gaze.extract_features(g1)
    {
      'saccade_reaction': 1,
      'saccade_duration': 3,
      'saccade_mse': 0.000623,
      'fixation_mse': 0.232406
    }

    >>> gaze.extract_raw_features(g1)
    {
      'saccade': {
        'source_points': [[0,0]],
        'saccade_points': [[0,0], [1,1], [2,2]],
        'target_points': [[2,2]],
        'mean_squared_error': 0.000623
      },
      'fixation': {
        'centroid': [[1.0,1.0]]
        'mean_squared_error': 0.232406,
      }
    }

As an alternative for using the default pretrained classifier, you can train one::

    >>> training_data = [g1, g2, g3]
    >>> classes = ['saccade', 'fixation', 'unknown']
    >>> gc = gaze.GazeClassifier()
    >>> gc.fit(training_data, classes)

The trained classifier has same API as the default::

    >>> gc.predict(g1)
    'saccade'



3. API
======

3.1. gazeclassifier.predict(pointlist)
--------------------------------------

Parameters:

-   pointlist: a list of [x, y] points i.e. a list of lists
    - OR alternatively the result dict from ``extract_features``.
      This is convenient if you need access to the features and want to
      prevent ``predict`` to re-extract them.

Return a string which can be one of the following:

- ``'saccade'``: gaze travels from point A to B and otherways stays still
- ``'fixation'``: gaze has mainly stayed still
- ``'unknown'``: gaze cannot be regarded as any of the above


3.2. gazeclassifier.extract_features(pointlist)
-----------------------------------------------

Parameters:

-  pointlist: a list of [x, y] points i.e. a list of lists

Return a dict that contains mean error and details for each hypothesis. The dict can be fed into ``classify`` for classification.


3.3. gazeclassifier.extract_raw_features(pointlist)
---------------------------------------------------

Parameters:

-  pointlist: a list of [x, y] points i.e. a list of lists

Return a dict that contains mean error and details for each hypothesis. The dict can be fed into ``predict`` for classification.


3.4. gazeclassifier.GazeClassifier()
------------------------------------

A new untrained classifier.

3.5. gazeclassifier.GazeClassifier#fit(pointlists, classes)
-----------------------------------------------------------

3.6. gazeclassifier.GazeClassifier#predict(pointlist_or_features)
-----------------------------------------------------------------


3.7. gazeclassifier.version
---------------------------

The current version string::

    >>> gazeclassifier.version
    '1.2.3'



4. For developers
=================

Tips for the developers of the package.


4.1. Use Git
------------

To develop, clone the repository from GitHub::

    $ git clone https://github.com/infant-cognition-tampere/gazeclassifier-py

Make changes to files, add them to commit, and do commit::

    (edit README.rst)
    $ git add README.rst
    $ git commit -m "Improved documentation"

List files that are not added or not committed::

    $ git status

Push local commits to GitHub::

    $ git push

Ignore some files by editing ``.gitignore``::

    $ nano .gitignore


4.2. Virtualenv
---------------

Manage python versions and requirements by using virtualenv::

    $ virtualenv -p python3.5 gazeclassifier-py
    $ cd gazeclassifier-py
    $ source bin/activate
    ...
    $ deactivate


4.3. Testing
------------

Follow `instructions to install pyenv
<http://sqa.stackexchange.com/a/15257/14918>`_ and then either run quick tests::

    $ python3.5 setup.py test

or run comprehensive tests for multiple Python versions listed in ``tox.ini``::

    $ pyenv local 2.6.9 2.7.10 3.3.6 3.4.3 3.5.0
    $ eval "$(pyenv init -)"
    $ pyenv rehash
    $ tox

Install new pyenv environments for example by::

    $ pyenv install 3.5.0

Validate README.rst at `http://rst.ninjs.org/
<http://rst.ninjs.org/>`_


4.4. Publishing to PyPI
-----------------------

Follow `python packaging instructions
<https://python-packaging-user-guide.readthedocs.org/en/latest/distributing/>`_:

1.  Create an unpacked sdist: ``$ python setup.py sdist``
2.  Create a universal wheel: ``$ python setup.py bdist_wheel --universal``
3.  Go to `PyPI and register the project by filling the package form
    <https://pypi.python.org/pypi?%3Aaction=submit_form>`_ by uploading
    ``gazeclassifier.egg-info/PKG_INFO`` file.
4.  Upload the package with twine:

    1. Sign the dist: ``$ gpg --detach-sign -a dist/gazeclassifier-1.2.3*``
    2. Upload: ``twine upload dist/gazeclassifier-1.2.3*`` (will ask your PyPI password)

5. Package published!

Updating the package takes same steps except the 3rd.


4.5 Version release
-------------------

1.  Change version string in ``gazeclassifier/version.py`` and ``setup.py`` to
    ``'1.2.3'``
2.  Run tox tests. See *4.3. Testing*.
3.  Git commit: ``$ git commit --all -m "v1.2.3 release"``
4.  Create tag: ``$ git tag -a 1.2.3 -m "v1.2.3 stable"``
5.  Push commits and tags: ``$ git push && git push --tags``
6.  Publish to PyPI. See *4.4. Publishing to PyPI*.



5. Versioning
=============

`Semantic Versioning 2.0.0
<http://semver.org/>`_



6. License
==========

`MIT License
<https://opensource.org/licenses/MIT>`_
