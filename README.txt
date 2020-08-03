This program plays piano tiles on the website http://tanksw.com/piano-tiles/

You may have to adjust the coordinates of where the bot scans since the (x,y) coordinates is dependent on your specific computer.

Logic: The bot works by scanning 4 pixels (one point in each column) to see if it is black. If the pixel scanned is black, then the program will move the mouse to the pixel and click the location. As the piano tiles game progresses, the tiles move faster. And since the tiles move faster, the mouse cannot get to the point fast enough before the tile moves out of the way. In order to fix this the mouse should move more and more down as the game progresses in order to counteract the tiles moving faster.