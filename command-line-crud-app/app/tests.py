from django.test import TestCase
from app import models


# Create your tests here.


class Test_Char(TestCase):
    def test_create(self):
        char = models.create_Char(
            "timmy",
            "bat",
            True,
        )

        self.assertEqual(char.name, "timmy")
        self.assertEqual(char.item, "bat")
        self.assertTrue(char.in_out)
        self.assertEqual(len(models.view_all()), 1)

    def test_can_view_all_char_at_once(self):
        char_data = [
            {
                "name": "Elias",
                "item": "switch",
                "in_out": True,
            },
            {
                "name": "Martin",
                "item": "case",
                "in_out": False,
            },
            {
                "name": "Alma",
                "item": "phone",
                "in_out": True,
            },
        ]

        for data in char_data:
            models.create_Char(
                data["name"],
                data["item"],
                data["in_out"],
            )

        chars = models.view_all()

        self.assertEqual(len(chars), len(char_data))

        chars_data = sorted(char_data, key=lambda c: c["name"])
        chars = sorted(chars, key=lambda c: c.name)

        for data, contact in zip(chars_data, chars):
            self.assertEqual(data["name"], contact.name)
            self.assertEqual(data["item"], contact.item)
            self.assertEqual(data["in_out"], contact.in_out)

    def test_can_search_by_name(self):
        char_data = [
            {
                "name": "Elias",
                "item": "switch",
                "in_out": True,
            },
            {
                "name": "Martin",
                "item": "case",
                "in_out": False,
            },
            {
                "name": "Alma",
                "item": "phone",
                "in_out": True,
            },
        ]

        for contact_data in char_data:
            models.create_Char(
                contact_data["name"],
                contact_data["item"],
                contact_data["in_out"],
            )

        self.assertIsNone(models.view_filter("aousnth"))

        contact = models.view_filter("Alma")

        self.assertIsNotNone(contact)
        self.assertEqual(contact.item, "phone")

    def test_can_view_favorites(self):
        char_data = [
            {
                "name": "Elias",
                "item": "switch",
                "in_out": True,
            },
            {
                "name": "Martin",
                "item": "case",
                "in_out": False,
            },
            {
                "name": "Alma",
                "item": "phone",
                "in_out": True,
            },
        ]

        for contact_data in char_data:
            models.create_Char(
                contact_data["name"],
                contact_data["item"],
                contact_data["in_out"],
            )

        self.assertEqual(len(models.view_in_out()), 2)

    def test_can_update_contacts_email(self):
        char_data = [
            {
                "name": "Elias",
                "item": "switch",
                "in_out": True,
            },
            {
                "name": "Martin",
                "item": "case",
                "in_out": False,
            },
            {
                "name": "Alma",
                "item": "phone",
                "in_out": True,
            },
        ]

        for contact_data in char_data:
            models.create_Char(
                contact_data["name"],
                contact_data["item"],
                contact_data["in_out"],
            )

        models.update("Elias", "laptop")

        self.assertEqual(models.view_filter("Elias").item, "laptop")

    def test_can_delete_contact(self):
        char_data = [
            {
                "name": "Elias",
                "item": "switch",
                "in_out": True,
            },
            {
                "name": "Martin",
                "item": "case",
                "in_out": False,
            },
            {
                "name": "Alma",
                "item": "phone",
                "in_out": True,
            },
        ]

        for contact_data in char_data:
            models.create_Char(
                contact_data["name"],
                contact_data["item"],
                contact_data["in_out"],
            )

        models.delete("Martin")

        self.assertEqual(len(models.view_all()), 2)
