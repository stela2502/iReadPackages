from setuptools import setup, find_packages

setup(
    name='iReadPackage',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy==1.21.0',
        'requests==2.25.1',
    ],
    
    # Optional: Document non-Python requirements in long_description
    long_description="""
    # Non-Python dependencies
    Please ensure you have the following installed:
    - Git (https://git-scm.com/downloads)
    - OpenSSL (https://www.openssl.org/)
    """,
)
