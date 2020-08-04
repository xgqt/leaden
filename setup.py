#!/usr/bin/env python3


from setuptools import setup


def readme():
    with open('README.md', encoding='utf-8') as f:
        return f.read()


setup(
    name='leaden',
    version='0.0.1',
    description='',
    author='src_prepare',
    url='https://gitlab.com/src_prepare/leaden',
    long_description=readme(),
    long_description_content_type='text/markdown',
    license='GPL-3',
    keywords="ebuild",
    python_requires=">=3.6.*",
    packages=['leaden'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'leaden = leaden.cmdline:execute',
        ],
    },
    classifiers=[
        'Development Status :: Beta',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Bug Tracking',
    ]
)
