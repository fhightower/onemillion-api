#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test the API."""

import unittest

import onemillion_api


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = onemillion_api.app.test_client()

    def test_landing_page(self):
        rv = self.app.get('/')
        assert b'<b>Onemillion API</b> - Check to see if a domain is in a top-onemillion domain list.' in rv.data

    def test_empty_domain_submission_redirect(self):
        """If no domain is given, expect a redirect to the index page."""
        rv = self.app.post('/onemillion', data={'domain': ''}, follow_redirects=True)
        assert rv.status_code == 200
        assert b'<b>Onemillion API</b> - Check to see if a domain is in a top-onemillion domain list.' in rv.data
        assert b'Please enter a domain.' in rv.data

    def test_domain_submission_redirect(self):
        domain = 'example.com'
        rv = self.app.post('/onemillion', data={'domain': domain})
        assert bytes(str('/onemillion/{}'.format(domain)), 'utf-8') in rv.data
        assert rv.status_code == 302

    def test_domain_retrieval(self):
        domain = 'example.com'
        rv = self.app.get('/onemillion/{}'.format(domain))
        assert len(rv.data) < 5
        # make sure the response can be cast as an integer
        assert int(rv.data) < 5000

    def test_obscure_domain_retrieval(self):
        domain = 'gaggle.com'
        rv = self.app.get('/onemillion/{}'.format(domain))
        assert rv.data == b'None'
