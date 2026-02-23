# setup.py
from setuptools import setup, find_packages

setup(
    name='scallion-django',
    version='1.0.3',
    packages=find_packages(),
    # 将common导出来
    include_package_data=True,
    # 添加依赖
    install_requires=[
        'Django>=4.2',
        'djangorestframework==3.15.2',
    ],
    python_requires='>=3.8',
    author='Rustor',
    author_email='18048587325@163.com',
    description='The basic django code',
    url='https://github.com/yourusername/your-repo',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
)