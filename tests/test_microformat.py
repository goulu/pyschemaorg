from typing import List
import unittest
import requests
import extruct

from td.event import Event
from td.place import Place


class TestEvent(unittest.TestCase):
    def test_fetch_and_parse_schema_org_event_jsonld(self):
        """
        Tests fetching JSON-LD microformat data from https://schema.org/Event,
        extracting it with extruct, and producing "objects" (typed dictionaries)
        based on the Event TypedDict.
        """
        url = "https://schema.org/Event"
        # It's good practice to set a User-Agent. Some sites may block default Python/requests User-Agent.
        headers = {
            'User-Agent': 'SchemaOrgMicroformatTest/1.0 (Python; +http://example.com/my-test-suite)'
        }

        try:
            response = requests.get(url, headers=headers,
                                    timeout=10)  # 10-second timeout
            response.raise_for_status()  # Raise an HTTPError for bad responses (4XX or 5XX)
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch URL {url}: {e}")

        html_content = response.text

        # Extract microformat data, specifically targeting JSON-LD
        # Providing base_url helps resolve any relative URLs within the extracted data
        extracted_data = extruct.extract(
            html_content,
            base_url=url,
            syntaxes=['json-ld'],
            errors='ignore'  # 'log' or 'ignore' or 'strict'
        )

        json_ld_items = extracted_data.get('json-ld')

        assert json_ld_items is not None, "No JSON-LD data found on the page."
        assert isinstance(
            json_ld_items, list), "JSON-LD data should be a list of items."
        assert len(json_ld_items) > 0, "JSON-LD item list is empty."

        processed_event_objects: List[Event] = []

        for item in json_ld_items:
            if not isinstance(item, dict):
                # JSON-LD items are expected to be dictionaries
                continue

            item_type_field = item.get('@type')

            # Determine if the item is an Event
            # @type can be a string or a list of strings
            is_event = False
            if isinstance(item_type_field, str):
                if item_type_field == 'Event':
                    is_event = True
            elif isinstance(item_type_field, list):
                if 'Event' in item_type_field:
                    is_event = True

            if is_event:
                # This item is identified as an Event.
                # "Produce an object" by creating a dictionary that we intend to conform
                # to the Event TypedDict.
                # This involves mapping fields from the raw JSON-LD item to our TypedDict structure.
                # Missing fields in `item` will result in `None` due to `.get()`.
                # `total=False` in TypedDict definition allows for partially filled objects.

                event_obj: Event = {
                    'context': item.get('@context'),
                    'id': item.get('@id'),
                    'type': item_type_field,  # Keep original @type
                    'name': item.get('name'),
                    'description': item.get('description'),
                    'startDate': item.get('startDate'),
                    'endDate': item.get('endDate'),
                    # For nested structures like 'location', 'organizer', 'performer',
                    # further processing might be needed if they are complex objects
                    # and you want to cast them to their respective TypedDicts.
                    # For this example, we'll assign them directly if they exist.
                    # This could be a dict for Place, or string
                    'location': item.get('location'),
                    'organizer': item.get('organizer'),
                    'performer': item.get('performer'),
                }

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
