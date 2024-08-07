
Below is the outline for the open source, self service security testing tool SaaSploit which I am currently developing on GitHub.
The project is still in the early stages of development, and I am currently working on fleshing out my ideas in a more solid way.

I am looking for feedback on the outline, and I am open to any suggestions or ideas that you may have.

Please read the below outline and provide feedback on what you think should be added, removed, or changed.


---

# SaaSploit Outline
---



# Introduction

I have noticed the not so new trend of individuals online who are interested in pursuing a career in B2B SaaS, or really just doing SaaS in general.

They just churn out their ideas and honestly that’s cool but the problem comes from the fact that security is almost always an afterthought if it is even thought about at all. 

A large portion of these SaaS companies base their products on systems like Google Firebase or now more often is Supabase. Regardless of which one they use, because there are plenty more, the use of these “backend as a service” databases like Supabase and Firebase are regularly misconfigured and open the company up to a wide variety of vulnerabilities 


My goal is to create something similar to wpscan, nuclei, or msfconsole, which we will call SaaSploit



The point of this project is to design a CLI tool in Python which when provided with either a target or a target list, is able to preform a variety of tests which are used to reliably detect various vulnerabilities and misconfigurations in a variety of popular services, systems and applications used by SaaS companies. 

This includes but is not limited to:

- backend as a service providers
- Auth & SSO providers
- CMS tools
- Data storage and analytics platforms 
- Customer engagement tools 
- Email systems and services
- etc etc etc

I think a good way to think of this, is to look at the website Product Hunt, and create a security assessment and vulnerability analysis tool that focuses on popular dependencies for services listed on Product Hunt. This may give you a better idea of the type of application that we are looking to target with this project. 

The ultimate goal of this project is to create a tool which can be used by SaaS developers to make sure they are at least following… not worst practices. I genuinely think with how easy it is to make an app or service these days, there absolutely needs to be quick and easy security assessment tools that are designed primarily for assessing the security posture of applications built on these tech stacks designed for rapid development and deployment. 

It is way to easy to learn how to make an app that looks good, while skipping over learning all the best practices and security concerns. This leads to the absolute fucking state of cybersecurity 

My plan for how I intend to develop this CLI tool is to study the Go based CLI applications developed by project discovery and structure my project in a similar manner 

Beyond the project structure I intend to use the same libraries as these project discovery tools and generally aim to use them as a standard for my project development as the organization is successful and produces quality code 


## UI/UX


this thing is SIMPLE. Like I am going to make it a script that accepts command line arguments as input and so I kinda want to make the output look pretty since I don’t really think it would take much effort to go a long way. 

We will be using various libraries by the GitHub organization known as Textualize, which provides several tools for creating beautiful CLI outputs

I kinda want to make something like Nmap in terms of user experience. No REPL or shell or anything just a script with arguments as input, but I want the output to be rendered beautifully in a modern way using whatever library we pick. 

Perhaps it would be rendered in more of a dashboard that, instead of filling up the screen over time with updates/status reports for the script, it could draw a dashboard and display the stats of the script, and the general output 





## assessment


This is where the actual thinking and brain power comes in, because we are going to have to actually begin thinking about… well a variety of things. We actually need to research every service we intend to provide testing for. That, at the moment includes only 
- Firebase
- Supabase
But I plan to add, not only more Database as a service, backend as a service providers, but other SaaS tooling

We will be focusing primarily on web based SaaS services which operate over HTTP. 

- how services are identified to be in use
- What each service needs to be used properly 
- What are indicators that a service is being used improperly and how can we can detect these indicators regularly 
- What might be some variations of the observed indicators across the same type of problem/misconfiguration. Like 2 people using Firebase may make the same access control configuration, but their use of Firebase within the overall application results in an indicator presenting itself either differently or not at all. We need to reference the documentation to best understand indicators or issues and how they manifest themselves within these applications 

So the overall design of this system should be based on modules. I am a python programmer at heart, so my instinct is to start by analyzing the potential vulnerabilities, misconfigurations, and general mistakes & problems within a specific backend as a service provider we intend to have tests/assessments for. Based on what we come up with for that provider, we would classify the different types of problems by creating python classes which contain functions that handle the testing related to that type of problem 



