# Mar 20 2021 Meeting Notes

These are the notes from Ian and J.I.'s first planning meeting.


## Agreed-Upon Procedure

### STEP 0: Generate List of Locations (National)

We will create a .txt file named `locations.txt` where we will store all **_unique_**  sites that our web scraper ran into.

Notes:
* historic66.com is the only site we'll design a specific script for
* Other sites that may be worth scraping, at least on the python terminal, are:
    * travelok.com
    * theroute-66.com
    * roadtripusa.com
* All other sites are not worth our time. Check [inputs](#inputs) section below for our comments on the list of sites we were given.

### STEP 1: Get Location Information

Once we feel satisfied with the number of unique sites, for each location in `locations.txt`, we'll do a call to the Google API to extract as much information for that site as possible.

**_FIRST ORDER OF BUSINESS IS FIGURING WHAT CAN AND CANNOT BE RELIABLY PULLED FROM THE GOOGLE MAPS API_**

**Whoever takes care of this portion should take failed requests or false positives into account when designing the script. Check Sarah's first email for more details on precuations to take with the Google API.**

We will then save all these sites on a `location_info.json` file using the following JSON dictionary:

```python
{
    RoadTripStopTypeID, # (Event=1; Location=2)
    CategoryID, # USE A PLACEHOLDER DUMMY VALUE. This ain't our job.
    RoadTripStopName, 
    RoadTripStopDescription,
    RoadTripStopAddressLine1,
    RoadTripStopCity,
    RoadTripStopState,
    RoadTripStopZip,
    RoadTripStopLat,
    RoadTripStopLong,
    RoadTripStopEmail,
    RoadTripStopPhone,
    TicketBookingURL,
    Image, 
    EventDateTime, # this will be null if RoadTripStopTypeID = 2 (Location)
    RoadTripStopURL,
    PlaceID # from google places API
}
```

### STEP 2: Manually fill in the gaps

This section may or not be necessary.

### STEP 3: Deliver the deliverables

1. We will need to create methods to filter out Oklahoma locations and save these in a **_pipe-delimited .txt file_**
2. We will need to turn in a script that automates steps 0 and 1-- perhaps 2, probably not-- and that gives them some sense of control over step 3 as well (e.g. filtering by different states, for example)

### STEP 4: Stretch Goals

Once we've delivered the first batch of deliverables, we might also:

1. Take care of Hours of Operation for all locations.
2. Design a web scraper that searches for _events_ along Route 66.


### Unanswered Questions:

1. What can and cannot be extracted from the Google Maps API?
2. How will we deal, if at all, with mining events along Route 66?
    * May be best to make a separate events scraper. Will propose to project manager.
3. Do we even make a API request script at all? The last sentence in the project description email suggests that the Project manager wants a "Postman Collection" of our API calls ([Postman](https://postman.com) is an API Development and Request Management platform). So part of me wonders if it even makes sense to make a script if what she wants is a list of get requests that she can add to a Postman workflow of some sorts. I will have to get clarification on this.

### Google Places API

Ok, team, this is where I lost what we're being asked for. From the email:

_Using the data obtained in the scraper, call the google places api (basic call). The information we are hoping to obtain from this call is the `place_id` for each place on the list._

_There are some problems with using the address (for searching for places in the API). In particular, some types of place IDs may sometimes cause a `NOT_FOUND` response, or the API may return a different place ID in the response. These place ID types include:_
* _Street addresses that do not exist in Google Maps as precise addresses, but are inferred from a range of addresses._
* _Segments of a long route, where the request also specifies a city or locality._
* _Intersections._
* _Places with an address component of type subpremise._
 
_I was thinking that using the phone number MIGHT improve the results, so that is why I made that suggestion, but we can look to see how the results look and evaluate as a team.  There are lookup sites we can use to validate the information returned is correct.  We will visit this as part of the QA process._

**_Please create a Postman collection and share with me for the API call.  (We can discuss if you have not used Postman, it is an extremely valuable tool for APIs).**_ 
