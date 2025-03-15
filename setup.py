from setuptools import setup, find_packages

setup(
    name="assistant",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'sounddevice>=0.4',
        'whisper-ctranslate2>=3.0',
        'coqui-tts>=0.22',
        'requests>=2.28',
        'numpy>=1.26'
    ],
    entry_points={
        'console_scripts': [
            'web-assistant=web_assistant.cli:main',
        ],
    },
)