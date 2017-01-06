import unittest
from DisjointSet import DisjointSet

class TestDisjSet(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_create(self):
        s = DisjointSet(10)
        self.assertEqual(len(s), 10)
        self.assertEqual(s.find(1), 1)
        
    def test_union(self):
        s = DisjointSet(10)
        s.union(1,2)
        s.union(3,4)
        self.assertEqual(len(s), 8)
        self.assertEqual(s.find(1), 2)
        
    def test_compress_path(self):
        s = DisjointSet(10)
        s.union(1,2)
        s.union(3,4)
        s.union(1,3)
        self.assertEqual(s.getPath(1), [1,2,4])
        s.find(1)
        self.assertEqual(s.getPath(1), [1,4])
        
if __name__ == "__main__":
    unittest.main()

