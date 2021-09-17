# dr14tool
Toolset for DR14 T.Meter for measuring audio compression. 

## Description
dr14tool is a wrapper aroound DR14 T.Meter. dr14tool can be used to scan your whole music collection for the existence of dr14.txt, the file in which DR14 T.Meter stores the compression information; if dr14.txt does not exist, it will generate the file on the fly. dr14tool can also be used to report the compression value for each album of your whole music library in one report.

## What is DR14 T.Meter?
DR14 T.meter is a free and open-source command-line tool for computing the Dynamic Range (DR) of your music according to the procedure used in the off-line meter released by the Pleasurize Music Foundation. DR is also known as 'loudness war'.\
\
For more info, see:
* DR14 T.Meter: http://dr14tmeter.sourceforge.net/index.php/Main_Page
* DR Compression Database: http://dr.loudness-war.info/

## Requirements
* python3
* dr14_tmeter

## Installation 
`# dr14_tmeter`\
`sudo apt install lame flac vorbis-tools faad ffmpeg`\
`sudo apt install python3-pip`\
`sudo pip3 install numpy scipy`\
`sudo pip3 install DR14-T.meter`\
`# dr14tool`\
`wget https://raw.githubusercontent.com/markbaaijens/dr14tool/master/dr14tool.py -O dr14tool.py`

## Usage
`python3 dr14tool.py [--scan] "[music folder]"`\
dr14tool scans your music library to detect dr14.txt. If absent, it will be generated. Note that dr14_tmeter it self has an option for recursive scanning; but the problem with that is that it overwrites every dr14.txt for a new one. Thus, scanning a large number of albums shall take a very long time. Scan-mode is default, so `python3 dr14tool.py [music folder]` will also work.\
\
`python3 dr14tool.py --report [music folder]`\
dr14tool scans your music folder for the existence of dr14.txt. It than outputs the DR-value per album, in a convenient and compact format, like this:
> 11 Bach/Goldberg Variations BWV 988 (Glenn Gould 1955) 1955\
> 13 Baker, Chet/Chet Baker Sings\
> 11 Beatles, The/Sgt Peppers Lonely Hearts Club Band\
> 14 Beethoven/Cello Sonata No. 1 Op. 5 No. 1 (Jacqueline du Prey,  Daniel Barenboim)



