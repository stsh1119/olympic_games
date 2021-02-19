import csv
from .variables_mapping import event_index


def form_unique_events_list():
    with open('athlete_events.csv') as athletes_file:
        reader = csv.reader(athletes_file)
        events_dict = {}
        for row in reader:
            if reader.line_num == 1:
                continue
            event = row[event_index]
            if '"' in event:
                event = event.replace('"', '\'')
            event_id = reader.line_num
            event_obj = {'event_name': event,
                         'id': event_id}
            events_dict[event] = event_obj
        return events_dict
