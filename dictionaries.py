# ========================================
# =============|| Task 1 ||===============
# ========================================

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverageges"] = ["Juice", "Coca-cola", "Sparkling Water"]
restaurant_menu["Main Course"]["Steak"] = 17.99
restaurant_menu["Starters"].pop("Bruschetta")

print(restaurant_menu)



# ========================================
# =============|| Task 2 ||===============
# ========================================

# ======= Functions ======== 

service_tickets = {}

def add_ticket(tickets):
  ticket = {}
  customer = input("What is the customer name? ")
  issue = input("What is the customer issue? ")
  # status of ticket set to 'Open' by default 
  status = "open"
  ticket["customer"] = customer
  ticket["issue"] = issue
  ticket["status"] = status
  
  # Gets the number part of last item and assign id based on that value (+1)
  id = None
  if len(service_tickets) > 0:
    last_id = int(list(service_tickets.keys())[-1].split("-")[1])
    id = last_id + 1 
  else:
    id = 1
  
  tickets[f"Ticket-{id}"] = ticket
  
  print("\033[94m", service_tickets, "\033[0m")   
  
  
# By updating I assume function toggles the status of the targeted ticket.    
def update_ticket(tickets):
    id = input("Enter the id of ticket you want to update? ")
    status = tickets[id]["status"]
    if status == "open":
      tickets[id]["status"] = "closed"
    else:
      tickets[id]["status"] = "open"  
  
  
def display_tickets(tickets):
  filter_criteria = input("Enter 'all' to view all tickets, Enter 'open' to view tickets with open status, 'closed' to view tickets with closed status: ") 
  
  if filter_criteria == 'all':
    print("\033[93m", tickets, "\033[0m") 
    
  elif filter_criteria == 'open':
    filtered_dict = {}
    for k,v in tickets.items():
      if v['status'] == 'open':
          filtered_dict.update({k: v})
    print("\033[93m", filtered_dict, "\033[0m")       
        
  elif filter_criteria == 'closed':
    filtered_dict = {}
    for k,v in tickets.items():
      if v['status'] == 'closed':
          filtered_dict.update({k: v})
    print("\033[93m", filtered_dict, "\033[0m")   
  
  
# ====================== Run App ==================== 
def manage_tickets():
  while True:
    action = input("Choose action: \nadd \nupdate \ndisplay \nquit\n: ")
    if action == 'add':
      add_ticket(service_tickets)
      
    elif action == 'update':
      update_ticket(service_tickets) 
    
    elif action == 'display':
       display_tickets(service_tickets)
     
    elif action == 'quit':
      break  
    
    else:
      print('Invalid Action')
  
  print("\033[96m", service_tickets, "\033[0m")   
  
  
  
manage_tickets()
  