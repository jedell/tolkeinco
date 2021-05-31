"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = ["marker_img.png","music.mp3","player_standing.png",
              "player_standing2.png","player_standing3.png",
              "player_standing4.png","player_walk1.png","player_walk2.png",
              "player_walk3.png","player_walk4.png","player_walk5.png",
              "player_walk6.png","walking.mp3","beleriand_map.jpg",
              "box_hov.png","box_nor.png"]
OPTIONS = {'argv_emulation': True}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)