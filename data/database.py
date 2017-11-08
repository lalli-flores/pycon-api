import os.path
import sqlite3

class micDB:
  '''Creates a database to store microphone's scrapped data.'''

  def __init__(self, name='pycon.db'):
    self.connection = sqlite3.connect(name)
    self.cursor = self.connection.cursor()

    print(os.path.isfile(name))
    if not os.path.isfile(name):
      pirnt('here')
      self._cleanup()

      self.cursor.execute('CREATE TABLE speakers(id, name, bio)')
      self.cursor.execute('CREATE TABLE talks(id, title, timeslot)')
      self.cursor.execute('CREATE TABLE events(id, name, location, start_date, end_date)')

      self.cursor.execute('CREATE TABLE talk_speakers(talkID, speakerID)')
      self.cursor.execute('CREATE TABLE event_talks(eventID, talkID)')

  def __enter__(self):
    return self

  def __exit__(self, type, value, traceback):
    self.cursor.close()
    self.connection.close()

  def _cleanup(self):
    '''Wipes database if it has existing data.'''

    self.cursor.execute('DROP TABLE IF EXISTS speakers')
    self.cursor.execute('DROP TABLE IF EXISTS talks')
    self.cursor.execute('DROP TABLE IF EXISTS events')

    self.cursor.execute('DROP TABLE IF EXISTS talk_speakers')
    self.cursor.execute('DROP TABLE IF EXISTS event_talks')

  def insertTalk(self, talk):
    '''Inserts the given talk into the database.'''

    self.cursor.execute('INSERT INTO talks values(:id, :title, :timeslot)', talk.__dict__)

  def getSpeakers(self):
    '''Returns all speakers found in the database.'''

    self.cursor.execute('SELECT * FROM speakers')
    return self.cursor.fetchall()


  def getTalks(self):
    '''Returns all talks found in the database.'''

    self.cursor.execute('SELECT * FROM talks')
    return self.cursor.fetchall()


  def test(self):
    self.cursor.execute('SELECT * FROM talks')
    print(self.cursor.fetchone())
