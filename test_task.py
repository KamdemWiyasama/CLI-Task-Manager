import unittest
from task import Task

class TestTask(unittest.TestCase):
    def test_mark_completed(self): #test case for mark_completed method
        task=Task("Sample task")
        self.assertFalse(task.completed)
        task.mark_completed()
        self.assertTrue(task.completed)

    def test_to_dict(self): #test case for to_dict method
        task=Task("Sample task", True)
        expected={
            "title": "Sample task",
            "completed": True
        }
        self.assertEqual(task.to_dict(), expected)

    def test_from_dict(self): #test case for from_dict method
        data={
            "title": "Sample task",
            "completed": False
        }
        task=Task.from_dict(data)
        self.assertEqual(task.title, "Sample task")
        self.assertFalse(task.completed)
    
if __name__ == "__main__":
    unittest.main()