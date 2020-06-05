import json
import config

from base.output.dkey.csharp_dkey import CSharpDKey

class MDKey(CSharpDKey):

    def __init__(self):

        if config.debug:
            print('calling MDKey.__init__()')

        super().__init__()

        self.name = 'dkey_env_csharp_ext_ip'
        self.mtype = 'dkey'
        self.author = '@s0lst1c3'
        self.description = 'Environmental key derived from external IP address.'

        self.compatible_interfaces = [

            'csharp_runner_interface',
        ]
        self.compatible_imodules = [

            'ekey_env_ext_ip',
        ]

        self.functions = []
        self._vars = [

            'request',
            'response',
            'stream',
            'reader',
        ]
        self.comments = []
        self.whitespaces = []

        self.imports = [

            'System',
            'System.IO',
            'System.Net',
        ]

        self.template = 'dkeys/dkey_env_csharp_ext_ip.cs'

        self.func_name = 'derive'
        self.class_name = 'DKeyCSharpExtIP'

        self.mutate_func_name = True
        self.mutate_class_name = True
