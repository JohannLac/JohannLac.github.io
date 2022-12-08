
import pandas as pd
import os

talks = pd.read_csv("talks.tsv", sep="\t", header=0)
talks

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    if type(text) is str:
        return "".join(html_escape_table.get(c,c) for c in text)
    else:
        return "False"

loc_dict = {}


md = "---\n\
layout: archive\n\
title: \"Talks\"\n\
permalink: /talks/\n\
author_profile: true\n\
redirect_from:\n\
  - /talks\n\
---\n\
\n\
{% include base_path %}"



for row, item in talks.iterrows():
    
    md_filename = str(item.date) + "-" + item.url_slug + ".md"
    html_filename = str(item.date) + "-" + item.url_slug 
    year = item.date[:4]
    
    md += "\n" + item.title + "\n"
    md += "------\n"
    
    
    if len(str(item.date)) > 3:
        md += "<span style=\"font-size:.8em;\">" + str(item.date) + "</span>  \n"
    if len(str(item.venue)) > 3:
        md += "<span style=\"font-size:.8em;\">*" + str(item.venue) + "*</span>"
    if len(str(item.location)) > 3:
        md += "<span style=\"font-size:.8em;\"> - " + str(item.location) + "</span>  \n"

    if len(str(item.description)) > 3:
        md += '\n\n<font size=\"4\">' + str(item.description) + ' </font>\n'
        
    md_filename = os.path.basename(md_filename)
    
with open("../_pages/talks.md", 'w') as f:
    f.write(md)

