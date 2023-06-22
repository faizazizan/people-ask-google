#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import time
import people_also_ask

# Define the URL for your request
url = 'https://www.google.com/search?q=app+developer&gl=my'

# Add a delay of 1 second before sending the request
time.sleep(1)

# Send the GET request to the URL
response = requests.get(url)

# Process the response as needed
# ...

# Use the people_also_ask library to get related questions
time.sleep(1)  # Add a delay before the next request
related_questions = people_also_ask.get_related_questions("app developer", 15)

# Process the related questions as needed
# ...


# In[ ]:




