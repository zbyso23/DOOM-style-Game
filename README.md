# DOOM style 3d (raycasting) game in Python (based on Wolfenstein 3d)

Control: 'WASD' + mouse

[Source Youtube](https://www.youtube.com/watch?v=ECqUrT7IdqQ&t=665s)

### For inspire/improvemnets

[Wolefenstein Java](https://www.youtube.com/watch?v=XS6BA1t2JYw)
[I MADE PYTHON FPS SHOOTER IN 33 MINUTES](https://www.youtube.com/watch?v=kC67H2QJApY)
[Creating a First-Person Shooter in Python. (Devlog)](https://www.youtube.com/watch?v=yPRCEmnhRVI)
[Complete Raycasting Game Project in Python: Dead And! - RPG FPS Full course with code on github](https://www.youtube.com/watch?v=FLc6vUwyTdM&ab_channel=FinFET)
[Modding Dead And! into a first person shooter - Python Pygame 3D raycasting game devlog tutorial FPS](https://www.youtube.com/watch?v=UJVtpBGnn_k&ab_channel=FinFET)
[I Tried Making an FPS Game - ThreeJS](https://www.youtube.com/watch?v=3DMZETkPieI&ab_channel=SimonDev)

![doom](/sreenshots/0.gif)


### Build - Pyinstaller

#### Linux

```
source ./.venv/bin/activate
pyinstaller --onefile main.py
pyinstaller --onefile setup.py
cp -R resources dist/
```