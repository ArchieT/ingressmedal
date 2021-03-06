ingressmedal
============

AP and medals counting for Ingress (game from Niantic Labs (a Google company))

**At the moment, no new medals are counted, the data format will also change, as I'm transforming my whole project into a Django project (it will be a web-app), while learning Django at the same time. If you're interested in my project, click Watch so you will know when something happens.**

Branches
---------
*`master`* branch is *always stable*, so you can safely just clone it for the latest version

Usage
---------

####The program is currently at an early stage of development, but it works well and already has many interesting features.

 * It can OCR the stats for you from the Ingress profile image
 * It can store data about many agents
 * It can print you the amount of AP you gained from different actions and their percentage of total AP.
 * It can save your entry to XML.
 * It can read your data from XML and tell you your average number of [attribute] per week between entries.
 * It can plot you a chart containing climbing to medals based on the XML database file, at the moment you can only view it from pyplot GUI, change the view (crop,resize), and save it from pyplot GUI.

####List of programs:

 * ./ocrentryandcuranalyze.py — analyze single entry and/or append it to the database (using ocrad and Pillow) (using tabulate)
 * ./entryandcuranalyze.py — the same, except it doesn't have OCR (using tabulate)
 * ./pastgainpweekbetwentrs.py — calculates your average gain of parameters per week between entries and shows it as an ASCII table (using tabulate)
 * ./plotmedalclimbing.py — plot a chart containing climbing to medals based on the XML database file, at the moment you can only view it from pyplot GUI, change the view (crop,resize), and save
 * ./plotmedalclimbgainavgperdaybetwentrs.py — same as above, except it contains the difference in medals' progress in percents divided by days between entries
 * ./plotapclimbing.py — same as above*2, axcept for that it cointains AP climbing data for total and for the 'apables' — actions which bring you AP
 * ./plotapgainavgperdaybetwentrs.py — difference in ap and apables between entries divided by days between entries
 

Program currently works only in text-only mode, except for pyplot GUI being opened.

###Search GMail for mails:
 * **edits**: *"Ingress Portal Data Edit Accepted:"*
 * **photos**: *"Ingress Portal Photo Accepted:"*
 
###What are the 'Uncomputables"?

The uncomputables are those values or parts of values, which can't be calculated. They are listed in the "AP-whereitcomesfrom-mindmap.mm" FreeMind mindmap in the info/ directory.

Why
---------

 * I'm learning Python
 * I'm playin' Ingress
 * I may accidentally create something... useful ;p
 
Credits
---------

During the creation of the OCR class, [https://github.com/BlueHerons/StatTracker/blob/master/code/OCR.class.php](https://github.com/BlueHerons/StatTracker/blob/master/code/OCR.class.php) [BlueHerons' StatTracker: master: commit [6650d1f](https://github.com/BlueHerons/StatTracker/commit/6650d1fff374af07d0d9a92beadd627bc428cdeb)] was very helpful, and some ideas in [ownlib/OcrRead.py](https://github.com/ArchieT/ingressmedal/blob/master/ownlib/OcrRead.py) are copied from it; Thanks!


Contributions
---------

If you want to fork my project, please send pull requests and regard my repository as the main repository, and let me be the project's main creator and owner — I'm learning Python for a fairly short time and I want everything to be presented as my own achievement. Of course, some help would be appreciated ;)

This code is shared to make it possible for people to help me create it. Please do not host it for regular use for more than a few people on your own without talking to me (and if I will allow to do so, I will require my name presented with a non-small font on the top of the front page).
