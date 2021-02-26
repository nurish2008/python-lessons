# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 21:57:20 2021

@author: lesson-36
"""

import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        name = get_full_name('alijon', 'valiev')
        self.assertEqual(name,'Alijon Valiev')
        
    def test_otasining_ismi(self):
        name = get_full_name('alijon', 'valiev', 'olimovich')
        self.assertEqual(name,'Alijon Olimovich Valiev')
unittest.main()
