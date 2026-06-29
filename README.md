# Converter.-ttf-to-.woff-
This is a simple Python script to convert all .ttf's in a directory to .woff default directory = C:\Users\Public\Documents\ttf

I Created this for a specific need where I had a user ask me for .woff fonts. They were only able to find them in the .ttf format. 
This python Script converts '.tff' fonts to '.woff' fonts. that is all. 

Immportant: you may notice this is you read to script but the directory is hard coded to "C:\Users\Public\Documents\ttf". you can change this by editing the path in the script. this is designed to be lightweight and I really only needed it for a single instance. If I end up needing this again I may add a feature to change the directory using a GUI. 

Again, the directory your fonts need to be in is: C:\Users\Public\Documents\ttf


---------------------------
You may notice there are two .py scripts, one named convert.py and another named fullconvert.py, the first one only converts ttf fonts to woff fonts. the full script converts .tff fonts to .woff, .woff2, and otf fonts, you only need to run one, decide if you need .woff or all three fonts. 