This also makes me realize we of course need a way to identify whether or not specific applications are or are not in use. There is no sense in preforming the Supabase focused assessments/tests on a service which was not built with Supabase. 



I believe that perhaps the best solution is to preform a detailed assessment & general recon on the target provided. Ideally this target would have a working service on port 80/443 or whatever port the web service is running on

From there if the server is running the program should recursively crawl the web content available on the server and that should serve as the entry point to the application 

The CLI tool should seek to identify any parts of the web application that are of interest and make note of them. This could be 
- endpoints that accept POST requests 
- HTML Forms
- JavaScript files?
- Anything that maybe should not be exposed, like sensitive documents 
- Internal resource / page URLs 
- External URLs 
- emails
- endpoints that accept GET requests
- etc

As this is going on, it should be displaying progress in the TUI dashboard 
I imagine the dashboard as a single still frame, where many “components” or “widgets” are rendered within this larger frame, making up a reactive dashboard that displays real time progress updates using the tools provided by textualize 

This way it is not an ever growing wall of text

All output should be written to a file or directory rather than being in memory and taking up valuable space on the dashboard 

Rather I seek to create “reports” for a variety of different members of an organization or company to understand their security posture, in terms they can easily understand based on their personal experience and ability. 
The goal is to be able to provide in depth technical analysis for security professionals as well as dumbed down cave man speak for the C suite fellas. Just jokes. 

To do this, we will be using Ollama & a variety of LLMs to create a standardized templates for how reports should be structured.
By the way these reports will be generated based on the findings from the analysis done in the recon phase. Basically we will use this data we find during the recon phase to fill out the templates for the reports. 

These templates will basically be markdown documents which outline a standard structure for the reports. These templates will be created using  Jinja2 templating engine. 
This is because markdown is a highly versatile format that can be easily converted into another format that the client wants. Some people may like markdown, some may like PDF or DocX 

And Jinja2 is just what I am familiar with and I believe it will do the job nicely 

In terms of what we are analyzing, each business may have completely different infrastructure and attack surface. For this reason we want to divide this overall penetration test style assessment of SaaS businesses in a “stages”, kinda like order of operations 

We will essentially work by providing a scope for the operation in the form of a CSV file that outlines the infrastructure and what type of infrastructure each item in the scope is 
We will use hackerone formatting and naming conventions for this scope CSV 



# Recon

The recon phase is where we will be doing the majority of the work.

We will take the scope that has been provided, as well as the "anti-scope".

This is where we will be identifying the services in use by the target, and the potential vulnerabilities and misconfigurations that are present in the services in use.

This will be done by crawling the web application and identifying the various parts of the application that are of interest. This could be endpoints that accept POST requests, HTML Forms, JavaScript files, anything that maybe should not be exposed, like sensitive documents, internal resource / page URLs, external URLs, etc.

In addition to the scope, we will also want to be able to provide a list of services that are not in use by the target. This will allow us to identify potential services in use by the target that were not identified in the recon phase.

## Scope Analysis

**Web Crawling**:
will be done with [Crawlee Python](https://github.com/apify/crawlee-python)
Crawlee—A web scraping and browser automation library for Python to build reliable crawlers. Extract data for AI, LLMs, RAG, or GPTs. Download HTML, PDF, JPG, PNG, and other files from websites. Works with BeautifulSoup, Playwright, and raw HTTP. Both headful and headless mode. With proxy rotation.https://github.com/apify/crawlee-python


**Port scanning**:
This will be done with [RustScan]() in a container


**Email Scraping**:
I am thinking about integrating a feature that

1. scrapes emails from the website(s) provided in the scope
2. uses [holehe](https://github.com/megadose/holehe) & other tools to analyze the emails to see where they are registered and what services they are registered with
3. use the results to identify potential services in use by the individuals relevant to the organization, this can be used to craft spear phishing campaigns or to identify potential services in use by the organization that were not identified in the recon phase.
4. This will be done in a separate thread from the main program, and will be done in a way that is not intrusive to the main program.




---

Please note that this is a work in progress.

Please analyze the outline and provide feedback on what you think should be added, removed, or changed.