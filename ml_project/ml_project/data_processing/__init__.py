"""
Data processing module for loading and preprocessing data.
"""
from typing import Optional, Union
import pandas as pd


class DataLoader:
    """A class to handle loading data from various file formats."""

    def __init__(self):
        """Initialize the DataLoader."""
        pass

    def read_csv(self, filepath: str, **kwargs) -> pd.DataFrame:
        """
        Read data from a CSV file.

        Args:
            filepath: Path to the CSV file
            **kwargs: Additional arguments to pass to pd.read_csv

        Returns:
            pd.DataFrame: Loaded data

        Raises:
            FileNotFoundError: If the file doesn't exist
            pd.errors.EmptyDataError: If the file is empty
        """
        try:
            return pd.read_csv(filepath, **kwargs)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filepath}")
        except pd.errors.EmptyDataError:
            raise pd.errors.EmptyDataError("The file is empty")

    def read_parquet(self, filepath: str, **kwargs) -> pd.DataFrame:
        """
        Read data from a Parquet file.

        Args:
            filepath: Path to the Parquet file
            **kwargs: Additional arguments to pass to pd.read_parquet

        Returns:
            pd.DataFrame: Loaded data

        Raises:
            FileNotFoundError: If the file doesn't exist
        """
        try:
            return pd.read_parquet(filepath, **kwargs)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filepath}")
