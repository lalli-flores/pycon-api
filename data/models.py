class Speaker:
  '''Speaker that has a talk.'''

  def __init__(self, speakerID, name, bio=''):
    self.id = speakerID
    self.name = name
    self.bio = bio

  def __repr__(self):
    return '{}(id={}, name={})'.format(self.__class__.__name__,
                                       self.id,
                                       self.name)


class Talk:
  '''Represents a presentation, tutorial or workshop for an event.'''

  def __init__(self, talkID, title, timeslot, speakers=[]):
    self.id = talkID
    self.title = title
    self.timeslot = timeslot
    self.speakers = speakers

  def __repr__(self):
    speakers = ', '.join(speaker.name for speaker in self.speakers)

    return '{}(id={}, title=\'{}\', speakers=[{}])'.format(self.__class__.__name__,
                                                        self.id,
                                                        self.title,
                                                        speakers)


class Event:
  '''Represents an event that has talks of semi-related topics.'''

  def __init__(self, name, location, start, end, talks=[]):
    self.name = name
    self.location = location
    self.start = start
    self.end = end
    self.talks = talks

  def __repr__(self):
    return '{}(name={}, location={}, dates={}-{})'.format(self.__class__.__name__,
                                                          self.location,
                                                          self.start,
                                                          self.end)
