"""Unit tests for the contact manager."""

import unittest
from unittest.mock import patch

import contact_manager


class TestContactManager(unittest.TestCase):
    """Test the contact manager functions."""

    def setUp(self):
        """Start each test with an empty contact list."""
        contact_manager.contacts.clear()

    def test_add_contact(self):
        """Check that a new contact is added."""
        contact_manager.add_contact("Ravi", "9876543210")

        self.assertEqual(
            contact_manager.contacts["Ravi"],
            "9876543210"
        )

    def test_find_existing_contact(self):
        """Check that finding a contact returns its number."""
        contact_manager.contacts["Ravi"] = "9876543210"

        result = contact_manager.find_contact("Ravi")

        self.assertEqual(result, "9876543210")

    def test_find_missing_contact(self):
        """Check that a missing contact returns None."""
        with patch("builtins.print"):
            result = contact_manager.find_contact("Unknown")

        self.assertIsNone(result)

    def test_delete_existing_contact(self):
        """Check that an existing contact is deleted."""
        contact_manager.contacts["Ravi"] = "9876543210"

        with patch("builtins.print"):
            contact_manager.delete_contact("Ravi")

        self.assertNotIn("Ravi", contact_manager.contacts)

    def test_delete_missing_contact(self):
        """Check that deleting a missing contact does not crash."""
        with patch("builtins.print") as mock_print:
            contact_manager.delete_contact("Unknown")

        mock_print.assert_called_with("Contact not found.")

    def test_duplicate_contact(self):
        """Check that duplicate names raise the custom exception."""
        contact_manager.add_contact("Ravi", "9876543210")

        with self.assertRaises(
            contact_manager.DuplicateContactError
        ):
            contact_manager.add_contact("Ravi", "1234567890")


if __name__ == "__main__":
    unittest.main()