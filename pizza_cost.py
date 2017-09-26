





import ui

def calculate_button_touch_up_inside(sender):
    labour_cost = 0.75
    Rent_cost = 1.0
    material_cost = 0.5
    hst = 1.13
   
    diameter = float(view['diameter_input_textfield'].text)
   
    cost = (labour_cost + Rent_cost + material_cost * diameter) * hst
    view['answer_label'].text = 'The cost is: ${:,.2f}'.format(cost)
	
view = ui.load_view()
view.present('sheet')
