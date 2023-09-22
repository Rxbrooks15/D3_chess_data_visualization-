# D3_chess_data_visualization-

Youtube link for demonstration below
(IMPORTANT)
https://youtu.be/AqJKR_vPSD0

Notes for story boarding and context down (below)
Context:
In QSS17 I plotted data in Regard to the ELO of famous grandmasters. The animated plot highlighted the 
progress of the players over the years. Now I was thinking of getting a better story by looking at MY
chess.com rating over the years. I could start will rapid and see if I can include additional data like my 
bullet and blitz rating 
Step1: Scrape chess.com data
Step2: Make dummuy plots in R
Step3: Make interactive plot in R
Step4: Work in D3 and try to add some interactive feature 

For the recreation I can try to recreate the chess.com elo rating plot here https://www.chess.com/stats/live/rapid/rainebrookshire/0
I can do this for the 3 time controls and have 3 or 4 plots
My D3 plot will document my progress and performance in chess from 2017-2023 and will include my progress 
in Bullet, Rapid, Blitz, and Daily chess... PS. Bullet includes games played under 3 minutes (mostly 1 minute speed chess)
Blitz includes games of 3 minutes to 14 minutes, rapid games go for 15 minutes and longer an daily games go 
over 24 hours to 7 days 

Brainstorming:
Dot plot seems likely 
Maybe an animation of my common chess openings is possible*


Challenges:

Added 140 to the userRating within the tooltip and data to account for discrepancy  as points werent lining up with the axis 

Had a hard time trying to reduce the number of breaks (default slider has 6 breaks) within the slider to make it smooth
I tried to incorporate a UI slider to help with this but there were some plotting issues 

Couldnt find a way to have interactive tooltip with double tap zoom feature. Brainstormed and ended up 
using sliders which were functional  

Had x-axis functionality issues when trying to merge my main code with my sliders code to have both the tooltip 
(hover feature) and sliding feature 
Had issue where only slider would zoom but points would stay the same: an update function was an easy fix 
Used https://www.remove.bg/ to remove background from chess pngs



Attempted to get transparent background images for my chess pawns but I had to infact use the file images from 
https://www.remove.bg/ and upload them to remove the background and download the edited image 
In this case, there was the annoying issue of white chess pieces having both the background and the white inner filling 
being removed. The proper chess images needed to be selected 

There were many challenges working in d3 so I will summarize
Axis unalighnemt 
tooltip & zooming conflict 
Dropbox challenges
zooming using brush and double tap malfunction
pawn image implementation
hover functionality 
opening url link 

Resources and notes: 
USED https://chessinsights.xyz WHICH is a tool that uses the chess.com api to export all user data to a csv. 
this came from https://www.reddit.com/r/chess/comments/118pyr5/i_made_a_website_that_lets_you_visualize_and/
and he provided the python script (https://github.com/NotJoeMartinez/chess-insights/blob/main/cli/chess_api_cli.py)
Which helped in scraping my data. The code is found in python_scrape -> raine_scrape
collected_data is a personal scrape of my chess.data in python but lacked information and functionality 

HTML documents within my main D3 file show layers and plots that helped me get to the final plot 


Functionality of D3 final plot:
Layers of functionality 
hover feature 
pawn implementation 
slider feature 
dropbox feature 


Slider:
sliderpoints represent years: leftmost is 2017 and rightmost is 2023
slider points zoom in based on increasing the distance between the years 
Note* The START slider length usually has to be less than the END slider length 
having the start slider greater than the end shows the points backwards 

You can click on either slider and use the right or left arrows to toggle movement 

Slider mostly can isolate clusters but doesnt do a good job of viewing individual points  

Dropbox:
Select any of the time control elements to see progress and elo over the 6 year period 

tooltip: 
Hover over points get get information about the specific game. Works better with isolated points 
Sometimes you have to wiggle mouse over a point for hover to work. Sometimes you also have quickly 
approach a point for tooltip to recognize mouse
Again* you can click on the Opening link by right clicking on the pawn and clicking on the link 
wORKS BEST WITH ISOLATED PAWNS (GOOD ISOLATED EXAMPLES ARE IN THE DAILY TIMECONTROL )

Zoom: 
There is a zoom based on the x-axis with the slider 
but a default zoom that allows you to zoom in to clusters and pawns. HAS NO EFFECT ON THE SCALE
you can zoom in how you would zoom in or move around a regular pdf file 
