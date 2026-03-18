# 2025 Group SH12 Project

## Name
Choose a self-explaining name for your project.

## Description
A prototype of a system to be used by Police to reduce the time required for officers to create intelligence reports and help visualise the information in said reports for the intelligence officers who use them. It creates intelligence reports based on inputted text files and extracts entities (of the types person, vehicle, telecom, location, or organisation) that are present within the text file. It also identifies potential links between the entities. On another page, a graph can be viewed containing all linked entities. This graph can be filtered in the following ways: By entitiyID (shows all entities in the same tree as the entity, ie all entities directly or indirectly connected to the entity), by reportID (shows all entities mentioned in the report), by name (shows all entities which contain the entered phrase as a wildcard), by type (as described above). There is a toggle that decides whether only the sidebar or the sidebar and graph will be filtered. Clicking on a node opens a page with all the information associated to it.

## Status
This project is a prototype developed as a student project. Future developement is unlikely.

## Installation
Download the files in the repository and install (optionally in a virtual environment) python 3.12.10 and the requirements listed in requirements.txt (pip install -r requirements.txt). To create the database used by the server, run "python manage.py migrate". To create a superuser/admin account run "python manage.py createsuperuser" then follow the prompts (email prompt is optional).

## Deployment
Download all files in the repository, install the requirements listed in requirements.txt into your virtual environment, and follow the standard django deployment steps
https://docs.djangoproject.com/en/4.0/howto/deployment/

## Usage
Main purpose is to automatically extract information on people, locations, vehicles, organisations, and telecoms from text files, automatically generate links between the entities extracted based on the content of the text file (with the option to manually override these), then visualise these links in the form of a graph. Filters can be used to limit the info listed in the sidebar and the graph, for example limiting the graph to entities in the same tree as another entity.

## Support
No support is available for this prototype.

## Contributing
You are free to create a fork of this project. To run the existing test, run "python manage.py test". To run a test/developement server run "python manage.py runserver"

## Authors and acknowledgment
Owners/Contributors: Archie Henderson, Azra Miray Atik, Rei Mito, Connor Mackenzie, Jiayue Wang, Oleksandr Dykyi

## License
Copyright 2025 Archie Henderson, Azra Miray Atik, Jiayue Wang, Rei Mito, Connor Mackenzie, Oleksander Dykyi
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.