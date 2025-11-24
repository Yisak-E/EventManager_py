
class Event:
    def __init__(self, _id, title, description, start_time, end_time, location, emirate, category, priority, capacity, registered_attendees, tags):
        self.eventId = _id
        self.title = title
        self.description = description
        self.startTime = start_time
        self.endTime = end_time
        self.location = location
        self.emirate = emirate
        self.category = category
        self.priority = priority
        self.capacity = capacity
        self.registeredAttendees = registered_attendees
        self.tags = tags
        self.reviews = []
    def add_review(self, _review):
        self.reviews.append(_review)


    def get_id(self):
        return self.eventId

