
import dash_bootstrap_components as dbc


def create_navbar(page):
    # Create the Navbar using Dash Bootstrap Components
    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu", # Label given to the dropdown menu
                children=[
                    # In this part of the code we create the items that will appear in the dropdown menu on the right
                    # side of the Navbar.  The first parameter is the text that appears and the second parameter 
                    # is the URL extension.
                    dbc.DropdownMenuItem("Total", href='/'), # Hyperlink item that appears in the dropdown menu
                  #   dbc.DropdownMenuItem(divider=True), # Divider item that appears in the dropdown menu 
                    dbc.DropdownMenuItem("Source of Payment", href='/payment'), # Hyperlink item that appears in the dropdown menu
                    dbc.DropdownMenuItem("Weight Gain", href='/weight_gain'), # Hyperlink item that appears in the dropdown menu
                    dbc.DropdownMenuItem("Prenatal Care", href='/prenatal_care') # Hyperlink item that appears in the dropdown menu
                ],
            ),
        ],
        brand = page,
        sticky="top",  # Stick it to the top... like Spider Man crawling on the ceiling?
        color="dark",  # Change this to change color of the navbar e.g. "primary", "secondary" etc.
        dark=True,  # Change this to change color of text within the navbar (False for light text)
    )

    return navbar