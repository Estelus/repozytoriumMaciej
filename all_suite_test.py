import unittest
from unittest.loader import makeSuite
from test_cases.framework import Test
from test_cases.Remind_Password import TestRemindPassword
from test_cases.add_new_player import TestAddPlayer
from test_cases.add_new_player_with_youtube_link import TestAddPlayerWithYoutubeLink
from test_cases.log_out_from_the_system import TestLogOutFromSystem
from test_cases.login_Invalid_Password import TestLogInWithInvalidPassword


def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(unittest.makeSuite(TestAddPlayer))
   test_suite.addTest(unittest.makeSuite(TestRemindPassword))
   test_suite.addTest(unittest.makeSuite(TestAddPlayerWithYoutubeLink))
   test_suite.addTest(unittest.makeSuite(TestLogOutFromSystem))
   test_suite.addTest(unittest.makeSuite(TestLogInWithInvalidPassword))
   return test_suite


if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())