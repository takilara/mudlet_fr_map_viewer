# mudlet_fr_map_viewer
Repo to hold Mudlet Package for a Final Realms Map viewer


# Installation

## Mudlet

The package can be installed as a package or a module. It is recommended to use package mode for most usecases, but if you want to contribute code back, then the Module approach is recommended.

### As Package

Drag the mpackage file into your Mudlet window.
Or use "Toolbox"->"Package Manager" and load the mpackage file

### As Module

Or clone this repo, and use "Toolbox"->"Module Manager"->Install Module and point to the xml file FR_Map_Viewer.xml

Enable sync if you want to save back to the repo

## On the Mud

* type `gmcp on` on the mud (this will enable gmcp communication)
* Then run the command `MapViewer:load_json_map()` to perform the initial loading of the map

Then try to move around
