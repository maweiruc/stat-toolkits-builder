from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_registry  # noqa: E402


class RegistryValidationTest(unittest.TestCase):
    def test_default_registry_validates(self) -> None:
        errors = validate_registry.validate_registry(
            ROOT / "examples" / "registry.yaml",
            strict=False,
        )
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
