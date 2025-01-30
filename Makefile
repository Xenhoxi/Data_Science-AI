# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ljerinec <ljerinec@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/23 21:35:09 by ljerinec          #+#    #+#              #
#    Updated: 2025/01/30 16:12:37 by ljerinec         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

CXX = g++
CC = gcc
CFLAGS = -Werror -Wextra -Wall -lcurl

SOURCES_CPP =	test_api.cpp \

SOURCES_C = \

OBJECTS_CPP = $(SOURCES_CPP:.cpp=.o)
OBJECTS_C = $(SOURCES_C:.c=.o)
OBJECTS = $(OBJECTS_CPP) $(OBJECTS_C)

AI = openAI_api

GLOB_INC = -I includes/
BREW_LIB = -L /home/ljerinec/homebrew/lib
BREW_INC = -I /home/ljerinec/homebrew/include

####################COMPILATION STYLING####################

all: $(AI)

%.o: %.cpp
	@$(CXX) $(CFLAGS) -c $< -o $@ $(BREW_INC)

%.o: %.c
	@$(CC) $(CFLAGS) -c $< -o $@ $(BREW_INC)

$(AI): $(OBJECTS)
	@$(CXX) $(CFLAGS) -o $(AI) $(OBJECTS) $(BREW_LIB)

clean:
	@rm -f $(OBJECTS)

fclean: clean
	@rm $(AI)

re: fclean all

.PHONY: all clean fclean re



# %.o : %.c D'ou la ligne vient
# @$(eval CURRENT_FILE=$(shell echo $$(($(CURRENT_FILE)+1))))
# @$(eval PROGRESS=$(shell echo $$(($(CURRENT_FILE) * $(BAR_WIDTH) / $(TOTAL_FILES)))))
# @$(eval REMAINING=$(shell echo $$(($(BAR_WIDTH) - $(PROGRESS)))))

# @printf "$(PRINT_PREFIX) \033[1;33m[$(CURRENT_FILE)/$(TOTAL_FILES)] ["
# @printf "%${PROGRESS}s" | tr ' ' '■'
# @printf "%${REMAINING}s" | tr ' ' ' '
# @printf "]\r\033[0m"


# $(SCOP): $(OBJECTS) D'ou la ligne vient
# @printf "$(PRINT_PREFIX) \033[1;32m[$(CURRENT_FILE)/$(TOTAL_FILES)] ["
# @printf "%${PROGRESS}s" | tr ' ' '■'
# @printf "%${REMAINING}s" | tr ' ' ' '
# @printf "][OK]\n\033[0m"
