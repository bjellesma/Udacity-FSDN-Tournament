# Udacity-FSDN-Tournament
## Table Of Contents
* [What Is This](#What-is-this "What is this")
* [Prerequisites](#Prerequisites "Prerequisites")
* [Quick Start](#Quick-Start "Quick Start")
* [Author](#Author "Author")

<a name="What-is-this"><h1>What Is This</h1></a>
  <p>This is my project for the Intro to Relational Databases course taught by Udacity. This course is part of the full stack developer nanodegree.</p>

<a name="Prerequisites"><h1>Prerequisites</h1></a>
* Download and install [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
* Download and install [Vagrant](https://www.vagrantup.com/downloads.html)
* (Windows only!) You need to use a shell to interact with the VM. I recomend using the git bash as part of the download of [git](https://git-scm.com/downloads)

<a name="Quick-Start"><h1>Quick Start</h1></a>
* Download or clone this repo
* `cd vagrant`
* `vagrant up`
* `vagrant ssh`
* Once you are ssh'd into the VM, navigate to the tournament directory with `cd /vagrant`
* create the PostgreSQL database from file. `psql -f tournament.sql`
* Finally, to run the file: `python tournament.py`

<a name="Author"><h1>Author</h1></a>
  <p>This project was authored by William Jellesma. </p>
