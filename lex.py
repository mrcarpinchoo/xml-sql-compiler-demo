#!/usr/bin/env python3

import ply.lex as lex

def t_error(token):
    print("Illegal character", token.value[0])

    token.lexer.skip(1)
# end def

# tokens
tokens = (
    "CARS_O",
    "CARS_C",
    "CAR_O",
    "CAR_C",
    "ID_O",
    "ID_C",
    "BRAND_O",
    "BRAND_C",
    "MODEL_O",
    "MODEL_C",
    "YEAR_O",
    "YEAR_C",
    "LICENSE_PLATE_O",
    "LICENSE_PLATE_C",
    "AVAILABLE_O",
    "AVAILABLE_C",
    "RENTAL_PRICE_O",
    "RENTAL_PRICE_C",
    "TRANSMISSION_O",
    "TRANSMISSION_C",
    "SERVICES_O",
    "SERVICES_C",
    "SERVICE_O",
    "SERVICE_C",
    "DATE_O",
    "DATE_C",
    "DESCRIPTION_O",
    "DESCRIPTION_C",
    "LICENSE_PLATE",
    "YEAR",
    "ID",
    "AVAILABLE",
    "RENTAL_PRICE",
    "TRANSMISSION",
    "DATE",
    "TEXT",
)

t_CARS_O = r"<cars>"
t_CARS_C = r"</cars>"

t_CAR_O = r"<car>"
t_CAR_C = r"</car>"

t_ID_O = r"<id>"
t_ID_C = r"</id>"

t_BRAND_O = r"<brand>"
t_BRAND_C = r"</brand>"

t_MODEL_O = r"<model>"
t_MODEL_C = r"</model>"

t_YEAR_O = r"<year>"
t_YEAR_C = r"</year>"

t_LICENSE_PLATE_O = r"<license_plate>"
t_LICENSE_PLATE_C = r"</license_plate>"

t_AVAILABLE_O = r"<available>"
t_AVAILABLE_C = r"</available>"

t_RENTAL_PRICE_O = r"<rental_price>"
t_RENTAL_PRICE_C = r"</rental_price>"

t_TRANSMISSION_O = r"<transmission>"
t_TRANSMISSION_C = r"</transmission>"

t_SERVICES_O = r"<services>"
t_SERVICES_C = r"</services>"

t_SERVICE_O = r"<service>"
t_SERVICE_C = r"</service>"

t_DATE_O = r"<date>"
t_DATE_C = r"</date>"

t_DESCRIPTION_O = r"<description>"
t_DESCRIPTION_C = r"</description>"

t_LICENSE_PLATE = r"[A-Z]{3}-[0-9]{3}"
t_YEAR = r"[0-9]{4}"
t_ID = r"[0-9]{3}"
t_AVAILABLE = r"(?:true|false)"
t_RENTAL_PRICE = r"[0-9]+\.[0-9]{2}"
t_TRANSMISSION = r"(?:automatic|manual)"
t_DATE = r"[0-9]{4}-(?:0[1-9]|[1][0-1])-(?:0[1-9]|1[0-9]|2[0-9]|3[0-1])"
t_TEXT = r"[A-Za-z ]+"

t_ignore = " \t\n"

lexer = lex.lex()