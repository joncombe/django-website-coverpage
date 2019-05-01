django-website-coverpage
====

Here in Thailand, it is customary for websites to show a cover page to celebrate national events, for example the King's birthday. This very simple app does just that.

### How it works:

- A middleware detects if a 'coverpage' cookie exists:
    - if it exists, nothing happens
    - if it doesn't exist, you are redirected to the URL of the coverpage

- A view:
    - shows the coverpage
    - sets the cookie so the page isn't shown again within this session

Note: this app uses a cookie, and not the user's session. This is because the session is refreshed when logging in or out, and showing the coverpage again wouldn't make any sense.

### Installation:
```
pip install django-website-coverpage
```

Add the following to your settings.py INSTALLED_APPS:
```
'websitecoverpage'
```

Add the following to your settings.py MIDDLEWARE:
```
'websitecoverpage/middleware.CoverPageMiddleware'
```

Add the following to your settings.py:
```
# The following are defaults, change them if you need to,
# i.e. if you are happy with the defaults, you don't need
# to add anything to your settings.py

# To disable the coverpage, set active = False
# To ignore certain URLs, use  'ignore_urls'
#    e.g. ['/a/', '/b/'] ignores all paths that startswith('/a/') and ('/b/')

WEBSITE_COVERPAGE = {
   'active': True,
   'cookiename': 'coverpage',
   'ignore_urls': [],
   'template': 'coverpage/coverpage.html',
   'url': '/coverpage/',
}
```

In your urls.py:
```
from websitecoverpage.views import CoverPageView
```

In your urls.py urlpatterns:
```
# change the path to be whatever you want but it needs to match
# what is in settings.py
path('coverpage/', CoverPageView.as_view()),
```

### Notes:
Is testing a pain because you need to keep clearing your cookies? Incognito mode is your friend.

### To-do:
- Make the cookie attributes (e.g. expiry) configurable. Today the cookie expires on browser close.
- Remember the URL the user originally went to, and redirect there after leaving the coverpage
- Add start and end datetimes that the coverpage should be active.

Note: I'll do the above when I need them but anyone is welcome to submit their PRs for the above or other suggestions.
