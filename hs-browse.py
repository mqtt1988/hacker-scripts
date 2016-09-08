# Author: Areeb Beigh
# Created: 10th April 2016

"""
Opens all the URLs listed in config.ini [hs-browse] section
"""

#############################################################################
#    Copyright (C) 2016  Areeb Beigh <areebbeigh@gmail.com>                 #
#                                                                           #
#    This program is free software: you can redistribute it and/or modify   #
#    it under the terms of the GNU General Public License as published by   #
#    the Free Software Foundation, either version 3 of the License, or      #
#    (at your option) any later version.                                    #
#                                                                           #
#    This program is distributed in the hope that it will be useful,        #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#    GNU General Public License for more details.                           #
#                                                                           #
#    You should have received a copy of the GNU General Public License      #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.  #
#############################################################################

# Python imports
import webbrowser

# Local imports
from src.initialize import Initialize
from src.configreader import ConfigReader

initializer = Initialize()
config_file = initializer.config_file
config_reader = ConfigReader(config_file)
main = initializer.basic_main

# List of URLs to open (will be filled later)
urls = config_reader.read_config("hs-browse")


def execute():
    for url in urls:
        print(" Opening", url)
        # Opens the URL with the default browser
        webbrowser.open(url)

if __name__ == "__main__":
    main(execute)
