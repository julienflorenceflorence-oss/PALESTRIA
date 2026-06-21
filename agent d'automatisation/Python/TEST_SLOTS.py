from datetime import datetime, timedelta

def calculate_available_slots(existing_events):
    slots = []
    # On commence à tester à partir de lundi 30 mars 2026 pour l'exemple
    start_date = datetime(2026, 3, 30, 9, 0) 
    
    print(f"--- Simulation des créneaux 'Prestige' (9h-17h) ---")
    print(f"Règle : 20min RDV + 10min marge = 1 créneau toutes les 30min\n")

    for day_offset in range(5): # On regarde les 5 prochains jours ouvrés
        current_day = start_date + timedelta(days=day_offset)
        
        # De 9h00 à 16h30 (dernier créneau finit à 17h00)
        for hour in range(9, 17):
            for minute in [0, 30]:
                if hour == 16 and minute > 30: continue
                if hour == 17: continue

                slot_start = current_day.replace(hour=hour, minute=minute)
                slot_end = slot_start + timedelta(minutes=30)
                
                # Vérification de conflit avec les événements existants
                is_busy = False
                for event in existing_events:
                    e_start = datetime.fromisoformat(event['start'])
                    e_end = datetime.fromisoformat(event['end'])
                    # Si le créneau chevauche un événement existant
                    if (slot_start >= e_start and slot_start < e_end) or (slot_end > e_start and slot_end <= e_end):
                        is_busy = True
                        break
                
                if not is_busy:
                    slots.append(slot_start)
        
    return slots

# Simulation de votre agenda actuel (Exemple : vous avez déjà un RDV à 10h le lundi)
my_current_agenda = [
    {"summary": "RDV Client Existant", "start": "2026-03-30T10:00:00", "end": "2026-03-30T11:00:00"},
    {"summary": "Déjeuner Prestige", "start": "2026-03-30T12:30:00", "end": "2026-03-30T14:00:00"}
]

available = calculate_available_slots(my_current_agenda)

# Affichage des 10 premiers créneaux que le prospect verrait
for i, s in enumerate(available[:10]):
    print(f"Créneau {i+1} : {s.strftime('%A %d %B à %Hh%M')}")

print(f"\n... (et {len(available)-10} autres créneaux libres trouvés)")
