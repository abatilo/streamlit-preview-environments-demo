import streamlit as st

def year2008():
  st.markdown("""
## 2008 to 2010
The year is 2008 and I'm in middle school. I'm in between my 7th and 8th grade
years and my family had just moved from California all the way to Colorado. All
my friends were people who I met through playing
[MapleStory](https://maplestory.nexon.net/) and downloading scripts off of the
old CheatEngine forums to hack the game. I had no idea what I was doing but it
made the game play itself and I could level up faster and catch up to the
people who were playing with me.

For the next few years, I would learn how to write C# which was my first
programming language. I was an active member on an old hacking forum where I
would contribute libraries that would wrap common activities such as reading
and writing process memory and [simulating key presses and mouse
clicks](https://www.pinvoke.net/default.aspx/user32.postmessage). I'd sometimes
dabble in C++ which was what most of these tools were written in. I built
scriptable macro engines and bots for automating all kinds of things in
MapleStory.
""")

def year2011():
  st.markdown("""
## 2011
While I was in my junior year of high school, I competed in the [CyberPatriot III
Open
Division](https://www.uscyberpatriot.org/Pages/Competition/Season%20History/CyberPatriot-III.aspx).
Unfortunately, my team didn't do all too well but it all worked out for me when I was accepted for a [high school internship with Northrop Grumman](https://web.archive.org/web/20110719180601/https://aurorak12.org/2011/07/07/northrop-grumman-internships/).

The Aurora interns were placed on a project to analyze graphs of Twitter
relationships and we studied graph centrality calculations to understand what
the impact would be if highly connected versus lowly connected accounts were to
be compromised and try to distribute malware.
""")

def year2012():
  st.markdown("""
## 2012
In 2012, I came back to Northrop Grumman during the summer and worked on a
project where we were building a toy GUI that wrapped nmap and metasploit. We
used output from nmap to visualize a set of virtual machines that we had on our
local machines, and then used metasploit to create a reverse shell to the
compromised VM. At the end of 2012, I started my first year of college at the
[University of Colorado, Colorado Springs](https://www.uccs.edu/) as a computer
science major.
""")

def year2013():
  st.markdown("""
## 2013
In the summer of 2013, I came back to Northrop Grumman but this time as a
college intern where I got to work on a real project with full time developers
on it. The team was working on an unclassified project for aggregating and
visualizing data from multiple sensors that were equipped to various vehicles.

I integrated histogram and scatterplot visualization panels that would
dynamically look at available data properties and adjust the visualizations and
options accordingly.
""")

def year2014():
  st.markdown("""
## 2014
While I was on campus, I took a web developer job where I would help other
teachers with their Ingeniux web pages.

I also built a perl/HTML5 mobile friendly website that would graphically draw
your class schedule on a canvas. The "official" class schedule website rendered
your schedule in a `<table>` and so your classes always looked to start and end
on the hour which was never actually true.

At the same time, I had joined an on campus group doing research funded by the
National Science Foundation (NSF) where the computer science departments and
the psychology departments were studying user behavior on phishing websites. I
had configured apache to reverse proxy several popular websites such as Amazon
and eBay so that we could be the man in the middle watching the users and
asking questions like: "How do you know this is the real Amazon?"

For the summer of 2014, I returned to Northrop Grumman one last time where I
received an Top Secret SCI clearance and I started working on a project that
was preconfiguring server racks to be sent off to other classified
environments. I was working part time for the rest of the year into the summer
of 2015 and I was writing automated provisioning scripts for all of the
software and hardware that went into the racks.

I'm actually kind of happy knowing that I got to work in an actual data center
because I don't think many engineers of my generation will be able to say that.
              Let alone engineers of future generations.
""")

def year2015():
  st.markdown("""
## 2015
Summer of 2015, I worked part time (as needed) as a research assistant for a
PhD student working on research in coreference resolution. This was mostly
doing trivially small scripts for cleansing data for the PhD student.

At the same time, I started working part time for
[Josh.ai](https://www.josh.ai) where I was the 3rd technical hire. 5th overall
hire to the company. At this time, I was largely building the website and
customer portal which was largely a Flask website hosted on Heroku. This
website let customers interact with our natural language chat bot that would
control your smart home devices.
""")

