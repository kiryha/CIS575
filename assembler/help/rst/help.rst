Intro
=====
The Book Assembler is an application that manages pages for the workbook.

Process
=======
The process of book developing includes such phases: concept, design, layout, and printing.

During concept phase the Book Author creates the draft version of the book that consist of a page sketches.
Once concept is done each page is saved as a jpeg file and sent to Illustrator.

At the design phase illustrator creates the final illustrations and return them back to author for review and storage.
Author place illustrations into the same folder with pages. Author decides when page is finalized and publishes
the finalized version (record the approved version to the database).

Once all Illustrations are finalized, they being send to layout artist who creates a Print PDF file for printing.
This file is sent to a printing facility to produce the circulation of the book.

The book development process is not linear, each page goes through multiple rounds of revisions, and hence
each page file has multiple versions.

The pages that Author sending to Layout Artist does not contain version component in the file name,
which allows automatic update of all pages to the final in Layout Software.


Assembler UI
============
The Book Assembler UI description.

.. image:: images/main_window.jpg
  :target: _images/main_window.jpg

Installation and Launch
-----------------------
Place the Book Assembler package to any folder on your local drive.
Double click the launch_assembler.bat file to run application. The Book Assembler Main window will appear.

Project Structure and Naming Conventions
----------------------------------------
Any book project should contain:

- `<project root>/pages/jpg` folder. Place pages files here.
- `<project root>/pages/jpg/final` folder. Assembler copy published pages without extension here.
- `<project root>/pages/pdf` folder. PDF files crested here.

Page file should be named: `<page_number>_<version>.jpg`


Menu
----
Book Assembler contains Help > Documentation item.

This will open Default Web browser with HTML Documentation page.

Main area
---------
The Book Assembler UI contains two parts, *Current Project/Project Pages* and *Page Preview*

To define the current project to work with, click "Set Project" button, navigate to the folder with current book
and press `Select Folder`. The Book Assembler will read existing pages and display the list in `Project Pages` table.

`Project Pages` table contains columns:

- Number: page number/name
- Pub: page published version
- Sent: page version sent to final folder
- Description: user note about page

`[ + ] and [ - ]`: Increase or Decrease version of selected page


`Publish Current Version`: Record current version as final into the database

`Reload Pages`: Update application UI if added a new pages to folder

`[ SEL ] Sent Published Versions`: Copy published pages to final folder without extension. If `SEL` activated, copy only pages,
selected in UI.

`[ pdf version ] Generate PDF File`: Create PDF file of all published pages.


Status line
-----------
The status line at the bottom of main window outputs messages regarding program actions.