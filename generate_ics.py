#!/usr/bin/env python3
"""Generate ICS calendar file from EVENTS.md for NYC Family Summer 2026."""

from datetime import datetime
import re

EVENTS = [
    # June
    {"date": "2026-06-06", "time": "12:00", "end": "18:00", "summary": "Central Park SummerStage Family Day",
     "desc": "Free outdoor performances, concerts, and dance shows for all ages. Central Park, Rumsey Playfield.",
     "loc": "Rumsey Playfield, Central Park, New York, NY"},
    {"date": "2026-06-07", "time": "10:00", "end": "17:00", "summary": "Bronx Zoo Spring Celebration",
     "desc": "Family wildlife exploration day with animal feedings, keeper talks, and kids' activities.",
     "loc": "Bronx Zoo, 2300 Southern Blvd, Bronx, NY 10460"},
    {"date": "2026-06-13", "time": "10:00", "end": "16:00", "summary": "Brooklyn Botanic Garden Cherry Blossom Festival",
     "desc": "Spring blooms, family walks, hanami celebrations, food vendors.",
     "loc": "Brooklyn Botanic Garden, 990 Washington Ave, Brooklyn, NY 11225"},
    {"date": "2026-06-20", "time": "10:00", "end": "17:00", "summary": "Governor's Island Summer Season Opening",
     "desc": "Free family ferry, zip line, art installations, playground, food trucks.",
     "loc": "Governors Island, New York, NY"},
    {"date": "2026-06-21", "time": "14:00", "end": "18:00", "summary": "Coney Island Mermaid Parade",
     "desc": "Legendary artistic nautical parade with costumes, floats, and live music.",
     "loc": "Coney Island, Surf Ave, Brooklyn, NY 11224"},
    {"date": "2026-06-27", "time": "09:00", "end": "15:00", "summary": "Brooklyn Bridge Park Free Open Kayak",
     "desc": "Free guided kayaking sessions for all skill levels. Registration required.",
     "loc": "Brooklyn Bridge Park, Pier 2, Brooklyn, NY 11201"},
    {"date": "2026-06-28", "time": "19:30", "end": "22:00", "summary": "Lincoln Center Midsummer Night's Dream",
     "desc": "Free outdoor film screening on the David Geffen Hall lawn.",
     "loc": "Lincoln Center, 10 Lincoln Center Plaza, New York, NY 10023"},

    # July
    {"date": "2026-07-01", "time": "20:30", "end": "23:00", "summary": "Bryant Park Summer Film Festival Opening",
     "desc": "Free classic and family movie screenings on the Great Lawn.",
     "loc": "Bryant Park, 5th Ave & 42nd St, New York, NY 10018"},
    {"date": "2026-07-04", "time": "20:00", "end": "22:00", "summary": "Macy's Fourth of July Fireworks",
     "desc": "NYC's iconic fireworks display over the East River. Multiple viewing locations.",
     "loc": "East River, Manhattan, New York, NY"},
    {"date": "2026-07-05", "time": "10:00", "end": "16:00", "summary": "Prospect Park Zoo Family Day",
     "desc": "Special zookeeper talks, animal enrichment activities, crafts for kids.",
     "loc": "Prospect Park Zoo, 450 Flatbush Ave, Brooklyn, NY 11225"},
    {"date": "2026-07-11", "time": "14:00", "end": "17:00", "summary": "Harlem Meer Performance Festival",
     "desc": "Outdoor live music, dance, and theater in Central Park's Harlem Meer.",
     "loc": "Harlem Meer, Central Park, New York, NY"},
    {"date": "2026-07-18", "time": "09:00", "end": "17:00", "summary": "Brooklyn Bridge Park Free Open Swim",
     "desc": "Free supervised open water swimming in the East River.",
     "loc": "Brooklyn Bridge Park, Pier 2, Brooklyn, NY 11201"},
    {"date": "2026-07-19", "time": "10:00", "end": "17:00", "summary": "Queens County Fair — Harvest Festival",
     "desc": "Fair games, farm animals, live bluegrass, pie-eating contests.",
     "loc": "Queens County Farm Museum, 73-50 Little Neck Pkwy, Floral Park, NY 11004"},
    {"date": "2026-07-25", "time": "11:00", "end": "16:00", "summary": "NYC Pizza Challenge Festival",
     "desc": "Family food festival celebrating NYC pizza. Samples, kids' activities, pizza-making demos.",
     "loc": "Queens, NY"},
    {"date": "2026-07-26", "time": "10:00", "end": "16:00", "summary": "Bicycle Sunday — Car-Free Park Loop",
     "desc": "Central Park's loop road closed to cars for cyclists, rollerbladers, and families.",
     "loc": "Central Park Loop, New York, NY"},

    # August
    {"date": "2026-08-01", "time": "20:00", "end": "22:00", "summary": "Shakespeare in the Park — Much Ado About Nothing",
     "desc": "Free live theater. Distribution lottery required.",
     "loc": "Delacorte Theater, Central Park, New York, NY 10024"},
    {"date": "2026-08-02", "time": "11:00", "end": "16:00", "summary": "Red Hook Pool Family Swimming Day",
     "desc": "Family swimming day, water games, DJ, free swim gear giveaway.",
     "loc": "Red Hook Pool, 767 Earl St, Brooklyn, NY 11231"},
    {"date": "2026-08-08", "time": "11:00", "end": "16:00", "summary": "Summer on the Hudson — Riverside Park",
     "desc": "Outdoor circus, puppet shows, juggling, and family performances.",
     "loc": "Riverside Park, 79th–110th St, New York, NY"},
    {"date": "2026-08-09", "time": "09:30", "end": "16:30", "summary": "New York Aquarium Family Day",
     "desc": "Family discount day, behind-the-scenes tours, penguin feedings.",
     "loc": "New York Aquarium, Surf Ave & W 8th St, Brooklyn, NY 11224"},
    {"date": "2026-08-15", "time": "10:00", "end": "14:00", "summary": "Hudson River Park Family Sail",
     "desc": "Free community sail on the Hudson River aboard historic vessels. Registration required.",
     "loc": "Pier 84, Hudson River Park, Manhattan, NY"},
    {"date": "2026-08-16", "time": "19:00", "end": "22:00", "summary": "Flushing Meadows Corona Park Summer Concert",
     "desc": "Free outdoor concert series, family-friendly acts.",
     "loc": "Flushing Meadows Corona Park, Queens, NY"},
    {"date": "2026-08-22", "time": "17:00", "end": "23:00", "summary": "Brooklyn Museum Target First Saturday",
     "desc": "Free admission, live DJ, family art workshops, gallery tours.",
     "loc": "Brooklyn Museum, 200 Eastern Pkwy, Brooklyn, NY 11238"},
    {"date": "2026-08-23", "time": "12:00", "end": "18:00", "summary": "Governor's Island Claremont Fest",
     "desc": "Live music, food vendors, lawn games, ferry included.",
     "loc": "Governors Island, New York, NY"},
    {"date": "2026-08-29", "time": "11:00", "end": "15:00", "summary": "Central Park Zoo Summer Celebration",
     "desc": "Special animal celebrations, cake, face painting, keeper talks.",
     "loc": "Central Park Zoo, East 64th St, New York, NY 10065"},
    {"date": "2026-08-30", "time": "10:00", "end": "14:00", "summary": "Last Day of Summer — Beach Cleanup + BBQ",
     "desc": "Family beach cleanup followed by free BBQ.",
     "loc": "Rockaway Beach, Queens, NY"},
]


