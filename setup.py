from setuptools import setup

setup(
    name='scrapy-querycleaner',
    version='1.0.0',
    license='BSD',
    description='Scrapy spider middleware to clean up query parameters in request URLs',
    author='Scrapinghub',
    author_email='info@scrapinghub.com',
    url='https://github.com/scrapy-plugins/scrapy-querycleaner',
    packages=['scrapy_querycleaner'],
    platforms=['Any'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=['scrapy>=1.0', 'six']
)
