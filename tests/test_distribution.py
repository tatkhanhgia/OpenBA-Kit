import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class DistributionTest(unittest.TestCase):
    def test_clean_project_and_global_installs(self):
        for scope in ("project", "global"):
            with self.subTest(scope=scope), tempfile.TemporaryDirectory() as temp:
                home = Path(temp) / "fake home"
                project = Path(temp) / "fake project"
                feature = project / "docs" / "booking"
                feature.mkdir(parents=True)
                install = (project if scope == "project" else home) / ".agents" / "skills"
                shutil.copytree(ROOT / "skills", install)
                self.assertEqual((install / "LICENSE").read_bytes(), (ROOT / "LICENSE").read_bytes())

                for skill in install.glob("*/SKILL.md"):
                    references = re.findall(
                        r"\x60((?:\./|\.\./)[^\x60\n ]+)\x60", skill.read_text(encoding="utf-8")
                    )
                    for reference in references:
                        resolved = (skill.parent / reference).resolve()
                        self.assertIn(install.resolve(), resolved.parents)
                        self.assertTrue(resolved.is_file(), (skill.name, reference))

                for name, template, rule, heading in (
                    ("prd", "01-prd.md", "01-fr-naming-convention.md", "Product Requirements"),
                    ("srs", "08-srs.md", "05-srs-ieee-830.md", "SRS Master"),
                    ("preview", "31-wireframe-html.html", "18-knowledge-graph-metadata.md", "<html"),
                ):
                    skill = install / name / "SKILL.md"
                    instructions = skill.read_text(encoding="utf-8")
                    for filename, expected in ((template, heading), (rule, "#")):
                        path = next(
                            match for match in re.findall(r"\x60([^\x60\n]+)\x60", instructions)
                            if match.endswith("/" + filename)
                        )
                        self.assertIn(expected, (skill.parent / path).read_text(encoding="utf-8"))

                for agent in (".claude", ".hermes"):
                    other = home / agent / "skills" / "diagram-design" / "scripts"
                    other.mkdir(parents=True)
                    for helper in ("mermaid_extract.py", "export_svg.py"):
                        (other / helper).write_text("raise SystemExit('wrong helper')\n")

                (feature / "flows.md").write_text(
                    "```mermaid\nsequenceDiagram\n"
                    "participant Reader\nparticipant Catalog\n"
                    "Reader->>Catalog: Reserve a book\n```\n",
                    encoding="utf-8",
                )
                preview = install / "preview" / "SKILL.md"
                relative_renderer = re.search(
                    r"\$SKILL_DIR/([^\x22]+)", preview.read_text(encoding="utf-8")
                ).group(1)
                command = [sys.executable, str(preview.parent / relative_renderer), "docs/booking/"]
                options = dict(cwd=project, env={**os.environ, "HOME": str(home)},
                               capture_output=True, text=True)
                result = subprocess.run(command, **options)
                self.assertEqual(result.returncode, 0, result.stderr)
                output = feature / "diagrams"
                self.assertIn("Reserve a book", (output / "flows-1.html").read_text(encoding="utf-8"))
                svg = ET.parse(output / "flows-1.svg").getroot()
                self.assertEqual(svg.tag, "{http://www.w3.org/2000/svg}svg")
                self.assertIn("flows-1.html", (output / "index.html").read_text(encoding="utf-8"))

                shutil.rmtree(output)
                exporter = install / "diagram-design" / "scripts" / "export_svg.py"
                exporter.write_text("raise SystemExit('fixture export failure')\n")
                failure = subprocess.run(command, **options)
                self.assertNotEqual(failure.returncode, 0)
                self.assertIn("fixture export failure", failure.stderr)
                self.assertNotIn("Hoàn thành", failure.stdout)
                self.assertEqual(list(output.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
