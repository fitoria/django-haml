from haml.management.commands.compilehaml import compile_haml
import unittest
import os

class CompileHamlTestCase(unittest.TestCase):

    def testAll(self):
        tests = ['test1', 'test2']

        for test in tests:
            test_file = 'tests/fixtures/%s.html' % (test,)
            if os.path.isfile(test_file):
                os.unlink(test_file)
                
        compile_haml(['tests'])
        
        for test in tests:
            test_file = 'tests/fixtures/%s.html' % (test,)
            assert os.path.isfile(test_file)
            assert os.system('cmp %s %s.expected' % (test_file, test_file)) == 0

def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(CompileHamlTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
