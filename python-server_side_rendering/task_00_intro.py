def generate_invitations (template, attendees):
    if not isinstance(template, str):
        print("Error: Invalid input type for template. Expected a string.")
        return
    if not isinstance(attendees, list) or not all (isinstance(a, dict) for a in attendees):
        print("Error: Invalid input type for attendees. Expected a list of dictionnaries.")
        return
    
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return
    
    for i, person in enumerate(attendees, start=1):
        filled = template.format(
            name = person.get("name", "N/A") or "N/A",
            event_title=person.get("event_title", "N/A") or "N/A",
            event_date=person.get("event_date", "N/A") or "N/A",
            event_location=person.get("event_location", "N/A") or "N/A"
        )

        output_filename = f"output_{i}.txt"
        try:
            with open(output_filename, "w") as file:
                file.write(filled)
            print(f"Generated {output_filename}")
        except Exception as e:
            print(f"Error writing to {output_filename}: {e}")
