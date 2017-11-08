import requests
from bs4 import BeautifulSoup
from .models import Talk, Speaker

pyconURL = 'http://us.pycon.org'


def isPresentationLink(tag):
  '''Verifies that the tag is a link to a presentation.'''

  href = tag.get('href')
  return href is not None and 'presentation' in href


def getSpeaker(uri):
  '''Returns the PyCon speaker of the given URI.'''

  data = requests.get('{}/{}'.format(pyconURL, uri))
  soup = BeautifulSoup(data.text, 'html.parser')
  contents = soup.select('div.span6', limit=1)[0]

  speakerID = uri.split('/')[-2]
  name = contents.select('h1')[0].text
  bio = contents.select('div#bio')[0].text

  return Speaker(speakerID, name, bio)


def getPresentation(uri):
  '''Returns the PyCon talk of the give URI.'''

  data = requests.get('{}/{}'.format(pyconURL, uri))
  soup = BeautifulSoup(data.text, 'html.parser')
  contents = soup.select('div.box-content')[0]
  timeslot, speakerLinks = contents.select('h4')

  talkID = uri.split('/')[-2]
  title = contents.select('h2')[0].text
  timeslot = timeslot.text.replace(' ', '').replace('\n', ' ')
  speakers = [getSpeaker(a.get('href')) for a in speakerLinks.find_all('a')]

  return Talk(talkID, title, timeslot, speakers)


def getPresentationURLs(year):
  '''Returns an iterator of the links for the PyCon presentations of the given year.'''

  data = requests.get('{}/{}/schedule'.format(pyconURL, year))
  soup = BeautifulSoup(data.text, 'html.parser')

  for a in soup.find_all(isPresentationLink):
    yield a.get('href')


def pyconPresentations(year):
  '''Returns an iterator for the PyCon presentations of the given year.'''

  for presentation in getPresentationURLs(year):
    yield getPresentation(presentation)
