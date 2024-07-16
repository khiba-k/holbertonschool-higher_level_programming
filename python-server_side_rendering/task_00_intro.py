#!/usr/bin/python3
import os
"""Program defines function that generates personalized invitation files
"""

def generate_invitations(template, attendees):
    """Function generates invitations

    Args:
        template (str)
        attendees (list)

    Returns:
        _type_: _description_
    """

    if not isinstance(template, str) or template is None: 
        print("Template is supposed to be a string")
        return
    
    if not isinstance(attendees, list) or attendees is None:
        print("Attendees is supposed to be a list")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    
    try:
        for x, attendee in enumerate(attendees, start=1):
            attendee_name = attendee.get("name") or "N/A"
            attendee_title = attendee.get("event_title") or "N/A"
            attendee_date = attendee.get("event_date") or "N/A"
            attendee_location = attendee.get("event_location") or "N/A"


            replace_name = "{name}"
            replace_title = "{event_title}"
            replace_date = "{event_date}"
            replace_location = "{event_location}"

            replace_text = template.replace(replace_name, attendee_name).replace(replace_title, attendee_title).replace(replace_date, attendee_date).replace(replace_location, attendee_location)
            current_file = f"output_{x}.txt"

            if os.path.exists(current_file):
                print(f"{current_file} already exists")
                continue
            
            with open(current_file, 'w') as output:
                output.write(replace_text)

    except Exception as e:
        print(f"{e} found")
        return


        


