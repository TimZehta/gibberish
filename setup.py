import os
try:
    # use setuptools if available
    from setuptools import setup
    kwargs = {
        'entry_points': {'console_scripts':
            'glarg = glarg:console_main',
        }
    }
except ImportError:
    # fall back to distutils
    from distutils import setup
    kwargs = {}


base_dir = os.path.dirname(os.path.abspath(__file__))

setup(
    name='Glarg',
    description="A pseudo-word generator",
    version='0.2',
    author='Timid Robot Zehta',
    author_email='tim@zehta.me',
    url='https://github.com/TimZehta/glarg',
    py_modules=('glarg',),
    license='MIT License',
    long_description=open(os.path.join(base_dir, 'README.rst')).read(),
    **kwargs
)
