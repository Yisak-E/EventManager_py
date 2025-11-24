import json
from model.review import Review
from model.event import Event
from model.event_repo import EventRepository




class Data:
    def __init__(self,filename):
        self.filename = filename
        self.data = []


    def read_data(self):
           try:
               with open(self.filename, 'r') as f:
                   file = json.load(f)
                   self.data = file["events"]

           except FileNotFoundError as e:
               print(e)
           except Exception as e:
               print(e)


    def load_data(self):
        _repo = EventRepository()
        for i,  _event in enumerate(self.data):
            event_id = _event["eventId"]
            event_title = _event["name"]
            start_time = _event["startDateTime"]
            end_time = _event["endDateTime"]
            location = _event["venue"]
            emirate = _event["city"]
            category = _event["category"]
            priority = _event["priority"]
            capacity = _event["capacity"]
            registered_attendees = _event["registered"]
            description = _event["description"]
            tags = _event["tags"]
            reviews_total = _event["reviews"]
            event_data = Event(event_id, event_title, description, start_time, end_time, location, emirate, category, priority, capacity, registered_attendees, tags)
            _repo.add_event(event_data)
            for _review in reviews_total:
                rev_id = _review["reviewId"]
                rating = _review["rating"]
                comment = _review["comment"]
                sentiment = _review["sentiment"]
                date = _review["date"]
                review_data = Review(rev_id, rating, comment, sentiment, date)
                _repo.get_event(event_id).add_review(review_data)

        return _repo



data = Data("../datas/events.json")
data.read_data()
repo = data.load_data()

event = repo.get_event("E-001")

if event:
    print(f" Event Id: {event.get_id()}")
    print(event.title)
    print(f"Number of reviews: {len(event.reviews)}")

    for review in event.reviews:
        print(f" Review: {review.id}")
        print(f" Rating: {review.rating}")
        print(f" Comment: {review.comment}")
        print(f" Sentiment: {review.sentiment}")

        print("\n \t")
