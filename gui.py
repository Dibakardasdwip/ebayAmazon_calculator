import PySimpleGUI as sg
from main import profit

label_buy = sg.Text("Buy", pad=(50,0))
input_buy = sg.InputText(tooltip="Buying Price", size= 10, key="buy" )

label_shipping = sg.Text("Shipping", pad=(30,0))
input_shipping = sg.InputText(tooltip="Shipping Price", size= 10, key="ship")

label_packaging = sg.Text("Packaging", pad=(30,0))
input_packaging = sg.InputText(tooltip="Packaging Price",size= 10, key="pack")

label_selling = sg.Text("Sell")
input_selling = sg.InputText(tooltip="Selling Price", size= 10, pad=(0,20,0,0), key="sell")

label_profit = sg.Text("Profit:", pad=(10,0,0,0))
text_box_profit = sg.Text("", key="popup")

enter_button = sg.Button("Enter")

layout = [[input_buy,input_shipping,input_packaging],
          [label_buy,label_shipping,label_packaging],
          [input_selling,label_selling,label_profit,text_box_profit],[enter_button]]

window = sg.Window("Calculator", layout=layout,font=["Helvetice", 20], return_keyboard_events=True)

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Enter":
            print(event,values)
            buy = float(values["buy"])
            print(buy)
            print(type(buy))
            ship = float(values["ship"])
            pack = float(values["pack"])
            sell = float(values["sell"])
            main_profit = profit(buy,ship,pack,sell)
            print("aaaaaaaaaaa",main_profit)
            window["popup"].update(value=(main_profit))

        case sg.WIN_CLOSED:
            break


window.close()