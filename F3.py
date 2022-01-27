import tkinter as tk
import tkinter.font as font
from tkinter import*


def change_to_basket():
    """
    This function swaps from the products frame
    to the basket frame.
    :return: Nothing
    """
    basket_frame.pack(fill='both', expand=1)
    products_frame.forget()


def change_to_products():
    """
    This function swaps from the basket frame
    back to the products frame.
    :return: Nothing
    """
    products_frame.pack(fill='both', expand=1)
    basket_frame.forget()


def back_to_basket():
    """
    This function swaps from the shipping frame
    back to the basket frame.
    :return: Nothing
    """
    basket_frame.pack(fill='both', expand=1)
    shipping_frame.forget()


def continue_to_shipping():
    """
    This function swaps from the basket frame
    to the shipping frame.
    :return: Nothing
    """
    shipping_frame.pack(fill='both', expand=1)
    basket_frame.forget()


def continue_to_receipt():
    """
    This function swaps from the shipping frame to the receipt frame.
    :return: Nothing
    """
    receipt_frame.pack(fill='both', expand=1)
    shipping_frame.forget()


def back_to_shipping():
    """
    This function swaps from the receipt frame to the shipping frame.
    :return: Nothing
    """
    shipping_frame.pack(fill='both', expand=1)
    receipt_frame.forget()


def add_to_basket():
    """
    This function adds the current dropdown select to the listbox
    :return: Nothing
    """
    basket.insert(END, item.get())


def remove_from_basket():
    """
    This function removes the current dropdown select from the listbox
    :return: Nothing
    """
    basket.delete(basket.curselection())


def print_receipt():
    """
    This function prints the entries into a list box.
    :return:
    """
    forename = forename_entry.get()
    surname = surname_entry.get()
    postcode = postcode_entry.get()
    house_number = house_number_entry.get()
    county_city = county_city_entry.get()
    town = town_entry.get()
    receipt_forename.config(text=forename)
    receipt_surname.config(text=surname)
    receipt_postcode.config(text=postcode)
    receipt_house_number.config(text=house_number)
    receipt_county_city.config(text=county_city)
    receipt_town.config(text=town)


# window data (how big, positioning on screen)
root = tk.Tk()
root.configure(bg='gray20')
root.iconphoto(True,
               tk.PhotoImage(file='aatlogo.png'))
width, height = 600, 500
root.geometry('%dx%d+0+0' % (width, height))
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cord = int((screen_width/2) - (width/2))
y_cord = int((screen_height/2) - (height/2))
root.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))
root.title('Shopping basket')

# creating fonts
font_large = font.Font(family='Georgia',
                       size='24',
                       weight='bold')
font_small = font.Font(family='Georgia',
                       size='12')

# frames
products_frame = tk.Frame(root, background='gray20')
basket_frame = tk.Frame(root, background='gray20')
shipping_frame = tk.Frame(root, background='gray20')
receipt_frame = tk.Frame(root, background='gray20')

# heading for products frame
lbl_heading_products = tk.Label(products_frame,
                                text='Products page',
                                font=font_large,
                                bg='gray20',
                                fg='white')

# pack heading
lbl_heading_products.pack()

# products label
products_lbl = tk.Label(products_frame,
                        text='Products',
                        font=font_small,
                        bg='gray20',
                        fg='white')

products_lbl.pack()

# create variable
item = StringVar(root)
items = {'PS5': '469', 'Action Man': '15', 'Lego Star Wars': '60', 'Nintendo Switch': '269', 'Nerf Gun': '40',
         'Monopoly': '20', 'Slime': '5', 'Lego Batman': '65'}
# drop down menu
items_menu = OptionMenu(products_frame, item, *items)

# pack dropdown menu
items_menu.pack()

# button to switch to basket frame
btn_change_to_basket = tk.Button(products_frame,
                                 text='View basket',
                                 font=font_small,
                                 bg='gray10',
                                 fg='white',
                                 command=change_to_basket)
# pack button
btn_change_to_basket.pack()

# button to add to basket
add_to_basket_btn = tk.Button(products_frame,
                              text='Add to basket',
                              font=font_small,
                              bg='gray10',
                              fg='white',
                              command=add_to_basket)

# pack button
add_to_basket_btn.pack()

# pack products frame
products_frame.pack(fill='both', expand=1)

# heading for basket frame
lbl_heading_basket = tk.Label(basket_frame,
                              text='Your basket',
                              font=font_large,
                              bg='gray20',
                              fg='white')

# pack heading
lbl_heading_basket.pack()


basket = tk.Listbox(basket_frame,
                    bg='gray10',
                    fg='white')
basket.pack()

# button to remove from basket
remove_from_basket_btn = tk.Button(basket_frame,
                                   text='Remove from basket',
                                   font=font_small,
                                   bg='gray10',
                                   fg='white',
                                   command=remove_from_basket)

# pack button
remove_from_basket_btn.pack()

