from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle
import unittest


class FlaskTests(TestCase):

  def setUp(self):
      app.config['TESTING'] = True
      app.config['DEBUG'] = False
      self.app = app.test_client()
      
  def tearDown(self):
      pass
  
  def test_home_redirects(self):
      response = self.app.get('/', follow_redirects=True)
      self.assertEqual(response.status_code, 200)
      self.assertIn('Boggle Board', response.data.decode('utf-8'))  
      
  def test_display_board(self):
      self.app.get('/')
      response = self.app.get('/board')
      self.assertEqual(response.status_code, 200)
      self.assertIn('Boggle Board', response.data.decode('utf-8'))  
      
  def test_guess(self):
       with self.app.session_transaction() as sess:
           sess['board'] = [['T', 'E', 'S', 'T', 'S'], ['T', 'E', 'S', 'T', 'S'], ['T', 'E', 'S', 'T', 'S'], ['T', 'E', 'S', 'T', 'S'], ['T', 'E', 'S', 'T', 'S']]  
       response = self.app.post('/guess', json={'guess': 'tests'})
       self.assertEqual(response.status_code, 200)
       self.assertIn('"result": "ok"', response.data.decode('utf-8'))  
        
  def test_reshuffle(self):
       response = self.app.get('/reshuffle')
       self.assertEqual(response.status_code, 200)
       self.assertTrue('board' in response.json)
       
if __name__ == '__main__':
    unittest.main()       
       
            
      
          
      