def format_ics_datetime(date_str, time_str):
    """Format datetime as ICS DTSTART/DTEND format: YYYYMMDDTHHMMSS."""
    dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    return dt.strftime("%Y%m%dT%H%M%S")


def generate_ics(events):
    """Generate ICS file content."""
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//NYC Family Summer 2026//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:NYC Family Summer 2026",
        "X-WR-TIMEZONE:America/New_York",
        "X-WR-CALDESC:Family activities calendar for New York City, Summer 2026",
        ""
    ]

    for i, ev in enumerate(events, 1):
        uid = f"nyc-family-{ev['date'].replace('-','')}-{i:02d}@pizzaman.local"
        dtstart = format_ics_datetime(ev['date'], ev['time'])
        dtend = format_ics_datetime(ev['date'], ev['end']) if 'end' in ev else None
        
        lines.extend([
            "BEGIN:VEVENT",
            f"UID:{uid}",
            f"DTSTAMP:{datetime.now().strftime('%Y%m%dT%H%M%S')}Z",
            f"DTSTART;TZID=America/New_York:{dtstart}",
        ])
        if dtend:
            lines.append(f"DTEND;TZID=America/New_York:{dtend}")
        lines.extend([
            f"SUMMARY:{ev['summary']}",
            f"DESCRIPTION:{ev['desc']}",
            f"LOCATION:{ev['loc']}",
            "END:VEVENT",
            ""
        ])

    lines.append("END:VCALENDAR")
    return "\r\n".join(lines)


if __name__ == "__main__":
    import sys
    output = generate_ics(EVENTS)
    outfile = "family-summer-2026.ics"
    with open(outfile, "w") as f:
        f.write(output)
    print(f"Written {len(EVENTS)} events to {outfile}")
