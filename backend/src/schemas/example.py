from dataclasses import dataclass


@dataclass
class ExampleList:
    example: list[str]

    def __len__(self) -> int:
        return len(self.example)
