#include "Master.hpp"

bool	write_txt(std::string filename, std::string data)
{
	std::ofstream ofs(filename);

    if (!ofs.is_open())
    {
        std::cout << "Impossible to open the file !" << std::endl; 
        return (1);
    }
    else
	{
        ofs << data;
		return (0);
	}
}