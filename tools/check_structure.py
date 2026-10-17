#!/usr/bin/env python3
"""Static inventory of the original Logisim-evolution XML circuit.

Does NOT simulate circuit operation or establish electrical correctness.
Requires Python 3 standard library only.
"""
from collections import Counter
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

PROJECT = Path(__file__).resolve().parents[1] / "circuit" / "4-bit-microprocessor-datapath.circ"


def main() -> int:
    try:
        root = ET.parse(PROJECT).getroot()
    except (OSError, ET.ParseError) as exc:
        print(f"ERROR: unable to read Logisim XML: {exc}", file=sys.stderr)
        return 1

    circuits = {c.get("name"): c for c in root.findall("circuit")}
    print(f"Source: {PROJECT.name}")
    print(f"Logisim source version: {root.get('source', 'unspecified')}")
    print("Circuits:", ", ".join(sorted(circuits)))

    errors = []
    for name in ("main", "ALU"):
        if name not in circuits:
            errors.append(f"Missing subcircuit: {name}")

    if errors:
        for error in errors:
            print("FAIL:", error, file=sys.stderr)
        return 1

    main = Counter(x.get("name") for x in circuits["main"].findall("comp"))
    alu = Counter(x.get("name") for x in circuits["ALU"].findall("comp"))
    expected_main = {"Register": 4, "Multiplexer": 3, "Decoder": 1, "ALU": 1, "Clock": 1, "LED": 1}
    expected_alu = {"Adder": 1, "Subtractor": 1, "AND Gate": 1, "OR Gate": 1, "NOR Gate": 1, "Multiplexer": 1}

    for name, counts, expected in (("main", main, expected_main), ("ALU", alu, expected_alu)):
        print(f"\n{name} ({sum(counts.values())} components):")
        for component, minimum in expected.items():
            actual = counts[component]
            print(f"  {component:16s} {actual:2d}  {'OK' if actual >= minimum else 'MISSING'}")
            if actual < minimum:
                errors.append(f"{name}: expected >= {minimum} {component}, found {actual}")

    if errors:
        print("\nFAIL: " + "; ".join(errors), file=sys.stderr)
        return 1

    print("\nPASS: expected circuit topology/components are present.")
    print("NOTE: this is NOT a Logisim simulation or functional test.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
