# Route 66 Oklahoma Locations Sraper

Repo for web scraping for AAA Road Trip app

This README describes the project scope.

Read [planning_meeting_notes.md](./planning_meeting_notes.md) for the procedure we've chosen to take.

Everything below is from the client, lightly edited by J.I. for clarity:

# Sandbox for development
This is a Holerton docker sandbox, using cuz it's convenient - high five!
Chromium and chrome-driver already isntalled - so can use selenium to scrape dynamic sites

Host: d27fce6f.hbtn-cod.io

User: 559bdd8f66a4

Password: 23143532c756db6b868f



## Project Scope

**We have a client who needs to gather travel and event stops along Route 66 to be used in a mobile app.** We have a list of websites the client would like us to use to populate this data in our database to feed the application. This project has 2 separate pieces for gathering data:

* Data Scraping of Websites
    * The subsequent segments explain this portion in detail.
* Data enhancement using Google Places API
    * See our notes about this in [planning_meeting_notes.md](./planning_meeting_notes/#google-api-stuff)

## Sites to Scrape

_Editor's Note: We (J.I. and Ian) decided it's probably best to only scrape historic66.com and then manually check these other sites for additional locations. We may perhaps lightly scrape some of the more interesting sites here, but most are just repeating themselves / have no standard format that make them worth scraping._

| Site | Notes from J.I. and Ian's first meeting |
|-|-|
| https://www.historic66.com | **Now this one has stuff worth scraping!** It has a database of places of interest divided by state. Not all of them are winners-- idk if AAA wants to hype up a pedestrian underpass but we'll clean that up later. |
| https://www.travelok.com/article_page/oklahomas-top-attractions-along-route-66 | For this first site, we can follow the links for each attraction. This takes us to another travelok.com page with more information that we can pull. |
| https://www.theroute-66.com/state.html | May be best to first inspect the route architecture for the entire theroute-66.com website and then we can pull the contents of header tags from routes that are relevant. |
| https://www.nps.gov/subjects/travelroute66/index.htm | _This site contains no valuable information. It's "Sites of Route 66" link is broken_ |
| https://www.roadtripusa.com/route-66/ | We could inspect all routes that start with https://www.roadtripusa.com/route-66/* and extract the title name out of these and then add to the list of attractions. |
| https://roadtrippers.com/the-ultimate-guide-route-66/ | It's essentially a blog with a list of top attractions followed by a list of attractions by state. May be worth scraping, maybe not. |
| https://www.legendsofamerica.com/route-66/ | _This site contains articles with historical information for sites, towns, and historical events. Truly not worth scraping for current attractions. We'll probably skip._ |
| https://www.national66.org/history-of-route-66/ | _Definitely not worth our time_ |
| https://www.pettitts.co.uk/blog/things-to-see-route-66 | _This is a listicle blog and only a few items are in Oklahoma. Not worth our time._  |
| https://oklahomawonders.com/things-to-see-on-route-66-bucket-list/ | _Not worth our time_ |
| https://www.travelandleisure.com/trip-ideas/road-trips/route-66-attractions | _Also not worth our time_ |

 
## Data Scraping Details

The first version of the application will be for Oklahoma only. So, the script should filter out result sets if other states are returned.
* Note: **_(Future versions will be rolled out over time to include additional states so ideally the mechanism we provide to them can have this filter modified as needed)._**
    * _J.I.'s note: Oh, we could totally do this._

Here is the data they want captured from the websites.

* **Road Trip Stop Spreadsheet**
    * A spreadsheet with basic data for either an Event or a Location. The columns are the following:
        * RoadTripStopTypeID. _(Event=1; Location=2)_
        * CategoryID _(Put a placeholder here. Someone will assign these manually later)_
        * RoadTripStopName
        * RoadTripStopDescription
        * RoadTripStopAddressLine1
        * RoadTripStopCity
        * RoadTripStopState
        * RoadTripStopZip
        * RoadTripStopLat
        * RoadTripStopLong
        * RoadTripStopEmail
        * RoadTripStopPhone
        * TicketBookingURL
        * Image - this is the main image that will display for the location
        * EventDateTime - this will be null for entries with RoadTripStopTypeID=2(Location)
        * RoadTripStopURL
        * PlaceID - **from Google Places API** _(read more about this [here](#google-places-api))

As a stretch goal, once we have all the previous data, we may be asked to also take care of hours of operation, in the following format:

* **Hours of Operation:**
    * Captured in Military time (HH:MM) and only required for a Location. 
    * Associated to RoadTripStopName field.
    * Fields:
        * RoadTripStopName
        * Sun Open Time
        * Sun Close Time
        * Mon Open Time
        * Mon Close Time
        * Tue Open Time
        * Tue Close Time
        * Wed Open Time
        * Wed Close Time
        * Thu Open Time
        * Thu Close Time
        * Fri Open Time
        * Fri Close Time
        * Sat Open Time
        * Sat Close Time


## Deliverables:

We need to confirm these with the project manager. The e-mail says we need to give the info back in "separate files" but we don't understand what that is referring to. For now, this is our understanding of the deliverables:

* `road_trip_stops.txt`
    * One "Road Trip Stop" per line, field values are pipe-separated (`|`)
    * **Please account for special characters in the file using text indicators**

* `scrape_66.py`
    * This is the script we use to scrape the sites and generate the .txt file.
    * Also include instructions on how to use.

* Additional deliverables may be added once we complete the first set of deliverables. See [planning_meeting_notes.md](./planning_meeting_notes.md)

##  Deadline: April 16th
