# NYC Family Summer 2026 Calendar

A practical data-formatting exercise: turn a hand-curated list of family activities into an `.ics` calendar file that a parent can import into Google Calendar, Apple Calendar, or Outlook.

## What this explores

- Collecting event data in a human-editable Markdown file
- Generating standards-based iCalendar output with Python
- Making a one-time research project portable across calendar apps
- Keeping source links visible so families can confirm details

The source list is in `EVENTS.md`; the generated file is `family-summer-2026.ics`.

## Regenerate the calendar

```bash
python3 generate_ics.py
```

Then import `family-summer-2026.ics` into your calendar app. Dates and venue details can change, so check the organizer before heading out.

## Why this is a learning exercise

The useful question here is not “can Python write an ICS file?” It is whether a simple data pipeline makes a seasonal plan easier to use than a long list of web pages.
