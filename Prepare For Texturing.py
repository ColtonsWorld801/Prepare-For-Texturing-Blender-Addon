import bpy

#Prepare for texturing main panel

class PrepareForTextureingMainPanel(bpy.types.Panel):
    bl_label = "Prepare"
    bl_idname = "OBJECT_PT_MAINPANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Prepare For Textureing'

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text= "Press Apply Object Scale to begin.")
        row.operator('apply.scale_operator')
        
        row = layout.row()
        row.label(text= "Press Set Orgin To Geomotry to continue")
        row.operator('orgin.geometry_operator')
        
        row = layout.row()
        row.label(text= "Press Smart UV Unwrap To Finish")
        row.operator('uv.smart_operator')
        
        
        
 #Custom Operator For Applying Scale       
        
class PREPARE_OT_APPLY(bpy.types.Operator):
    bl_label = "Apply Object Scale"
    bl_idname = 'apply.scale_operator'
    
    def execute(self, content):

        bpy.context.scene.tool_settings.lock_object_mode = False
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

#Custom Operator For Orgin to Geometry    

class PREPARE_OT_ORGIN(bpy.types.Operator):
    bl_label = "Set orgin to geometry"
    bl_idname = 'orgin.geometry_operator'
    
    def execute(self, content):
        
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
        bpy.context.scene.tool_settings.lock_object_mode = False
        
#Custom Operator For Smart UV Unwraping

class PREPARE_OT_UV(bpy.types.Operator):
    bl_label = "Smart UV Unwrap"
    bl_idname = 'uv.smart_operator'
    
    def execute(self, content):
        
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.uv.smart_project(angle_limit=60)
        bpy.ops.object.editmode_toggle()
        bpy.context.scene.tool_settings.lock_object_mode = False

 #Register and Unregister

def register():
    bpy.utils.register_class(PrepareForTextureingMainPanel)
    bpy.utils.register_class(PREPARE_OT_APPLY)
    bpy.utils.register_class(PREPARE_OT_ORGIN)
    bpy.utils.register_class(PREPARE_OT_UV)
    
    

def unregister():
    bpy.utils.unregister_class(PrepareForTextureingMainPanel)
    bpy.utils.unregister_class(PREPARE_OT_APPLY)
    bpy.utils.unregister_class(PREPARE_OT_ORGIN)
    bpy.utils.unregister_class(PREPARE_OT_UV)

if __name__ == "__main__":
    register()
