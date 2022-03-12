# T4A2-B Full Stack Application - Capstone - Joseph Buhagiar

**Website is hosted at:** http://3.26.206.173:8000/
**Github Repo:** https://github.com/JoeComputational/djangoshop

**To run the application locally do the following steps:**
0 Install pip with (python3 get-pip.py) or (python get.pip.py)
1 Navigate to the store folder and (pip install -r requirements.txt)
2 Install Django with (pip install django)
3 Navigate into the ecommerce folder with (cd ecommerce)
4 Run (python3 manage.py runserver)
5 in your browser - navigate to http:127.0.0.1:8000
6 Enjoy :)



## CMP1043-1.3 Appropriate use of libraries used in the app
**EC2 hosting** - This is Amazon's Elastic Cloud Compute service, it allows me to rent a hypervisor and host my application on one sturdy platform. As the application, I have developed is small in nature, I did not have to remotely store and service my images and databases on external Amazon services. These services would've included Amazon RDS which is a database service - as well as Amazon S3 which is a file/image store for larger applications and programs.

**SQlite** - A database servier that uses SQL language instancing. Comes prepackaged with Django so implementation was rather simple and connection worked well out of the gate. Just required Models to be added to the code.

**Django** - is an open-source web framework that was developed to be used with the Python programming language. It uses the model-template-view architecture and was really fun to learn as I developed this web app. It was difficult at first until I figured out the layout and the need for root folders and sub root folders - such as splitting shop and store with separate settings and URL roots so that I can add new features in the future.

**Stripe** - This is a financial application company that works together with banks to implement easy and straightforward purchase platforms. They have separate levels of API - including a full checkout and Database implementation, a simple and secure checkout page with remote database integration or just a secure card processing platform that is generally used by bigger organisations.

**Pillow** - This is a library for Python that helps with file and image manipulation within the application itself. This helps with image restructuring with bootstrap.

**Pip** - This is a packet management system that is used with Python. It is used to install and manage packages that depend on Python and Python depends for importing features, routes and tests. Helps greatly add packages to their application.

**Unittest** - This is a Python module that provides a rich set of tools that help build and run tests against. It can be used as either a test case scenario, fixture or a full suite that tests all aspects of the application - but require to be written independently by the developer.

**Python3** - This is a newer version of the Python programming language. It is Object-Orientated and is an interpreted language which means the machine interprets it as its written, instead of needing to be compiled into assembly or machine code.

**Virtual Env** - This is a package that allows users to set up and deploy their code from a virtual setting - keeping all files local. It is all done, employed and deployed through the command line.

Not all of these are Libraries of Python or development libraries. But they are required to build my application the way I have built it. I would also consider a few of these almost as a prerequisite to building a good quality application.

## PRG1006-2.1 Employ and utilise proper source control methodology
To achieve this I have created a public Git Repository and am filling out my README.md so that users understand how to run and use my application. The git commits have a .gitignore file that ignores files that are not required by the end user, the commits are also over more than one branch and over 15 commits in total. Every commit was for a new feature or fixing errors that were encountered.

## PRG1006-2.2 Employ and utilise project management methodology

To build this webshop I found it easiest and best practice to implement an agile project management methodology towards the development. This helped me make sure that features and tasks were completed within a timely manner to a reasonably well-done standard. Along with the Agile methodology, I Implemented a Trello board with due dates and checklists for feature completion. This was done as instead of working in a group - the assessment was changed to an individual working environment and I required external help (Trello) to keep track of required tasks/features and what date they should be completed by. 

As an independent developer, it was quite difficult - this is due to the fact that I believe my strengths are in the back end of the application - the interconnectivity of everything and setting up the database. I also love working with scripting languages and cloud technologies. This is where I believe my strengths lay.

Where I truly lack skills and ability is with the front end of the application. What the user will see - that is why for this application I have chosen to import a free boilerplate template that is using bootstrap. It's important to remember when doing so - to create security key pairs so that no nasty interference can be made between that external connection.

## PRG1006-2.3 Employ and utilise task delegation methodology

As above, I have been given this task to complete on my own. But to be able to manage the application and its features - have was using a Trello board with due dates and features plastered all over it to make sure everything was completed by due date

![Trello 1](https://i.ibb.co/sC3gLHb/Trella1.png)
Started the Trello off with all of the features that I believe will be required for the application and with a date that I would like them completed by.


![Trello 2](https://i.ibb.co/mFSJycY/trella2.png)
In this step I have started production on the database, homepage and Items for sale that are available on the website.

![Trello 3](https://i.ibb.co/TgrCQSh/trella3.png)
Here I have tested the 3 features mentioned above, all had issues that were rectified and have also started completing the Stripe API and Database implementation with stripe.

![Trello 4](https://i.ibb.co/4ZktN0q/trella-4.png)
Now looking at EC2 hosting and pushing features to Git. Also now testing the Stripe implementation and how it interacts with the database. Saves the purchase locally - but also saves it on the Stripe page with their bank details for a more secure service.

![Trello 5](https://i.ibb.co/YRpdhFw/trella5.png)
Pushing the rest of Stripe production to git and ready for production, EC2 instancing seems simple enough, will add application to the instance on next board.

![Trello 6](https://i.ibb.co/2gyXLCP/Trella6.png)
Features are all completed and are being pushed to production/main b ranch - application done. Working out EC2 Hosting for final step.

![Final Trello](https://i.ibb.co/k6qyWFD/trella7.png)
App is done and fully EC2 hosted - have chosen not to purchase a domain as its not a project I will continue on with.
## PRG1006-7.1 Development testing
![Development Testing Completed](https://i.ibb.co/2FBSCvg/Manual-Developer-Tests.png%20)

These were extention tests that I as the developer completed. These were ontop of the testing that was completed by an end user for the website. There are a few features that I still need to work on to complete, but for the most part - the website is live and working and processing orders. I just need to implement a bit more with the database to fully connect to purchased items.

The site can be accessed here: http://3.26.206.173:8000/

And is working well, both purchases and and cancellation of orders is working properly as well as storing purchases in both the database that is built in SQLite and via Stripes online hosted database.

This here is what the homepage looks like:
![Mighty Bean Store](https://i.ibb.co/yfky8J8/beans.png)


The Stripe Checkout page looks like this:
![Stripe checkout](https://i.ibb.co/tX3HGt0/stripe.png)

All which are working as intended

## PRG1006-7.2 Production testing
![Production Testing completed](https://i.ibb.co/xM0JtCk/Manual-Production-Testing.png)

Here is the testing done from an end user perspective, making sure that all directional routing is working and purchases can be made or cancelled. I have also included database rectifications required in this test as I believe these are all very important steps that are needed to be rectified.