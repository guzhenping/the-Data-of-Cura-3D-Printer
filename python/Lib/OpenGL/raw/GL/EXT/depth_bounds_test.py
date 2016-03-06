'''OpenGL extension EXT.depth_bounds_test

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_depth_bounds_test'
_DEPRECATED = False
GL_DEPTH_BOUNDS_TEST_EXT = constant.Constant( 'GL_DEPTH_BOUNDS_TEST_EXT', 0x8890 )
glget.addGLGetConstant( GL_DEPTH_BOUNDS_TEST_EXT, (1,) )
GL_DEPTH_BOUNDS_EXT = constant.Constant( 'GL_DEPTH_BOUNDS_EXT', 0x8891 )
glget.addGLGetConstant( GL_DEPTH_BOUNDS_EXT, (1,) )
glDepthBoundsEXT = platform.createExtensionFunction( 
'glDepthBoundsEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLclampd,constants.GLclampd,),
doc='glDepthBoundsEXT(GLclampd(zmin), GLclampd(zmax)) -> None',
argNames=('zmin','zmax',),
deprecated=_DEPRECATED,
)


def glInitDepthBoundsTestEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )