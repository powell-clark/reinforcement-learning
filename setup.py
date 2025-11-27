"""
Setup configuration for Reinforcement Learning Curriculum

This allows the algorithms module to be installed as a package:
    pip install -e .

Or for production:
    pip install .
"""

from setuptools import setup, find_packages
import os

# Read README for long description
def read_file(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# Read requirements
def read_requirements(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return []

setup(
    name="rl-curriculum",
    version="2.0.0",
    author="Powell-Clark Limited",
    author_email="contact@powell-clark.com",
    description="Production-ready Reinforcement Learning curriculum from Classical RL to RLHF",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/powell-clark/reinforcement-learning",
    packages=find_packages(exclude=["tests", "notebooks", "examples"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Education",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "dev": read_requirements("requirements-dev.txt"),
        "all": read_requirements("requirements.txt") + read_requirements("requirements-dev.txt"),
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.yml", "*.yaml"],
    },
    entry_points={
        "console_scripts": [
            # Add CLI commands here if needed
            # Example: "rl-train=algorithms.cli:train",
        ],
    },
    keywords=[
        "reinforcement-learning",
        "deep-reinforcement-learning",
        "machine-learning",
        "rlhf",
        "ppo",
        "dqn",
        "sac",
        "chatgpt",
        "llm-alignment",
        "artificial-intelligence",
        "education",
        "tutorial",
        "curriculum",
    ],
    project_urls={
        "Documentation": "https://github.com/powell-clark/reinforcement-learning/blob/main/README.md",
        "Source": "https://github.com/powell-clark/reinforcement-learning",
        "Tracker": "https://github.com/powell-clark/reinforcement-learning/issues",
        "Changelog": "https://github.com/powell-clark/reinforcement-learning/blob/main/CHANGELOG.md",
    },
)
