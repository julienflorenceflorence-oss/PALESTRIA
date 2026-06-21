import requests
import json
import time

# Configuration
BASE_URL = "http://localhost:4747"
# URL de votre n8n LOCAL (configurée d'après votre lien)
N8N_WEBHOOK_URL = "http://localhost:5678/webhook/agent-appointment"

def run_test():
    print("--- Démarrage du Test d'Agenda Automatisé ---")

    # 1. Création d'une session pour le prospect
    print("\n1. Simulation d'un prospect arrivant sur le site...")
    session_data = {
        "url": "https://happy-house.fr/contact",
        "projectId": "PROJET_TEST_AGENDA"
    }
    try:
        res = requests.post(f"{BASE_URL}/sessions", json=session_data)
        session = res.json()
        session_id = session['id']
        print(f"   OK : Session créée avec l'ID : {session_id}")
    except Exception as e:
        print(f"   ERREUR : Le serveur n'est pas lancé sur {BASE_URL}. Lancez 'npm run dev' ou votre serveur node.")
        return

    # 2. Simulation d'une demande de rendez-vous par l'Agent IA
    print("\n2. L'Agent IA qualifie le prospect et propose un créneau...")
    appointment_data = {
        "sessionId": session_id,
        "prospectName": "Jean Dupont",
        "prospectEmail": "jean.dupont@example.com",
        "startTime": "2026-03-27T14:00:00Z",
        "endTime": "2026-03-27T14:30:00Z",
        "notes": "Intéressé par l'automatisation de sa gestion locative Happy House."
    }

    print("   Envoi de la demande de RDV au système local...")
    try:
        res = requests.post(f"{BASE_URL}/sessions/{session_id}/appointments", json=appointment_data)
        if res.status_code == 201:
            appt = res.json()
            print(f"   SUCCÈS : Rendez-vous enregistré localement (ID: {appt['id']})")
            print("   INFO : Le système tente maintenant d'envoyer le Webhook à n8n...")
        else:
            print(f"   ERREUR : Statut {res.status_code} - {res.text}")
    except Exception as e:
        print(f"   ERREUR : Impossible de contacter l'API appointments.")

    # 3. Vérification dans la base de données (via l'API)
    print("\n3. Vérification de l'historique des rendez-vous...")
    try:
        res = requests.get(f"{BASE_URL}/sessions/{session_id}/appointments")
        appts = res.json()
        if len(appts) > 0:
            print(f"   OK : {len(appts)} rendez-vous trouvé(s) en base SQLite pour cette session.")
        else:
            print("   ERREUR : Aucun rendez-vous trouvé en base.")
    except Exception as e:
        print(f"   ERREUR lors de la lecture des rendez-vous.")

    print("\n--- Test Terminé ---")
    print(f"\nPROCHAINE ÉTAPE : Assurez-vous d'avoir importé le workflow sur {N8N_WEBHOOK_URL}")
    print("pour que Jean Dupont reçoive son email de confirmation !")

if __name__ == "__main__":
    run_test()
