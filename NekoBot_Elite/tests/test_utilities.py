"""
Tests for bot/plugins/utilities.py.

_safe_calc is the highest-risk piece here: it evaluates arbitrary
user-supplied arithmetic text. It must accept ordinary arithmetic and
reject anything that isn't — no eval() of arbitrary Python, no name
lookups, no function/attribute access, no unbounded exponents.
"""
from __future__ import annotations

import os
import sys
import tempfile
import unittest

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

_TMP_DB = tempfile.NamedTemporaryFile(prefix="test_utilities_", suffix=".db", delete=False)
_TMP_DB.close()
os.environ.setdefault("BOT_TOKEN", "123:test")
os.environ.setdefault("OWNER_ID", "123456")
os.environ["DATABASE_URL"] = f"sqlite+aiosqlite:///{_TMP_DB.name}"

from bot.plugins.utilities import _safe_calc, register  # noqa: E402


class TestSafeCalc(unittest.TestCase):
    def test_basic_arithmetic(self):
        self.assertEqual(_safe_calc("2+2"), 4)
        self.assertEqual(_safe_calc("(3+5)*2"), 16)
        self.assertEqual(_safe_calc("10 / 4"), 2.5)
        self.assertEqual(_safe_calc("10 // 4"), 2)
        self.assertEqual(_safe_calc("10 % 3"), 1)

    def test_exponentiation_both_notations(self):
        self.assertEqual(_safe_calc("2**10"), 1024)
        self.assertEqual(_safe_calc("2^10"), 1024)

    def test_negative_numbers(self):
        self.assertEqual(_safe_calc("-5+3"), -2)
        self.assertEqual(_safe_calc("-(2+3)"), -5)

    def test_division_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            _safe_calc("1/0")

    def test_oversized_exponent_rejected(self):
        with self.assertRaises(ValueError):
            _safe_calc("9999999**9999999")

    def test_function_call_rejected(self):
        with self.assertRaises(Exception):
            _safe_calc("__import__('os').system('echo pwned')")

    def test_name_lookup_rejected(self):
        with self.assertRaises(Exception):
            _safe_calc("os.system('echo pwned')")

    def test_attribute_access_rejected(self):
        with self.assertRaises(Exception):
            _safe_calc("().__class__")

    def test_string_literal_rejected(self):
        with self.assertRaises(Exception):
            _safe_calc("'a' * 1000000")


class TestUtilitiesRegistration(unittest.TestCase):
    def test_register_adds_handlers_without_error(self):
        added = []

        class FakeApp:
            def add_handler(self, handler, group=0):
                added.append(handler)

        register(FakeApp())
        self.assertGreater(len(added), 0)

    def test_no_duplicate_command_strings_within_this_plugin(self):
        from telegram.ext import CommandHandler

        added = []

        class FakeApp:
            def add_handler(self, handler, group=0):
                added.append(handler)

        register(FakeApp())
        seen = set()
        for h in added:
            if isinstance(h, CommandHandler):
                for c in h.commands:
                    self.assertNotIn(c, seen, f"/{c} registered twice within utilities.py")
                    seen.add(c)


if __name__ == "__main__":
    unittest.main()
