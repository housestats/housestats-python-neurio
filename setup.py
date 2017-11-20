from setuptools import setup, find_packages

setup(
    name='housestats-python-neurio',
    version='0.1',
    author='Lars Kellogg-Stedman',
    author_email='lars@oddbit.com',
    description='sensor for neurio',
    license='GPLv3',
    url='https://github.com/larsks/housestats-python-neurio',
    packages=find_packages(),
    entry_points={
        'housestats.sensor': [
            'neurio=housestats_python_neurio.sensor:NeurioSensor',
        ],
    }
)
