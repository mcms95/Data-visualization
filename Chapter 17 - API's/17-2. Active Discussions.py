# Ex -> Using the data from hn_submissions.py, make a bar chart showing the most active discussions currently happening on Hacker News. The height of each bar should correspond to the number of comments each submission has. The label for each bar should include the submission’s title and act as a link to the discussion page for that submission. If you get a KeyError when creating a chart, use a try-except block to skip over the promotional posts.

import requests
from operator import itemgetter
import json
import plotly.express as px

# Make API call and store the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code :{r.status_code}")

# Explore Data
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    # Make a new API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id : {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary dor each article
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants']
    }

    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

print(submission_dicts)
titles, hn_links, comments = [], [], []
for submission_dict in submission_dicts:
    titles.append(submission_dict['title'])
    link = f"<a href='{'hn_link'}'>{submission_dict['title']}</a>"
    hn_links.append(link)
    comments.append(submission_dict['comments'])

title = "Most Commented articles on Hacker News"
labels = {'x': 'Repository', 'y': 'Comments'}
fig = px.bar(x=hn_links, y=comments, title=title,
             labels=labels, hover_name=titles)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()
