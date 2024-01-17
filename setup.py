from setuptools import setup, find_packages

setup(
    name='linalg',  # Replace with your project's name
    version='0.1.0',  # The initial release version
    author='Chris Camano',  # Replace with your name
    author_email='ccamano@sfsu.edu',  # Replace with your email
    description='An interactive series of Jupyter notebooks for learning linear algebra with Manim',  # Short description
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/yourproject',  # Replace with the URL to your project
    packages=find_packages(),  # This will automatically find any packages you have
    install_requires=[
        # Add your project dependencies here
        'numpy',
        'matplotlib',
        'manim',
        'jupyter',
        # etc.
    ],
    classifiers=[
        # Choose classifiers that best describe your project
        # See the full list at https://pypi.org/classifiers/
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Topic :: Education',
        'License :: OSI Approved :: MIT License',  # If you are using MIT License
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.8',  # Specify the min Python version
)
