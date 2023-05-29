import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = []
# 打开文件
with open('requirements.txt', 'r') as file:
    # 逐行读取文件内容
    for line in file:
        line = line.strip()  # 去除行末尾的换行符和空格
        if line:  # 忽略空行
            install_requires.append(line)  # 将行添加到集合列表中

setuptools.setup(
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    name="Python alfred auto",
    version="1.0.0",
    author="Kings",
    author_email="kings1990@gmail.com",
    description="Some python alfred auto script",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kings1990",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.7',
)