def year2016():
  st.markdown("""
## 2016
As the team at [Josh.ai](https://www.josh.ai) continued to grow, I started
working on the Josh Android application so that customers could control their
smart homes from their phone. This Android app used a lot of bleeding edge
patterns at the time such as the Model-View-ViewModel, combined with RxJava and
WebSockets which meant that the phone application was constantly updated in
real time and gave customers a truly fluid user experience. Your wife could
have turned the lights on right as you were about to and you'd see the updates
happen within milliseconds.

I also had implemented UI tests with Espresso right as those tools were being
released, which meant we had a lot of confidence in the app.

My other role at the time was to provision the Mac Minis that we shipped with
our backend server on. The Mac Mini would sit in your home and communicate with
all of your devices locally. I would install certain software and packages on
the Mac Mini, and we had our own packaging that we would place the Mac Mini
into which I'd box up with packing peanuts and send to customers.
""")

def year2017():
  st.markdown("""
## 2017
I transitioned into writing more C++ for our local server which would talk to
your smart home devices. Eventually, the company decided that shipping Mac
Minis was not sustainable so I started working on making that
codebase cross platform compatible.

I left [Josh.ai](https://www.josh.ai) in the summer and joined
[FullContact](https://www.fullcontact.com/) where I migrated applications from
running on raw EC2 instances to running in Kubernetes. I maintained and fixed
bugs on the FullContact Card Reader API, and I designed and implemented our ML
based [job title classification
system](https://www.fullcontact.com/blog/2018/02/07/experimentation-leads-innovation-machine-learning-fullcontact/).
""")

def year2018():
  st.markdown("""
## 2018
Alas, FullContact was going through some financial troubles as data privacy
became more and more relevant. I left
[FullContact](https://www.fullcontact.com/) before a round of lay offs happened
to join [Conga](https://conga.com/). Conga was looking to build a green field
team to add machine learning based features to it's suite of document
management and generation products. I built and operated our AWS Elastic
Kubernetes Service clusters as well as built tooling and automation for our
data scientists to be able to experiment quickly.

Near the end of 2018, we had a demo application to demonstrate our APIs and it
was decided that we'd launch an entire product line directly to customers that
used these APIs. This launched in mid 2019 and became known as [Conga AI
Analyze](https://conga.com/workflow-automation-software/business-process-automation-insights/ai-contracts).
""")

def year2019():
  st.markdown("""
## 2019
After 1.5 years at Conga, I joined
[iStreamPlanet](https://www.istreamplanet.com/) where I've taken a much heavier
operations oriented software engineering role. In 2019, I moved some of our
applications off of
[Distelli](https://puppet.com/blog/welcome-distelli-to-puppet-family/) into
Kubernetes based applications. In some cases this included rewrites of
application functionality in order to fit a [12 factor](https://12factor.net/)
containerized model. At the same time, the improved disposability of the
applications allowed us to run on AWS Spot instances and reduced cost.

In order to facilitate the move, I developed combinations of terraform modules
and other infrastructure as code solutions, along with GitHub Action pipelines
that would allow teams to automatically provision EKS clusters tailored to the
rest of our observability stack within a matter of minutes. This started a long
journey to encourage teams to start moving to Kubernetes and to manage their
infrastructure in a declarative GitOps based way. These changes in process
increased trust, safety, and visibility into all of our infrastructure. Changes
could now be code reviewed and team members could provide input.
""")

def year2020():
  st.markdown("""
## 2020
Continuing my role in demystifying Kubernetes, I helped more teams migrate as
well as lead the engineering effort to load testing and tuning the autoscalers
for one of our products that is largely susceptible to very spikey traffic.

My role and day to day activities consists largely of helping teams understand
scalable design characteristics as well as reducing our spend in AWS. In total,
I've contributed in reducing our AWS spend by over $100,000 a month while our
actual usage continues to grow.

I develop platform tooling and automations to improve and optimize the
developer experience of all of the engineering members across the company.
""")

st.write("""
# Aaron Batilo's interactive history
""")

year = st.slider("What year would you like to read about?", min_value=2008, max_value=2020, value=2020)

years = {
  2008: [year2008],
  2009: [year2008],
  2010: [year2008],
  2011: [year2011],
  2012: [year2012],
  2013: [year2013],
  2014: [year2014],
  2015: [year2015],
  2016: [year2016],
  2017: [year2017],
  2018: [year2018],
  2019: [year2019],
  2020: [year2020],
}

for y in years[year]:
  y()
