import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'envrun',
    'hvac',
]

dev_require = [
    'black',
]

setup(
    name='envrun-vault',
    version='0.0.1',
    description='An envrun extension providing a Vault backend.',
    long_description=README + '\n\n' + CHANGES,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Topic :: Security",
        "Topic :: Utilities",
    ],
    author='Jan Likar',
    author_email='jan.likar@protonmail.com',
    url='https://github.com/JanLikar/envrun-vault',
    keywords='cli util secret-managament',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={'dev': dev_require},
    install_requires=requires,
    entry_points="""\
        [envrun.backends]
        vault=envrun_vault:Vault
      """,
    python_requires='>=3.6',
)
