# Analysis Project

Project of Full Stack Web Development Udacity Nanodegree

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
- Vagrant 1.8.5. Follow the steps from here: https://howtoprogram.xyz/2016/07/23/install-vagrant-ubuntu-16-04/
- Virtualbox 5.0. Download and install from here: https://www.virtualbox.org/wiki/Download_Old_Builds_5_0

```

### Installing

1. In command line write **git clone** and the url of the project.
2. Go to the main folder where is the Vagrantfile and write **vagrant up** to start the VM.
3. Once the machine is setted, write **vagrant ssh** and you will be in the **vagrant@vagrant:**


### Configure Database

First, unzip the file newsdatal.zip.

To load the data, **cd /vagrant/Analysis\ Project/** and use the command **psql -d news -f newsdata.sql**.

Here's what this command does:

* ***psql:*** the PostgreSQL command line program
* ***-d news:*** connect to the database named news which has been set up for you
* ***-f newsdata.sql:*** run the SQL statements in the file newsdata.sql

Explore to your database using **psql -d news** and explore the tables using the **\dt** and **\d table** commands and select statements.

Here's what this command does:

* ***\dt:*** display tables — lists the tables that are available in the database.
* ***\d table:*** (replace table with the name of a table) — shows the database schema for that particular table.

The database includes three tables:

* The *authors* table includes information about the authors of articles.
* The *articles* table includes the articles themselves.
* The *log* table includes one entry for each time a user has accessed the site.

## Running the project

Once the vagrant machine is up and the *news* database is setted, do the following steps:

1. In the command line write **python view.py** 
2. Go to your web browser and enter *http://localhost:8000/*

