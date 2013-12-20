import haml_test

def suite():
    import unittest
    suite = unittest.TestSuite()
    suite.addTests(haml_test.suite())
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
    
