#This identifier only is here so blender stops whining that I don't have a "manifest file." The real license is UNLICENSE.
#Blender 4.2 needs to shut up.

# SPDX-License-Identifier: UNLICENSE

bl_info = {
    "name": "Framerate Buttons In Editors",
    "author": "Splits285",
    "blender": (2, 80, 0),
    "version": (0, 0, 4),
    "description": "Adds a neat FPS slider to some editors",
    "doc_url": "https://github.com/Splits285 forgot to add the repo",
    "tracker_url": "https://github.com/Splits285/ /issues",
    "category": "Dope Sheet",
    "support": "COMMUNITY",
}

import bpy

#Read all about it @ https://docs.blender.org/api/current/bpy.types.UILayout.html
#Create the thing
class CUSTOM_PT_slider_panel(bpy.types.Panel):
    bl_label = "Custom Slider Panel"
    bl_space_type = 'DOPESHEET_EDITOR'
    bl_region_type = 'HEADER'

    def draw(self, context):
        layout = self.layout
       ##FPS slider
        row = layout.row()
        row.ui_units_x = 2.7
        row.prop(context.scene.render, "fps", text="FPS")

#Add our elements. They could be .prepend-ed as well but that looks weird being ahead of the window type button.
def register():
    bpy.utils.register_class(CUSTOM_PT_slider_panel)
    bpy.types.DOPESHEET_HT_header.append(CUSTOM_PT_slider_panel.draw)
    bpy.types.GRAPH_HT_header.append(CUSTOM_PT_slider_panel.draw)

#Remove them.
def unregister():
    bpy.types.DOPESHEET_HT_header.remove(CUSTOM_PT_slider_panel.draw)
    bpy.types.GRAPH_HT_header.remove(CUSTOM_PT_slider_panel.draw)
    bpy.utils.unregister_class(CUSTOM_PT_slider_panel)

#Spawn automatically if we're __main__.py I guess.
if __name__ == "__main__":
    register()