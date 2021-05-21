from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

longDescription = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='numeralsystems',
    version='1.0.0',
    description='An implementation for generalized numeral systems.',
    long_description=longDescription,
    long_description_content_type='text/markdown',
    url='https://github.com/HazelTheWitch/NumeralSystems',
    author='Hazel Rella',
    author_email='hazeltrinity@protonmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(),
    python_requires='>=3.6, <4',
    install_requires=[

    ],
    project_urls={
        'Report an Issue': 'https://github.com/HazelTheWitch/NumeralSystems/issues',
        'Buy Me a Coffee': 'https://ko-fi.com/hazeltrinity'
    }
)
