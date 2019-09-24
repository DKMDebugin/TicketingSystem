# TICKETING SYSTEM DOCS
## Overview
The main purpose of this application, is to create a platform where clients can submit their issues by raising tickets, and also see their issues resolved.
The ticketing system application will be connected to an email account, where a client can just raise a ticket by directly sending a mail from his or her email account. The application will also be able to directly send mails by directly replying to tickets.
### SPECIFICATION
* A dashboard showing tickets
* Request time(time when ticket was raised by the client)
* Response time(time showing when ticket was closed by an admin)
* Automatic response to clients anytime tickets are raised (i.e lets say a client with email account example@gmail.com raises a ticket, there should be an automatic response like thank you example@gmail.com your ticket has been created successfully your ticket id is 2233444).

   **Note:**
Ticket id will be uniquely generated as soon as ticket is created. Each ticket will be identified using the id
* You should be able to view contents of a ticket when you click on that particular ticket
* You should be able to update the status of a ticket, any time you update the status of a ticket, the clients will also get emails telling him or her the status of his or her ticket.
* A log in to the ticketing platform
* Access to the platform will be restricted using role. Where a super admin can perform all features in the application, while ordinary admins can only perform selected features.

## SYSTEM ANALYSIS & DESIGN
## MODELS/DATABASES
* User
* Ticket
* Company
* Project
* Task
### User Model:
First Name, Last Name, Email, is_staff, is_active, Company (foreign key)
### Ticket Model:
ID, Request Time, Response Time, User (foreign key), Status (open/close), Subject, Message, Priority (high, mid or low), Project (foreign key), Task (foreign key), is_active,
### Company Model:
ID, Name, is_active,
### Project Model:
ID, Name, Description, Company (foreign key), is_active,
### Task Model:
ID, Name, Description, Project (foreign key), is_active,

## BUSINESS LAYERS/ VIEWS
* User Authentication: Create, Login, Logout, List, Detail
* Ticket: Create, List, Detail, Delete, Update, Search
* Projects: Create, List, Detail, Delete
* Tasks: Create, List, Detail, Delete
* Companies: Create, List, Detail, Delete
* Signals:
    - Send mail after ticket is created
    - Send mail after ticket is updated
* Connect app to a particular email account in such a way that users can create a ticket by sending a mail to that email account.
* Access to some functionalities is restricted using roles.
* Set response time when the ticket is closed.
