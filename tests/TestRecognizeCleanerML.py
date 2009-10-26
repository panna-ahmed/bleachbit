# vim: ts=4:sw=4:expandtab

## BleachBit
## Copyright (C) 2009 Andrew Ziem
## http://bleachbit.sourceforge.net
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.



"""
Test case for RecognizeCleanerML
"""



import sys
import unittest

sys.path.append('.')
from bleachbit.RecognizeCleanerML import hashdigest, HAVE_HASHLIB



class TestRecognizeCleanerML(unittest.TestCase):
    """Test cases for RecognizeCleanerML"""

    def test_hash(self):
        """Unit test for hash()"""
        digest = hashdigest('bleachbit')
        if HAVE_HASHLIB:
            self.assertEqual(len(digest), 128)
            self.assertEqual(digest[1:10], '6382c203e')
        else:
            self.assertEqual(len(digest), 72)
            self.assertEqual(digest[1:10], '0d4a3172f')


if __name__ == '__main__':
    unittest.main()
