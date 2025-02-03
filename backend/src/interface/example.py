from abc import ABC, abstractmethod
from pathlib import Path


class ExampleInterface(ABC):
    """Abstract interface for file management."""

    @abstractmethod
    def run_example(self, file_path: Path) -> None:
        """Archive existing files with the same name."""
        pass
