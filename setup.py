from setuptools import setup, find_namespace_packages
import os

version = '1.10.3+tooltip.2'


def read(*rnames):
    """Read a file from a path."""
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


long_description = "\n\n".join([
    read('README.rst'),
    read('js', 'jqueryui', 'test_jqueryui.rst'),
    read('CHANGES.rst'),
])


setup(
    name='js.jqueryui',
    version=version,
    description="jQuery UI packaged for fanstatic.",
    long_description=long_description,
    classifiers=[],
    url='https://bitbucket.org/fanstatic/js.jqueryui',
    keywords='',
    author='Fanstatic Developers',
    author_email='fanstatic@googlegroups.com',
    license='BSD',
    packages=find_namespace_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'js.jquery',
    ],
    entry_points={
        'fanstatic.libraries': [
            'jqueryui = js.jqueryui:library',
        ],
        'console_scripts': [
            'download_jqueryui = js.jqueryui.download:main'],
    },
    extras_require={
        'scripts': [
            'lxml',
        ],
    }
)
