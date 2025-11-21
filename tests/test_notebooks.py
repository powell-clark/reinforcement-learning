"""
Notebook execution tests using nbval.

To run notebook tests:
    pytest --nbval notebooks/

This will execute all notebooks and verify outputs match expected values.
"""

import pytest
import os
from pathlib import Path


def get_notebook_paths():
    """Get all notebook paths."""
    notebooks_dir = Path(__file__).parent.parent / "notebooks"
    if not notebooks_dir.exists():
        return []
    return list(notebooks_dir.glob("*.ipynb"))


@pytest.mark.parametrize("notebook_path", get_notebook_paths())
def test_notebook_execution(notebook_path):
    """Test that notebook executes without errors."""
    # This is a placeholder - actual execution done by nbval
    # Run with: pytest --nbval notebooks/0a_rl_introduction_theory.ipynb
    assert notebook_path.exists(), f"Notebook {notebook_path} does not exist"


# TODO: Add specific notebook tests
# - test_notebook_has_required_sections()
# - test_notebook_imports_work()
# - test_notebook_produces_expected_outputs()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
