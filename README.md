# Brand - Easy way to add a logo to photo.
> Simle project using Python Imaging Library 'Pillow' 

## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Features](#features)
* [Code Examples/Run](#features)

## General info
This is a simple application project, that allows you to add a logo to a chosen photo. 

## Screenshots
![Example watermark screenshot](./img/photo_watermark.jpg)
![Example logo add screenshot](./img/photo_logo.jpg)

## Technologies
* Python 3.8.5
* Pillow - Image

## Code Examples/Run
Show examples of usage:
Default - `pytohn brand.py picture.jpg logo.jpg`
Resize Logo - `pytohn brand.py picture.jpg logo.jpg 50`
Logo position - `pytohn brand.py picture.jpg logo.jpg 50 CC`
Margin - `pytohn brand.py picture.jpg logo.jpg 50 CC 20`
Watermark - `pytohn brand.py picture.jpg logo.jpg 50 W`

Size:
    Value in percent 0-100

Position:
LT  CT  RT  |   Left Top        Center Top      Right Top
LC  CC  RC  |   Left Center     Center Center   Right Center
LB  CB  RB  |   Left Bottom     Center Bottom   Right Bottom

Margin:
    Value in pixels 

## Features
List of features ready and TODOs for future development
* Add a chosen logo to the photo and save it as a new file.
* Resize the logo image
* Chose a one of nine predefined logo position
* Add a margin to the logo
* Use the logo to create a watermark 



