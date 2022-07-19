#!/usr/bin/env python3

__author__ = "Surya Banerjee"

import os

from django.urls import reverse
from django.conf import settings
from django.core import management
from django.test import override_settings
from django.test import TestCase, Client

from elements.api.models import AppData


@override_settings(CACHEOPS_ENABLED=False)
class AppDataAPITest(TestCase):
    def setUp(self):
        # Import csv into db
        management.call_command(
            "importcsv",
            os.path.join(settings.BASE_DIR, "elements/api/test_data/testdata.csv"),
            mappings="title,description,image",
            model="api.AppData",
            delimiter=",",
        )
        self.client = Client()
        self.valid_titles = ["title", "apple", "computer", "surya"]
        self.valid_descriptions = [
            "description",
            "red fruit",
            "computational machine",
            "human",
        ]
        self.valid_images = [
            "image",
            "https://www.collinsdictionary.com/images/thumb/apple_158989157_250.jpg",
            "https://britishlibrary.typepad.co.uk/.a/6a00d8341c464853ef01bb07aa6800970d-pi",
            "https://avatars.githubusercontent.com/u/21195061?s=400&u=cd6ab06db049a75aa2d7949d308773d00e0707e1&v=4",
        ]

    def test_api_list(self):
        response = self.client.get(reverse("appdata-list"))
        self.assertEqual(len(response.json()), 4)

        for i in range(4):
            self.assertEqual(response.json()[i]["title"], self.valid_titles[i])

    def test_api_detail(self):
        for i in range(1, 5):
            response = self.client.get(reverse("appdata-list") + f"{i}/")
            self.assertEqual(response.json()["title"], self.valid_titles[i - 1])
            self.assertEqual(
                response.json()["description"], self.valid_descriptions[i - 1]
            )
            self.assertEqual(response.json()["image"], self.valid_images[i - 1])
