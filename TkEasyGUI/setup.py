from setuptools import setup, find_packages

setup(
    name='TkEasyGUI_old_compatible',  # パッケージ名
    version='0.1.0',  # バージョン
    packages=find_packages(),  # 自動でパッケージを探してくれる
    description='Your package description',  # パッケージの簡単な説明
    long_description=open('README.md').read(),  # README.mdの内容を長い説明として読み込む
    long_description_content_type='text/markdown',  # long_descriptionの形式を指定
    author='Your Name',  # 作成者名
    author_email='your.email@example.com',  # 作成者のメールアドレス
    url='https://github.com/yourgithub/yourrepository',  # プロジェクトのURL
    install_requires=[
        'numpy',  # 依存関係の例
        'pandas',  # 別の依存関係の例
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)