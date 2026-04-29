# NYC Family Summer 2026 Calendar

Curated family activity events for New York City, Summer 2026.

## Quick Start

1. **Download the ICS file** — `family-summer-2026.ics`
2. **Import into any calendar** — Google Calendar, Apple Calendar, Outlook
3. Done! All 25 events will load with times, locations, and descriptions.

## What's Included

- **25 hand-curated events** across June, July, and August 2026
- Mix of free and paid events
- Age-appropriate for families
- Location, time, and description for each event
- Recurring weekly events (kayak sessions, car-free Sundays, etc.)

## File Structure

```
nyc-family-summer-2026/
├── EVENTS.md          # Raw event listings
├── generate_ics.py    # Script to regenerate ICS from EVENTS.md
├── family-summer-2026.ics   # Calendar file ready to import
└── README.md
```

## Regenerate the Calendar

If you add new events to EVENTS.md:

```bash
cd ~/nyc-family-summer-2026
python3 generate_ics.py
```

## Import Instructions

### Google Calendar
1. Go to [calendar.google.com](https://calendar.google.com)
2. Settings → Import calendar → Upload `family-summer-2026.ics`
3. Or: Add by URL (if hosted)

### Apple Calendar (iCal)
1. File → Import → Select `family-summer-2026.ics`
2. Choose which calendar to add to

### Outlook
1. File → Open Calendar → From File → Select ICS

## Event Sources

- nycgovparks.org — NYC Parks official events
- publictheater.org — Shakespeare in the Park
- coneyisland.com — Coney Island events
- bronxzoo.com — Bronx Zoo
- prospectparkzoo.com — Prospect Park Zoo
- govisland.com — Governors Island
- bryantpark.org — Bryant Park events
- queensfarm.org — Queens County Farm
