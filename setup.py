import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = (
    '.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')


def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                            or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                            or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out


setup(name='docassemble.MSM01ClientIntake',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description='# docassemble.MSM01ClientIntake\r\n\r\nA docassemble extension.\r\n\r\n## Author\r\n\r\nShelley Toth, toth0018@flinders.edu.au\r\nShai Barboza, barb0176@flinders.edu.au\r\nPaige Bowers, bowe0153@flinders.edu.au\r\nNiamh Keller, kell0481@flinders.edu.au\r\nCaitlin Driscoll, dris0025@flinders.edu.au\r\nBrandon Trimboli, trim0056@flinders.edu.au\r\n\r\n## Description\r\n\r\nThis file operates as the client intake form for MSM Legal Pty Ltd. It asks the client for their personal information and details about their issue in the areas of Wills, Estates and Probate Law, or Migration Law.',
      long_description_content_type='text/markdown',
      author='Paige Bowers',
      author_email='bowe0153@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(
          where='docassemble/MSM01ClientIntake/', package='docassemble.MSM01ClientIntake'),
      )
