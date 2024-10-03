import os
from pathlib import Path
import logging

# Correct list of files with the missing comma and proper backslashes
list_of_files = [
    # GitHub Actions Workflow (for CI/CD automation)
    ".github\\workflows\\.gitkeep",  
    
    # Package initialization for the src directory
    "src\\__init__.py",  
    
    # Initialization and Python files for components (like data ingestion, transformation, etc.)
    "src\\components\\__init__.py",  
    "src\\components\\data_ingestion.py",  # Ingest data from different sources
    "src\\components\\data_transformation.py",  # Transform data (cleaning, feature engineering, etc.)
    "src\\components\\model_trainer.py",  # Train machine learning models
    "src\\components\\model_evaluation.py",  # Evaluate model performance
    
    # Initialization and pipeline files (training and prediction pipelines)
    "src\\pipeline\\__init__.py",  
    "src\\pipeline\\training_pipeline.py",  # Pipeline for training the model
    "src\\pipeline\\prediction_pipeline.py",  # Pipeline for making predictions
    
    # Initialization and utility files (common reusable functions)
    "src\\utils\\__init__.py",  
    "src\\utils\\utils.py",  # Utility functions used across the project
    
    # Logger to track the application's logging info
    "src\\logger\\logging.py",  
    
    # Custom exception handling for the project
    "src\\exception\\exception.py",  
    
    # Unit and integration test initialization files
    "tests\\unit\\__init__.py",  # Initialization for unit tests
    "tests\\integration\\__init__.py",  # Initialization for integration tests
    
    # Shell script for initial project setup (e.g., installing dependencies)
    "init_setup.sh",  
    
    # List of project dependencies for production
    "requirements.txt",  
    
    # List of dependencies for development (e.g., testing, linting)
    "requirements_dev.txt",  
    
    # Setup script for packaging and installing the project
    "setup.py",  
    
    # TOML file for configuring build tools (e.g., Poetry)
    "pyproject.toml",  
    
    # Tox configuration for testing the project in multiple environments
    "tox.ini",  
    
    # Jupyter notebook for experiments or exploratory analysis
    "experiment\\experiments.ipynb"  
]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file

