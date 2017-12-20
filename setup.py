from setuptools import setup
try:
    import multiprocessing
except ImportError:
    pass

setup(
    name='httpie-vimond-auth',
    description='Vimond API auth plugin for HTTPie.',
    long_description=open('README.rst').read().strip(),
    version='0.0.1',
    author='Johan Dewe',
    author_email='johan@dewe.net',
    license='MIT',
    url='https://github.com/dewe/httpie-vimond-auth',
    download_url='https://github.com/dewe/httpie-vimond-auth',
    py_modules=['httpie_vimond_auth'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_vimond_auth = httpie_vimond_auth:VimondAuthPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.9.0',
        'pytz>=2017.3'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
