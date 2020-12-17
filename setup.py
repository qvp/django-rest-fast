from setuptools import setup

README = '''
Fast create REST API with Swagger documentation based on native django views and forms.
'''

setup(
    name='django-rest-fast',
    version='0.0.2',
    packages=['django_rest_fast'],
    description='Fast create REST API with Swagger documentation based on native django views and forms.',
    long_description=README,
    author='Alexander Kuzmenko',
    author_email='mail@alex.md',
    url='https://github.com/qvp/django-rest-fast',
    download_url='',
    license='MIT',
    install_requires=[],
    python_requires='>=3.6'
)
