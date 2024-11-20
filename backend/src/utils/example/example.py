from core.logging import logger


def run_example(example: str) -> str:
    """Process example and return example"""
    # Add computation information
    logger.info(f"Received information {example}")
    return example
