from distutils.core import setup


with open('README.rst') as file:
    long_description = file.read()


setup(
    name='scrapy-notifications',
    version='0.1.0',
    author='Pablo SEMINARIO',
    author_email='pabluk@gmail.com',
    url='https://github.com/pabluk/scrapy-notifications',
    license='GNU General Public License v3 (GPLv3)',
    description="Send HTTP notifications on spider actions",
    long_description=long_description,
    packages=['scrapy_notifications'],
    provides=['scrapy_notifications (0.1.0)'],
    requires=['Scrapy (>=0.16)'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
