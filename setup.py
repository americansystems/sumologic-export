"""Our python packaging stuff."""


from setuptools import setup


setup(

    # Basic package information:
    name = 'sumologic-export',
    version = '0.0.3',
    scripts = ['sumologic-export'],

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = ['requests>=2.3.0', 'boto3>=1.9.0'],

    # Metadata for PyPI:
    author = 'Caleb Fogleman',
    author_email = 'caleb.fogleman@americansystems.com',
    license = 'UNLICENSE',
    url = 'https://github.com/cafogleman/sumologic-export',
    keywords = ['sumologic', 'logs', 'export', 'utility'],
    description = 'Easily export your Sumologic log data.',
    long_description = 'Easily export your Sumologic log data.',

)
