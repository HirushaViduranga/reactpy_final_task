from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, event, html, use_state
import reactpy as rp
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

@component
def MyCrud():
    # Creating state
    alltodo = use_state([])
    name, set_name = use_state("")
    password, set_password = use_state("")
    contact_no, set_contact_no = use_state("")  
    address, set_address = use_state("")

    def mysubmit(event):
        newtodo = {
            "name": name,
            "password": password, 
            "contact_no": contact_no,
            "address": address
        }

        alltodo.set_value(alltodo.value + [newtodo])
        login(newtodo)  

    def handle_age_change(event):
        set_contact_no(event["target"]["value"])

    def handle_address_change(event): 
        set_address(event["target"]["value"])

    def clear_form():
        set_name("")
        set_password("")
        set_contact_no("")
        set_address("")

    # Looping data from alltodo to show on the web
    list = [
        html.li(
            {},
            f"{b} => {i['name']}  ; {i['password']} ; {i['contact_no']} ; {i['address']}",
        )
        for b, i in enumerate(alltodo.value)
    ]

    def handle_event(event):
        print(event)
        ##start point return mean return the out put 
        ##  html.div 
    background_image_url = "https://www.dhl.com/content/dam/dhl/local/global/dhl-global-forwarding/images/downloads/glo-dgf-zoom-wallpaper2-1920x1080.jpg"
    return html.div(
        {
         "style": {
                "position": "relative",
                "background-image": f"url('{background_image_url}')",
                "background-size": "cover",
                "background-repeat": "no-repeat",
                "padding": "50px 25px",
                "overflow": "hidden",  # Hide any overflowing content
            } 
        },
        
        html.div(                    ## this for button css.  in a single div there are to buttons
                {
                    "style": {
                    "position": "relative",
                    "z-index": "1",
                    "text-align": "center",
                    "color": "black",
                }
                },
         html.h1("DHL COURIER SERVICE."),
        html.span("SIGN UP FORM"),
        ),
        
         html.div(
            {
                "style": {
                    "position": "absolute",
                    "top": "0",
                    "left": "0",
                    "width": "100%",
                    "height": "100%",
                    "background-color": "rgba(0, 0, 0, 0.5)",  # Semi-transparent dark overlay
                    "z-index": "0",
                    "filter": "brightness(0.5) contrast(0.7)",  # Adjust brightness and contrast as needed
                }
            }
        ), 
        html.form(
            {"on_submit": mysubmit,
             "style": {
                "border": "1px solid #ced4da",  # Border for the form
                "padding": "10px 25px",              ## inside the box we want to increase padding use 
                "margin": "35px 400px",        ## out side of box it call margin 
                 "border-radius": "10px",
                 "box-shadow": "0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23)",
                "color": "white" ,
                "position": "relative",
                "z-index": "1",
                "background-color": "rgba(3, 3, 9, 0.5)" # Padding for the form
            }
             },   
           
            
            html.br(),
            html.label(                    ####   in this line label name willl show
                {"for": "name", "style": {"margin-right": "10px"}},
                "Name:"
            ),
            html.input(
                {
                    "type": "text",
                    "id": "name",
                    "placeholder": "Name",
                    "on_change": lambda event: set_name(event["target"]["value"]),
                    "style": {
                        "width": "100%",
                        "padding": "15px 8px",
                        "margin-top": "5px",
                        "margin-bottom": "10px",
                        "border": "1px solid #ced4da",
                        "border-radius": "4px",
                        "box-sizing": "border-box",
                    },
                }
            ),
            html.br(),
            html.br(),
            html.label(
                {"for": "password", "style": {"margin-right": "10px"}},
                "Password:"
            ),
            html.input(
                {
                    "type": "password",
                    "id": "password",
                    "placeholder": "Password",
                    "on_change": lambda event: set_password(event["target"]["value"]),
                    "style": {
                        "width": "100%",
                        "padding": "15px 8px",
                        "margin-top": "5px",
                        "margin-bottom": "10px",
                        "border": "1px solid #ced4da",
                        "border-radius": "4px",
                        "box-sizing": "border-box",
                    },
                }
            ),
            html.br(),
            html.br(),
            html.label(
                {"for": "contact_no", "style": {"margin-right": "10px"}},
                "Contact_no:"
            ),
            html.input(
                {
                    "type": "number",
                    "id": "contact_no",
                    "placeholder": "Contact no",
                    "on_change": handle_age_change,
                    "style": {
                        "width": "100%",
                        "padding": "15px 8px",
                        "margin-top": "5px",
                        "border": "1px solid #ced4da",
                        "border-radius": "4px",
                        "box-sizing": "border-box",
                    }
                }
            ),
            html.br(),
            html.br(),
            html.label(
                {"for": "address", "style": {"margin-right": "10px"}},
                "Address:"
            ),
            html.input(
                {
                    "type": "address",
                    "id": "address",
                    "placeholder": "Address",
                    "on_change": handle_address_change,
                    "style": {
                        "width": "100%",
                        "padding": "15px 8px",
                        "margin-top": "5px",
                        "border": "1px solid #ced4da",
                        "border-radius": "4px",
                        "box-sizing": "border-box",
                    }
                }
            ),
            html.div(
                {
                    "style": {
                        "display": "flex",
                        "justify-content": "space-between",
                        "margin-top": "20px",
                    }
                },
                html.button(
                    {
                        "type": "submit",
                        "on_click": event(lambda event: mysubmit(event), prevent_default=True),
                        "style": {
                            "background-color": "#FFD700",
                            "color": "black",
                            "border": "none",
                            "border-radius": "4px",
                            "padding": "10px 20px",
                            "cursor": "pointer",
                        },
                    },
                    "Submit",
                ),
                html.button(
                    {
                        "type": "submit",
                        "on_click": clear_form,
                        "style": {
                            "background-color": "#dc3545",
                            "color": "black",
                            "border": "none",
                            "border-radius": "4px",
                            "padding": "10px 20px",
                            "cursor": "pointer",
                        },
                    },
                    "Clear",
                ),
            ),
        ),
    #    html.ul(list),
    )

app = FastAPI()

from pymongo.mongo_client import MongoClient 
from pymongo.server_api import ServerApi



#Copy and pasting the MongoDB URI
uri= "mongodb+srv://ADMIN:admin123@cluster0.xaihwpf.mongodb.net/"
client = MongoClient(uri) #camel case

#defining the database name and collection
db = client["Reactpy_task1"]
collection= db["task1"]

#Checking the connection
try:
    client.admin.command("ping")
    print("Successfully connected Mongodb")
except Exception as e:
    print(e)
    
def login(login_data: dict):
    name = login_data["name"]
    password = login_data["password"]
    contact_no = login_data["contact_no"]
    address = login_data["address"]

    document = {
        "name": name,
        "password": password,
        "contact_no": contact_no,
        "address": address,
    } 
    print(document)

    post_id = collection.insert_one(document).inserted_id   ##insert document
    print(post_id)

    return {"message":"Login successful"}

    

configure(app, MyCrud)