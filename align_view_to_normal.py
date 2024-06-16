bl_info = {
    "name": "Align View to Normal",
    "blender": (4, 1, 0),
    "category": "3D View",
    "description": "Align the view to the selected normal in various directions from the right-click menu in edit mode",
    "location": "View3D > Edit Mode > Right-click Menu",
    "author": "flyinggoatman"
}

import bpy
import bmesh
import webbrowser

class AlignViewToNormalPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    menu_type: bpy.props.EnumProperty(
        name="Menu Type",
        description="Choose between pie menu and list menu",
        items=[
            ('PIE', "Pie Menu", "Use pie menu"),
            ('LIST', "List Menu", "Use list menu")
        ],
        default='PIE',
    )
    documentation_url: bpy.props.StringProperty(
        name="Documentation URL",
        description="URL for the add-on's documentation",
        default="https://github.com/flyinggoatman/blender-align-view-addon"
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "menu_type")
        layout.operator("wm.url_open", text="Open Documentation").url = self.documentation_url
        if self.menu_type == 'PIE':
            layout.label(text="Pie Menu is enabled")
        else:
            layout.label(text="List Menu is enabled")

class OpenURL(bpy.types.Operator):
    bl_idname = "wm.url_open"
    bl_label = "Open URL"
    
    url: bpy.props.StringProperty()

    def execute(self, context):
        webbrowser.open(self.url)
        return {'FINISHED'}

def align_view_to_normal(self, context, direction='TOP'):
    obj = context.active_object
    if obj.mode == 'EDIT':
        mesh = bmesh.from_edit_mesh(obj.data)
        if not (any(face.select for face in mesh.faces) or 
                any(edge.select for edge in mesh.edges) or 
                any(vert.select for vert in mesh.verts)):
            self.report({'ERROR'}, "You must select at least one face, edge, or vertex.")
            return {'CANCELLED'}
        
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
    disable_when_invalid: bpy.props.BoolProperty(
        name="Disable When Invalid",
        description="Disable this operator when selection is invalid",
        default=True
    )

    def execute(self, context):
        return align_view_to_normal(self, context, self.direction)

def is_selection_valid(context):
    obj = context.active_object
    if obj and obj.mode == 'EDIT':
        mesh = bmesh.from_edit_mesh(obj.data)
        return any(face.select for face in mesh.faces) or \
               any(edge.select for edge in mesh.edges) or \
               any(vert.select for vert in mesh.verts)
    return False

class VIEW3D_MT_align_view_to_normal_pie(bpy.types.Menu):
    bl_label = "Align View to Normal Pie Menu"

    def draw(self, context):
        layout = self.layout.menu_pie()
        valid_selection = is_selection_valid(context)
        layout.operator("view3d.align_to_normal", text="Top").direction = 'TOP'
        layout.operator("view3d.align_to_normal", text="Bottom").direction = 'BOTTOM'
        layout.operator("view3d.align_to_normal", text="Front").direction = 'FRONT'
        layout.operator("view3d.align_to_normal", text="Back").direction = 'BACK'
        layout.operator("view3d.align_to_normal", text="Right").direction = 'RIGHT'
        layout.operator("view3d.align_to_normal", text="Left").direction = 'LEFT'
        
        layout.separator()
        box = layout.box()
        col = box.column()
        col.label(text="Extra Options")
        col.operator("view3d.dummy_operator", text="Coming Soon 1")
        col.operator("view3d.dummy_operator", text="Coming Soon 2")

class VIEW3D_MT_align_view_to_normal_menu(bpy.types.Menu):
    bl_label = "Align View to Normal"

    def draw(self, context):
        layout = self.layout
        valid_selection = is_selection_valid(context)
        layout.operator("view3d.align_to_normal", text="Top").direction = 'TOP'
        layout.operator("view3d.align_to_normal", text="Bottom").direction = 'BOTTOM'
        layout.operator("view3d.align_to_normal", text="Front").direction = 'FRONT'
        layout.operator("view3d.align_to_normal", text="Back").direction = 'BACK'
        layout.operator("view3d.align_to_normal", text="Right").direction = 'RIGHT'
        layout.operator("view3d.align_to_normal", text="Left").direction = 'LEFT'
        
        layout.menu("VIEW3D_MT_align_view_to_normal_submenu")

