from typing import List
import unittest
import microformat
from factory import factory

import td


class TestEvent(unittest.TestCase):
    def test_songkick(self):
        data = microformat.read(
            "http://www.songkick.com/artists/236156-elysian-fields")
        data = data.get('json-ld')
        assert data is not None, "No JSON-LD data found on the page."
        for row in data:
            object = factory(row)
            assert object

    def test_event(self):
        """
        Tests fetching JSON-LD microformat data from https://schema.org/Event,
        extracting it with extruct, and producing "objects" (typed dictionaries)
        based on the Event TypedDict.
        """
        data = microformat.read("https://schema.org/Event")
        data = data.get('json-ld')

        assert data is not None, "No JSON-LD data found on the page."
        assert isinstance(
            data, list), "JSON-LD data should be a list of items."
        assert len(data) > 0, "JSON-LD item list is empty."

        processed_event_objects: List[td.Event] = []

        for item in data:
            event_obj = factory(item)

            # Perform basic assertions on the "produced object"
            # These checks validate that essential fields are present and have expected basic types.
            # Your actual TypedDicts from `src` will guide more specific assertions.
            assert event_obj.get('name') is not None, \
                f"Event object missing 'name'. Item: {item}"
            assert isinstance(event_obj['name'], str), \
                f"Event 'name' should be a string. Got: {type(event_obj['name'])}. Item: {item}"

            if event_obj.get('startDate') is not None:
                assert isinstance(event_obj['startDate'], str), \
                    f"Event 'startDate' should be a string. Got: {type(event_obj['startDate'])}. Item: {item}"

            # Example check for a nested object (location)
            if event_obj.get('location') is not None:
                # Location could be a simple string (name of place) or a Place object (dict)
                assert isinstance(event_obj['location'], (dict, str)), \
                    f"Event 'location' should be a dict (Place object) or string. Got: {type(event_obj['location'])}. Item: {item}"
                if isinstance(event_obj['location'], dict):
                    # If it's a dict, assume it's a Place object and check its type
                    # type: ignore
                    location_place: Place = event_obj['location']
                    assert location_place.get('@type') == 'Place' or 'Place' in location_place.get('@type', []), \
                        f"Location object @type is not Place. Location: {location_place}"

            processed_event_objects.append(event_obj)

        assert len(processed_event_objects) > 0, \
            "No objects of type 'Event' were found or processed from the JSON-LD data."

        # You can add more specific assertions here, e.g., checking content of known events
        # or properties of the first processed event.
        # print(f"Successfully processed {len(processed_event_objects)} Event objects.")
        # from pprint import pprint
        # if processed_event_objects:
        #     print("First processed Event object:")
        #     pprint(processed_event_objects[0])


if __name__ == '__main__':
    unittest.main()
