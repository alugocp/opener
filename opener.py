from json import loads,dumps
from os.path import join,expanduser
from os import popen
import webbrowser

# options
def get_options():
    try: return loads(open(join(expanduser("~"),".local","etc","options.json"),"r").read())
    except IOError: print("options.json does not exist")
    except ValueError: print("Error while parsing options.json")
    return loads("{}")
def save_options(options):
    try:
        file=open(join(expanduser("~"),".local","etc","options.json"),"w")
        file.write(dumps(options))
        file.close()
    except ValueError: print("Error while JSONifying your options")
    except IOError: print("Cannot open options.json")
def ignore_hidden(options,value):
    options["ignore-hidden"]=value
def add_ignore(options,dirname):
    if not "ignore" in options: options["ignore"]=[]
    options["ignore"].append(dirname)

# filter sites
def filter_sites(options,sites):
    filtered=[]
    for site in sites:
        s=site.rstrip().split("/")
        if not (filter_hidden(options,s) or filter_ignore(options,s)): filtered.append(site.rstrip())
    return filtered
def filter_hidden(options,s):
    if "ignore-hidden" in options and options["ignore-hidden"]:
        for p in s:
            if len(p)>0 and p[0]==".": return True
def filter_ignore(options,s):
    if "ignore" in options:
        for ign in options["ignore"]:
            for a in range(len(s)-ign.count("/")):
                if ign=="/".join(s[a:a+ign.count("/")+1]): return True

# sites
def get_sites(options):
    sites=popen("find ~/Desktop -type f -name index.html").readlines()
    filtered=filter_sites(options,sites)
    return filtered
def print_sites(options):
    sites=get_sites(options)
    for s in sites: print(s[s.index("Desktop")+len("Desktop"):-len("/index.html")])
def open_site(location):
    webbrowser.open("file://"+location.replace(" ","%20"),new=2)
def open_project(options,proj):
    sites=get_sites(options)
    named=[]
    for s in sites:
        if proj in s: named.append(s)
    if len(named)==1: return open_site(named[0])
    for n in named:
        if proj+"/index.html" in n: return open_site(n)
    if len(named)==0: print("No matching projects")
    else: print("Ambiguous project selected")

__all__=["open_project"]
