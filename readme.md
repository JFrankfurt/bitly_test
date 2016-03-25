# Bitly App Engineering Test
###### SUBMITTED BY: Jordan Frankfurt
###### DATE: March 23rd, 2016
#
#
## Summary:
This folder includes two scripts and a readme:
1. boatrace.py
2. warthogs.py
3. readme.md

#### How to tell if your boats are weirdly slow or not:
_boatrace.py_ : calculates the average time taken by a set of boats to finish a race. It's **really** simple and just returns a single integer.

```
Arguments:
    startTime : string
            Should follow format: "XX hours : xx minutes nM (n=A||P), DAY Z (0 < Z < 100)"
    finishTimes : list
            Should be a list of string times after the start date in the format given above.
```
```
Usage:    
    startTime = "08:00 AM, DAY 1"
    finishTimes = ["08:01 AM, DAY 1", "12:00 PM, DAY 65", "12:00 AM, DAY 34"]

    x = Race(startTime, finishTimes)
    x.avgMinutes()
```
#### How to wrastle a ~~warthog~~ blog:
_warthogs.py_ : Scrapes my blog (_Young Warthog_) and returns stats about the posts and bitlinks associated with them.
This is a python library for wrastling (young) warthogs. It scrapes the my blog for posts, creates bitlinks to them, and provides data on those bitlinks.
```
Arguments:
    accessToken : string
            Should be the user's access token from Bitly
    blogLinks : list
            optional: Should be a list of links to blog posts
    bitLinks : list
            optional: Should be a list of bitlinks to blog posts
    blogURL : string
            optional: Should be the url you are trying to scrape. Better to just leave this empty.
```
```
Usage:
    accessToken = 'asdfasdfasfasdfadfasd'
    blogLinks = [
        'http://jwfrankfurt.tumblr.com/post/131345868872/',
        'http://jwfrankfurt.tumblr.com/post/133066434925/',
        'http://jwfrankfurt.tumblr.com/post/139355789560/'
        ]
    bitLinks = [
        'http://bit.ly/21CrN6t',
        'http://bit.ly/1pv4Cit',
        'http://bit.ly/1Uy02wU'
        ]
    blogURL = "http://www.jwfrankfurt.tumblr.com"
    yw = YoungWarthog(accessToken, blogLinks, bitLinks, blogURL)
```
But that's more work than is actually necessary. If you *really* want to
make this work with on another blog, you can just provide your own link
data and ignore the getNewPosts method. No scraping necessary.
Since you only have to deal with one warthog, you can leave the
link wrangling to the scraper and just instantiate without any arguments:

```
yw = YoungWarthog()
```
Instantiating without any arguments (above) requires you to call the following method before proceeding.
```
Arguments:
    none
```
```
Usage:
    yw.getNewPosts()
```
.getNewPosts will scrape my blog and add any missing posts to the list provided, returning the new list.
```
Arguments:
    blogLinks : list
            optional: Should be a list of links to blog posts to be turned into bitlinks. If no argument is provided, shorten will look for links on self.blogLinks (provided by .getNewPosts). 
```
```
Usage:
    blogLinks = [
        'http://jwfrankfurt.tumblr.com/post/131345868872/',
        'http://jwfrankfurt.tumblr.com/post/133066434925/',
        'http://jwfrankfurt.tumblr.com/post/139355789560/'
        ]
    yw.shorten(blogLinks)
```
.shorten Returns bitlinks from those long urls provided and added
```
Arguments:
    unit : string
        "minute", "hour", "day", "week", "mweek", "month"; defaults to "day"
    units : integer
        optional: defaults to -1 to returna all units of time, otherwise any positive integer 
    timezone : string or int
        optional: defaults to America/New_York, -15 < tz < 15
    limit : integer
        optional: 1 - 1000; defaults = 100
```
```
Usage:
    unit : "day"
    units : -1
    timezone : 0
    limit : 100
    yw.clicks(unit, units, timezone, limit)
```
Returns a single aggregate digit of all link clicks
```
Arguments:
    created_before : integer
        optional: unix epoch
    created_after : integer
        optional: unix epoch
    limit : integer
        optional: limit to the number of results, 0 < limit <= 100; defaults to 50
    offset : integer
        optional: specifies the result at which to start
    private : string
        optional: "on", "off", or default "both"
```
```
Usage:
    created_before : 1451606400
    created_after : 746841600
    limit : 15
    private : "both"
    yw.linkHistory(created_before, created_after, limit, offset, private)
```

Returns a big 'ol object of info on all the links associated with the access token. I only use Bitly in conjunction with my blog, but this might be confusing for others.
