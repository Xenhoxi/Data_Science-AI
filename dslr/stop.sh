#!/bin/bash

ENV="env"

if [ -d "$ENV" ]; then \
    deactivate
    rm -rf $ENV
    echo "Environnement virtuel supprimé."; \
else \
    echo "Auncun environnement virtuel détecté."; \
fi