#include "Master.hpp"

std::string	read_json(std::string filename)
{
	std::string data_read;
	std::ifstream ifs(filename);
    std::string buff;

    if (!ifs.is_open())
    {
        std::cout << "Impossible to open the file !" << std::endl; 
        return (data_read);
    }
    else
    {
        while (std::getline(ifs, buff))
        {
            if (!data_read.empty())
                data_read += "\n";
            data_read += buff;
        }
    }
	return (data_read);
}