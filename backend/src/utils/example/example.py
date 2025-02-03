from core.logging import logger
from interface.example import ExampleInterface


class Example(ExampleInterface):
    def __init__(self, example_text: str) -> None:
        self.example_text = example_text

    def run_example(example: str) -> str:
        """Process example and return example"""
        # Add computation information
        logger.info(f"Received information {example}")
        return example
