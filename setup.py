from setuptools import setup, find_packages

setup(
    name='bangshow',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bangshow = bangshow.main:main',  # 这里的 main 是你的主函数
        ],
    },
    package_data={
        'bangshow': ['slidesplayer'],  # 包含脚本
    },
    install_requires=[
        'requests',
        'selenium',
        'setuptools'
    ],
    author='sprooc',
    author_email='1127626033@qq.com',
    description='Bang Dream Images Display Tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sprooc/bangshow',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
