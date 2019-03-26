#!/usr/bin/env python3

"""
    AUTHOR : Cavallo Luigi
    DESCRIPTION: 
    This module manage the various server instances active on the current machine.
    For now it can see all active server instances and send to them SIGKILL for 
    shutdown the service.
    TODOS:
    -> Define good architecture
    -> Implement individual operations by offering an interactive prompt
    -> Implement usage method for defined commands
"""

from manager import manager
from lib.utils.utils import message
import os
import sys

class monitor(object):
    """
        This is the system monitor which is responsible
        for starting the dialogue with the server that 
        manages the services. It can send to the server
        different command for start, kill or log services 
        data.
    """

    __version__ = "0.0"
    __author__  = "cavallo luigi"
    __email__ = "luigi.cavallo_lc@libero.it"

    def __init__(self, machine_services: object, server_config: object):
        # Services file position 
        self.root_service_log = os.path.join("machine-services", machine_services)
        # Config options of active services that must be initialized
        self.__server_config = self.__retrive_active_services()
        # Services Manager
        self.__manager = manager(self.__server_config)
        # All active services
        self.__services = None

    def shell(self):
        """
            Command and Controll system
        """
        while True:
            cmd = input("shell>")
            if cmd == "exit":
                # close honeypot
                break
            elif cmd == "start":
                """
                    This command allows you to start a certain service
                    or a list of services
                """
                pass
            elif cmd == "logs":
                """
                    This command allows you to view a real time log 
                    associated to a running service
                """
                pass
            elif cmd == "kill":
                """
                    This command allows you kill a runnig service or
                    a list of running services
                """
                pass
            else:
                message("Invalid command", "[!]", "red")
    
    def __retrive_active_services(self):
        """
            Parse the .services file generated by the scanner 
            an retrieve active service. If no active service 
            are found tells the manager to start only http,ftp
            services. Do this by populating the "active" entry
            in the server configuration file. If this operation
            fails so generate an error an block execution of 
            services manager.

            @return : active_services
        """
        active_services = []
        with open(self.root_service_log) as fd:
            for info in fd.readlines():
                proto, status, port = info.split("||")
                if status.strip() == "open":
                    active_services.append(proto.strip())
        return active_services


m = monitor("log.services", "config-test.json")