class VIEW3D_MT_align_view_to_normal_submenu(bpy.types.Menu):
    bl_label = "Extra Options"

    def draw(self, context):
        layout = self.layout
        layout.operator("view3d.dummy_operator", text="Coming Soon 1")
        layout.operator("view3d.dummy_operator", text="Coming Soon 2")

class VIEW3D_OT_dummy_operator(bpy.types.Operator):
    bl_idname = "view3d.dummy_operator"
    bl_label = "Dummy Operator"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        self.report({'INFO'}, "Coming Soon")
        return {'FINISHED'}

def menu_func_pie(self, context):
    layout = self.layout
    layout.menu("VIEW3D_MT_align_view_to_normal_pie", icon="VIEW3D")

def menu_func_list(self, context):
    layout = self.layout
    layout.menu("VIEW3D_MT_align_view_to_normal_menu", icon="VIEW3D")

def update_menu(self, context):
    unregister()
    register()

def register():
    bpy.utils.register_class(AlignViewToNormalPreferences)
    bpy.utils.register_class(OpenURL)
    bpy.utils.register_class(VIEW3D_OT_align_to_normal)
    bpy.utils.register_class(VIEW3D_MT_align_view_to_normal_pie)
    bpy.utils.register_class(VIEW3D_MT_align_view_to_normal_menu)
    bpy.utils.register_class(VIEW3D_MT_align_view_to_normal_submenu)
    bpy.utils.register_class(VIEW3D_OT_dummy_operator)
    
    prefs = bpy.context.preferences.addons.get(__name__, None)
    if prefs:
        prefs = prefs.preferences
        if prefs.menu_type == 'PIE':
            bpy.types.VIEW3D_MT_edit_mesh_context_menu.append(menu_func_pie)
        else:
            bpy.types.VIEW3D_MT_edit_mesh_context_menu.append(menu_func_list)
    
        wm = bpy.context.window_manager
        km = wm.keyconfigs.addon.keymaps.new(name='Mesh', space_type='EMPTY')
        if prefs.menu_type == 'PIE':
            kmi = km.keymap_items.new("wm.call_menu_pie", 'A', 'PRESS', ctrl=True, shift=True)
            kmi.properties.name = "VIEW3D_MT_align_view_to_normal_pie"
        else:
            kmi = km.keymap_items.new("wm.call_menu", 'A', 'PRESS', ctrl=True, shift=True)
            kmi.properties.name = "VIEW3D_MT_align_view_to_normal_menu"

def unregister():
    prefs = bpy.context.preferences.addons.get(__name__, None)
    if prefs:
        prefs = prefs.preferences
        if prefs.menu_type == 'PIE':
            bpy.types.VIEW3D_MT_edit_mesh_context_menu.remove(menu_func_pie)
        else:
            bpy.types.VIEW3D_MT_edit_mesh_context_menu.remove(menu_func_list)

    bpy.utils.unregister_class(AlignViewToNormalPreferences)
    bpy.utils.unregister_class(OpenURL)
    bpy.utils.unregister_class(VIEW3D_OT_align_to_normal)
    bpy.utils.unregister_class(VIEW3D_MT_align_view_to_normal_pie)
    bpy.utils.unregister_class(VIEW3D_MT_align_view_to_normal_menu)
    bpy.utils.unregister_class(VIEW3D_MT_align_view_to_normal_submenu)
    bpy.utils.unregister_class(VIEW3D_OT_dummy_operator)
    
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.get('Mesh', None)
    if km:
        for kmi in km.keymap_items:
            if kmi.idname in ['wm.call_menu_pie', 'wm.call_menu']:
                km.keymap_items.remove(kmi)
                break

if __name__ == "__main__":
    register()

bpy.app.handlers.load_post.append(update_menu)
bpy.app.handlers.depsgraph_update_post.append(update_menu)
