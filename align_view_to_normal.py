
bl_info = {
    "name": "Align View to Normal",
    "blender": (4, 1, 0),
    "category": "3D View",
    "description": "Align the view to the selected normal in various directions from the right-click menu in edit mode",
    "location": "View3D > Edit Mode > Right-click Menu",
    "author": "flyinggoatman"
}

import bpy


def align_view_to_normal(context, direction='TOP'):
    obj = context.active_object
    if obj.mode == 'EDIT':
        bpy.ops.view3d.view_selected(use_all_regions=False)
        bpy.ops.transform.create_orientation(name='Normal', use=True, overwrite=True)
        bpy.ops.transform.select_orientation(orientation='Normal')
        
        bpy.ops.view3d.view_axis(type=direction, align_active=True)
        
    return {'FINISHED'}

class VIEW3D_OT_align_to_normal(bpy.types.Operator):
    bl_idname = "view3d.align_to_normal"
    bl_label = "Align View to Normal"
    bl_options = {'REGISTER', 'UNDO'}
    
    direction: bpy.props.EnumProperty(
        items=[
            ('TOP', "Top", ""),
            ('BOTTOM', "Bottom", ""),
            ('FRONT', "Front", ""),
            ('BACK', "Back", ""),
            ('RIGHT', "Right", ""),
            ('LEFT', "Left", "")
        ],
        name="Direction",
        description="Direction to align the view"
    )

    def execute(self, context):
        return align_view_to_normal(context, self.direction)

class VIEW3D_MT_align_view_to_normal_menu(bpy.types.Menu):
    bl_label = "Align View to Normal"

    def draw(self, context):
        layout = self.layout
        layout.operator("view3d.align_to_normal", text="Top").direction = 'TOP'
        layout.operator("view3d.align_to_normal", text="Bottom").direction = 'BOTTOM'
        layout.operator("view3d.align_to_normal", text="Front").direction = 'FRONT'
        layout.operator("view3d.align_to_normal", text="Back").direction = 'BACK'
        layout.operator("view3d.align_to_normal", text="Right").direction = 'RIGHT'
        layout.operator("view3d.align_to_normal", text="Left").direction = 'LEFT'

class VIEW3D_MT_align_view_to_normal_pie(bpy.types.Menu):
    bl_label = "Align View to Normal Pie Menu"

    def draw(self, context):
        layout = self.layout.menu_pie()
        layout.operator("view3d.align_to_normal", text="Top").direction = 'TOP'
        layout.operator("view3d.align_to_normal", text="Bottom").direction = 'BOTTOM'
        layout.operator("view3d.align_to_normal", text="Front").direction = 'FRONT'
        layout.operator("view3d.align_to_normal", text="Back").direction = 'BACK'
        layout.operator("view3d.align_to_normal", text="Right").direction = 'RIGHT'
        layout.operator("view3d.align_to_normal", text="Left").direction = 'LEFT'

def menu_func(self, context):
    if context.object.mode == 'EDIT':
        layout = self.layout
        layout.menu("VIEW3D_MT_align_view_to_normal_menu", icon="VIEW3D")

def register():
    bpy.utils.register_class(VIEW3D_OT_align_to_normal)
    bpy.utils.register_class(VIEW3D_MT_align_view_to_normal_menu)
    bpy.utils.register_class(VIEW3D_MT_align_view_to_normal_pie)
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.append(menu_func)
    

    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Mesh', space_type='EMPTY')
    kmi = km.keymap_items.new("wm.call_menu_pie", 'A', 'PRESS', ctrl=True, shift=True)
    kmi.properties.name = "VIEW3D_MT_align_view_to_normal_pie"

def unregister():
    bpy.utils.unregister_class(VIEW3D_OT_align_to_normal)
    bpy.utils.unregister_class(VIEW3D_MT_align_view_to_normal_menu)
    bpy.utils.unregister_class(VIEW3D_MT_align_view_to_normal_pie)
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.remove(menu_func)
    

    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps['Mesh']
    for kmi in km.keymap_items:
        if kmi.idname == 'wm.call_menu_pie' and kmi.properties.name == 'VIEW3D_MT_align_view_to_normal_pie':
            km.keymap_items.remove(kmi)
            break

if __name__ == "__main__":
    unregister()
    register()
