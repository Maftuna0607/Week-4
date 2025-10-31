def calculate_tickets_value(ticket_type, tickets, priority_level):
    total_value=0
    if ticket_type=="technical":
        if priority_level=="low":
            value=20
        elif priority_level=="medium":
            value=35
        else:
            value=55
    elif ticket_type=="billing":
        if priority_level=="low":
            value=15
        elif priority_level=="medium":
            value=25
        else:
            value=40
    else:
        if priority_level=="low":
            value=10
        elif priority_level=="medium":
            value=18
        else:
            value=28
    total_value=tickets*value
    return total_value
def calculate_resolution_efficiency(agent_quarters, baseline_tickets, resolved_tickets):
    expected_t=1000+(agent_quarters*100)
    capacity=expected_t-baseline_tickets
    efficiency_percentage=(resolved_tickets-baseline_tickets)/capacity*100
    return efficiency_percentage
def determine_performance_level(efficiency_percent):
    if efficiency_percent<50:
        return "Developing Level"
    elif efficiency_percent<60:
        return "Competent Level"
    elif efficiency_percent<70:
        return "Proficient Level"
    elif efficiency_percent<85:
        return "Advanced Level"
    else:
        return "Expert Level"
def calculate_performance_bonus(value, tickets, level_multiplier):
    base_bonus= value*0.05+tickets*2
    if level_multiplier=="Developing Level":
        bonus=0.5
    elif level_multiplier=="Advanced Level":
        bonus=1.5
    elif level_multiplier=="Proficient Level":
        bonus=1.2
    elif level_multiplier=="Competent Level":
        bonus=1.0 
    elif level_multiplier=="Expert Level":
        bonus=1.8   
    final_bonus=base_bonus*bonus
    return round(final_bonus,1)
def needs_additional_training(service_weeks, total_tickets, efficiency_percentage):
    if service_weeks>=6 and efficiency_percentage<50:
        return True
    elif total_tickets<100 and efficiency_percentage<60:
        return True
    elif service_weeks>=4 and efficiency_percentage<40:
        return True
    else:
        return False
def generate_quality_report(agent_name, ticket_type, tickets, priority_level, 
                            agent_quarters, baseline_tickets,tickets_resolved, service_weeks):
    total_value=calculate_tickets_value(ticket_type, tickets, priority_level)
    efficiency_percent=calculate_resolution_efficiency(agent_quarters, baseline_tickets, tickets_resolved)
    performance_level=determine_performance_level(efficiency_percent)
    performance_bonus=calculate_performance_bonus(total_value, tickets, performance_level)
    additional_training=needs_additional_training(service_weeks, tickets, efficiency_percent)

    print(f"CUSTOMER SERVICE QUALITY MONITOR\n========================================")
    print(f"Quality Report For:{agent_name}")
    print(f"----------------------------------------")
    print(f"Ticket Type: {ticket_type}")
    print(f"Tickets Resolved: {tickets}")
    print(f"Priority Level: {priority_level}")
    print(f"Tickets Value: ${total_value}")
    print(f"Efficiency Analysis: ")
    print(f"  Experience: {agent_quarters} quarters, Baseline: {baseline_tickets}, Resolved Tickets: {tickets_resolved}")
    print(f"  Efficiency: {efficiency_percent}%")
    print(f"  Performance Level: {performance_level}")
    print(f"Performance Bonus: ${performance_bonus}")
    print(f"Service Weeks: {service_weeks}")
    print(f"Additional Training Needed: {'Yes' if additional_training else 'No'}")
    print(f"========================================")
generate_quality_report("Harper", "technical", 45, "high", 3,800, 1150, 3)
generate_quality_report("Jesse", "general", 30,"low",8, 850, 950, 7)