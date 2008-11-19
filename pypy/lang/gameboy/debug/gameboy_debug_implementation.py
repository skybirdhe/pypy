#!/usr/bin/env python 
from __future__ import generators
        
from pypy.lang.gameboy.gameboy_implementation import *
from pypy.lang.gameboy.debug.debug_cpu import DebugCPU
from pypy.lang.gameboy.debug import debug
from pypy.lang.gameboy.debug.debug_rpc_xml_connection import *
from pypy.lang.gameboy.debug.debug_comparator import *
import time
import pdb

# GAMEBOY ----------------------------------------------------------------------

class GameBoyDebugImplementation(GameBoyImplementation):
    
    def __init__(self, debugger_port, skip_execs=0, debug_connection_class=None):
        GameBoyImplementation.__init__(self)
        self.cpu = DebugCPU(self.interrupt, self)
        self.debug_connection = debug_connection_class(self, debugger_port, skip_execs)
        self.create_comparators()
        
     # ------------------------------------------------------------------------   
    def create_comparators(self):
        self.gameboy_comparator = GameboyComparator(self.debug_connection, self)
        self.rom_comparator = ROMComparator(self, self.debug_connection, self)
    
    def compare_rom(data):
         self.rom_comparator.compare(data)
         
    def compare_system(data):
        self.gameboy_comparator.compare(data)
        
    # ------------------------------------------------------------------------
    
    def init_sdl(self):
        pass;
        
    def create_drivers(self):
        # make sure only the debug drivers are implemented
        self.clock = Clock()
        self.joypad_driver = JoypadDriverDebugImplementation()
        self.video_driver  = VideoDriverDebugImplementation()
        self.sound_driver  = SoundDriverImplementation()
        
    def emulate_cycle(self):
       	self.emulate(constants.GAMEBOY_CLOCK >> 2)
   
    def handle_execution_error(self, error):
    	print error
        print "closing socket debug_connections"
        pdb.set_trace()
        self.is_running = False
        debug.print_results()
        self.debug_connection.close()
    
    def handle_executed_op_code(self, is_fetch_execute=True):
        self.debug_connection.handle_executed_op_code(is_fetch_execute)
        
    def mainLoop(self):
        self.debug_connection.start_debug_session()
        GameBoyImplementation.mainLoop(self)
        
    
    
        
# VIDEO DRIVER -----------------------------------------------------------------

class VideoDriverDebugImplementation(VideoDriver):
    
    
    def __init__(self):
        # do not initialize any libsdl stuff
        VideoDriver.__init__(self)
    
    def update_display(self):
        # dont update the display, we're here only for testing
        pass
    
             
        
# JOYPAD DRIVER ----------------------------------------------------------------

class JoypadDriverDebugImplementation(JoypadDriver):
    
    def __init__(self):
        JoypadDriver.__init__(self)
      
    def update(self, event):
      	pass;  
        
        
# SOUND DRIVER -----------------------------------------------------------------

class SoundDriverDebugImplementation(SoundDriverImplementation):
    pass
    
    
# ==============================================================================