# button to switch back to products frame
btn_change_to_products = tk.Button(basket_frame,
                                   text='Back to products',
                                   font=font_small,
                                   bg='gray10',
                                   fg='white',
                                   command=change_to_products)
# pack button
btn_change_to_products.pack()

# button to continue to shipping
btn_continue_to_shipping = tk.Button(basket_frame,
                                     text='Continue to shipping',
                                     font=font_small,
                                     bg='gray10',
                                     fg='white',
                                     command=continue_to_shipping)
# pack button
btn_continue_to_shipping.pack()


# heading for shipping frame
lbl_heading_shipping = tk.Label(shipping_frame,
                                text='Shipping details',
                                font=font_large,
                                bg='gray20',
                                fg='white')


# pack heading
lbl_heading_shipping.pack()
# forename heading
forename_heading = tk.Label(shipping_frame,
                            text='Forename',
                            font=font_small,
                            bg='gray20',
                            fg='white')
# pack heading
forename_heading.pack()
# forename entry
forename_entry = tk.Entry(shipping_frame)
# pack forename entry
forename_entry.pack()
# surname heading
surname_heading = tk.Label(shipping_frame,
                           text='Surname',
                           font=font_small,
                           bg='gray20',
                           fg='white')
# pack heading
surname_heading.pack()
# surname entry
surname_entry = tk.Entry(shipping_frame)
# pack surname entry
surname_entry.pack()
# postcode heading
postcode_heading = tk.Label(shipping_frame,
                            text='Post code',
                            font=font_small,
                            bg='gray20',
                            fg='white')
# pack heading
postcode_heading.pack()
# postcode entry
postcode_entry = tk.Entry(shipping_frame)
# pack postcode entry
postcode_entry.pack()
# house number heading
house_number_heading = tk.Label(shipping_frame,
                                text='House number',
                                font=font_small,
                                bg='gray20',
                                fg='white')
# pack heading
house_number_heading.pack()
# house number entry
house_number_entry = tk.Entry(shipping_frame)
# pack entry
house_number_entry.pack()
# county/city heading
county_city_heading = tk.Label(shipping_frame,
                               text='County/City',
                               font=font_small,
                               bg='gray20',
                               fg='white')
# pack heading
county_city_heading.pack()
# county/city entry
county_city_entry = tk.Entry(shipping_frame)
# pack entry
county_city_entry.pack()
# town heading
town_heading = tk.Label(shipping_frame,
                        text='Town',
                        font=font_small,
                        bg='gray20',
                        fg='white')
# pack heading
town_heading.pack()
# town entry
town_entry = tk.Entry(shipping_frame)
# pack entry
town_entry.pack()

# button to continue to receipt frame
btn_continue_to_receipt = tk.Button(shipping_frame,
                                    text='View receipt',
                                    font=font_small,
                                    bg='gray10',
                                    fg='white',
                                    command=continue_to_receipt)
# pack button
btn_continue_to_receipt.pack()

# button to switch back to basket frame
btn_back_to_basket = tk.Button(shipping_frame,
                               text='Back to basket',
                               font=font_small,
                               bg='gray10',
                               fg='white',
                               command=back_to_basket)
# pack button
btn_back_to_basket.pack()

# heading for receipt frame
lbl_heading_receipt = tk.Label(receipt_frame,
                               text='Receipt',
                               font=font_large,
                               bg='gray20',
                               fg='white')

# pack heading
lbl_heading_receipt.pack()

# button to print receipt
btn_print_receipt = tk.Button(receipt_frame,
                              text='Print receipt',
                              font=font_small,
                              bg='gray10',
                              fg='white',
                              command=print_receipt)
# pack button
btn_print_receipt.pack()

# button to switch back to shipping frame
btn_back_to_shipping = tk.Button(receipt_frame,
                                 text='Back to shipping details',
                                 font=font_small,
                                 bg='gray10',
                                 fg='white',
                                 command=back_to_shipping)

# pack button
btn_back_to_shipping.pack()

# receipt
receipt_forename = tk.Label(receipt_frame,
                            font=font_small,
                            bg='gray10',
                            fg='white')

# pack label
receipt_forename.pack()

receipt_surname = tk.Label(receipt_frame,
                           font=font_small,
                           bg='gray10',
                           fg='white')

# pack label
receipt_surname.pack()

receipt_postcode = tk.Label(receipt_frame,
                            font=font_small,
                            bg='gray10',
                            fg='white')

# pack label
receipt_postcode.pack()

receipt_house_number = tk.Label(receipt_frame,
                                font=font_small,
                                bg='gray10',
                                fg='white')

# pack label
receipt_house_number.pack()

receipt_county_city = tk.Label(receipt_frame,
                               font=font_small,
                               bg='gray10',
                               fg='white')

# pack label
receipt_county_city.pack()

receipt_town = tk.Label(receipt_frame,
                        font=font_small,
                        bg='gray10',
                        fg='white')

# pack label
receipt_town.pack()


root.mainloop()
