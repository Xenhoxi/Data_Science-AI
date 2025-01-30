#ifndef MASTER_HPP
# define MASTER_HPP

#include <string>
#include <fstream>
#include <iostream>
#include <curl/curl.h>

std::string read_json(std::string filename);
bool		write_txt(std::string filename, std::string data);

#endif