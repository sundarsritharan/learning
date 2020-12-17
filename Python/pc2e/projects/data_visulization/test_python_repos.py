# Unit test class to test github project visualizations
import unittest
import python_repos as pr 

class PythonReposeTestClass(unittest.TestCase):
    """ A class to unit test python_repos.py """

    def setUp(self):
        """ call all the function in python_repos.py and test separately """ 
        self.r = pr.get_response('python')
        self.repo_dicts = pr.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        
    def test_get_response(self):
        """Test that we get a valid response."""
        self.assertEqual(self.r.status_code,200)

    def test_items_returned(self):
        """Test that we're getting the data we think we are."""
        # We should get dicts for 30 repositories.
        self.assertEqual(len(self.repo_dicts), 30)

        # Repositories should have required keys.
        required_keys = ['name', 'owner', 'stargazers_count', 'html_url']
        for key in required_keys:
            self.assertTrue(key in self.repo_dict.keys())
    
if __name__ == '__main__':
    unittest.main()
