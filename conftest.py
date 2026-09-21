import sys
from pathlib import Path

# Modules are imported flat (import converter), so put their folder on the path.
sys.path.insert(0, str(Path(__file__).parent / "src" / "md2doc"))

