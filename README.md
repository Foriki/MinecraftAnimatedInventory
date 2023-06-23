# MinecraftGifInventory
this python script takes a gif, and makes it into a texturepack you can use in minecraft

to use this you will need the pillow libary:
pip install pillow
py mainv1.py
enter your gif(for example): example.gif
after you've that you should have output.png, copy it into template pack/assets/minecraft/mcpatcher/anim

bugs:
[ ] need to shift inventroy to accurately represent inventory slots


gif doesnt show in inventory?
when the mainv1 finishes it tells you how many frames the output.png has, take the output.png height and divide it by the amount of frames it has so for example
my output.png height is 6902 and i have 14 frames
6902/14=493
change the "h=" in the inventory.properties

if you dont get a round number add pixels to the end of the image 
if you know to know just search on google and swap the varriables with your thing yes
(image_height+x)/14=unround number+1
