import os
import json
import re
import sys
import time
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

languages = {
    "pt": {
        "choose_language": "Escolha seu idioma:",
        "language_options": ["1. Português Brasileiro", "2. English", "3. Español"],
        "language_prompt": "Digite sua escolha (1-3): ",
        "invalid_language_option": "Opção inválida. Escolhendo Inglês como padrão.",
        "menu_title": "Ferramenta por Whatify | Adaptado para Python por tom4tee | Traduzido por nozkel",
        "menu_options": [
            "1. Adicionar conta",
            "2. Remover contas",
            "3. Visualizar contas instaladas",
            "4. Sair do programa"
        ],
        "input_option": "Insira sua opção: ",
        "invalid_option": "Sua escolha é inválida. Por favor, escolha uma opção entre 1-4.",
        "exiting": "Saindo do programa...",
        "press_to_continue": "Pressione ENTER para retornar ao menu...",
        "remove_menu_title": "Escolha o tipo de remoção:",
        "remove_menu_options": [
            "1. Remover todas as contas",
            "2. Remover contas Piratas (accessToken não é um UUID)",
            "3. Remover contas Premium (accessToken é um UUID)"
        ],
        "input_remove_option": "Insira sua opção: ",
        "invalid_remove_option": "Sua escolha é inválida. Retornando ao menu.",
        "username_prompt": "Insira o nome de usuário desejado: ",
        "invalid_username_warning": "Seu nome de usuário é inválido, você pode presenciar problemas ao entrar em servidores.",
        "uuid_prompt": "Insira um UUID válido: ",
        "invalid_uuid_warning": "O UUID inserido é inválido. Por favor, certifique-se de que o UUID está no formato correto.",
        "retry_prompt": "Você gostaria de tentar novamente? (s/n): ",
        "returning_to_menu": "Retornando ao menu principal.",
        "success_created": "Sua conta foi criada com sucesso.",
        "success_removed_all": "Todas as contas foram removidas com sucesso.",
        "success_removed_cracked": "Todas as contas Piratas foram removidas com sucesso.",
        "success_removed_premium": "Todas as contas Premium foram removidas com sucesso.",
        "installed_accounts": "Contas instaladas:",
        "failed_load": "Falha ao carregar arquivo de contas: ",
        "check_lunar": "Por favor, verifique se você tem Lunar Client instalado.",
        "save_failed": "Falha ao salvar arquivo de contas: ",
        "success_save": "Contas foram salvas com sucesso."
    },
    "en": {
        "choose_language": "Choose your language:",
        "language_options": ["1. Português Brasileiro", "2. English", "3. Español"],
        "language_prompt": "Type your option (1-3): ",
        "invalid_language_option": "Invalid option. Defaulting to English.",
        "menu_title": "Tool by Whatify | Ported to Python by tom4tee",
        "menu_options": [
            "1. Create Account",
            "2. Remove Accounts",
            "3. View Installed Accounts",
            "4. Exit the program"
        ],
        "input_option": "Please type your option (1-4) here: ",
        "invalid_option": "Your choice is invalid. Please pick an option (1-4).",
        "exiting": "Exiting the program.",
        "press_to_continue": "Press Enter to return to the main menu...",
        "remove_menu_title": "Choose an option to remove accounts:",
        "remove_menu_options": [
            "1. Remove All Accounts",
            "2. Remove Cracked Accounts (accessToken is not a UUID)",
            "3. Remove Premium Accounts (accessToken is a UUID)"
        ],
        "input_remove_option": "Please type your option (1-3) here: ",
        "invalid_remove_option": "Invalid option. Returning to main menu.",
        "username_prompt": "Enter your desired username: ",
        "invalid_username_warning": "You may experience issues joining servers because of your username being invalid.",
        "uuid_prompt": "Enter a valid UUID: ",
        "invalid_uuid_warning": "The UUID you entered is invalid. Please ensure it follows the correct format.",
        "retry_prompt": "Would you like to try again? (y/n): ",
        "returning_to_menu": "Returning to main menu.",
        "success_created": "Your account has successfully been created.",
        "success_removed_all": "All accounts have been successfully removed.",
        "success_removed_cracked": "Cracked accounts have been successfully removed.",
        "success_removed_premium": "Premium accounts have been successfully removed.",
        "installed_accounts": "Installed Accounts:",
        "failed_load": "Failed to load accounts file: ",
        "check_lunar": "Please check that you have Lunar Client installed.",
        "save_failed": "Failed to save accounts file: ",
        "success_save": "Accounts have been saved successfully."
    },
    "es": {
        "choose_language": "Elige tu idioma:",
        "language_options": ["1. Português Brasileiro", "2. English", "3. Español"],
        "language_prompt": "Escribe tu opción (1-3): ",
        "invalid_language_option": "Opción inválida. Configurando idioma a inglés.",
        "menu_title": "Herramienta por Whatify | Porteado a Python por tom4tee",
        "menu_options": [
            "1. Crear cuenta",
            "2. Eliminar cuentas",
            "3. Ver cuentas instaladas",
            "4. Salir del programa"
        ],
        "input_option": "Escribe tu opción (1-4) aquí: ",
        "invalid_option": "Opción inválida. Elige una opción (1-4).",
        "exiting": "Saliendo del programa.",
        "press_to_continue": "Presiona Enter para volver al menú principal...",
        "remove_menu_title": "Elige una opción para eliminar cuentas:",
        "remove_menu_options": [
            "1. Eliminar todas las cuentas",
            "2. Eliminar cuentas cracked (accessToken no es UUID)",
            "3. Eliminar cuentas premium (accessToken es UUID)"
        ],
        "input_remove_option": "Escribe tu opción (1-3) aquí: ",
        "invalid_remove_option": "Opción inválida. Volviendo al menú principal.",
        "username_prompt": "Ingresa el nombre de usuario deseado: ",
        "invalid_username_warning": "Podrías tener problemas al unirte a servidores porque tu nombre de usuario es inválido.",
        "uuid_prompt": "Ingresa un UUID válido: ",
        "invalid_uuid_warning": "El UUID ingresado es inválido. Asegúrate de que siga el formato correcto.",
        "retry_prompt": "¿Quieres intentarlo de nuevo? (s/n): ",
        "returning_to_menu": "Volviendo al menú principal.",
        "success_created": "Tu cuenta se creó con éxito.",
        "success_removed_all": "Todas las cuentas se eliminaron con éxito.",
        "success_removed_cracked": "Las cuentas cracked se eliminaron con éxito.",
        "success_removed_premium": "Las cuentas premium se eliminaron con éxito.",
        "installed_accounts": "Cuentas instaladas:",
        "failed_load": "Error al cargar el archivo de cuentas: ",
        "check_lunar": "Asegúrate de tener Lunar Client instalado.",
        "save_failed": "Error al guardar el archivo de cuentas: ",
        "success_save": "Las cuentas se han guardado correctamente."
    }
}

# language variable
selected_language = None

def choose_language():
    global selected_language
    print(languages["en"]["choose_language"] if selected_language is None else "")
    for option in languages["en"]["language_options"]:
        print(option)
    choice = input(languages["en"]["language_prompt"]).strip()
    if choice == "1":
        selected_language= "pt"
    elif choice == "2":
        selected_language = "en"
    elif choice == "3":
        selected_language = "es"
    else:
        print(Fore.RED + languages["en"]["invalid_language_option"])
        selected_language = "en"

    if selected_language == "es":
        print(languages["es"]["choose_language"])
        for option in languages["es"]["language_options"]:
            print(option)
    elif selected_language == "pt":
        print(languages["pt"]["choose_language"])
        for option in languages["pt"]["language_options"]:
            print(option)
    else:
        print(languages["en"]["choose_language"])
        for option in languages["en"]["language_options"]:
            print(option)

def get_text(key):
    return languages[selected_language][key]

# Validation functions Thing
def is_valid_minecraft_username(username):
    if len(username) < 3 or len(username) > 16:
        return False
    pattern = r"^[a-zA-Z0-9_]+$"
    return bool(re.match(pattern, username))

def is_valid_uuid(uuid):
    pattern = r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
    return bool(re.match(pattern, uuid))

# Thing
def print_with_color(info, text, color):
    timestamp = datetime.now().strftime("%H:%M:%S")
    info_text = f" [{timestamp}] > [{info}] {text}"
    print(color + info_text + Style.RESET_ALL)

def print_line_with_color(info, text, color):
    timestamp = datetime.now().strftime("%H:%M:%S")
    info_text = f" [{timestamp}] > [{info}] {text}"
    print(color + info_text + Style.RESET_ALL)

class AccountManager:
    json_data = {}
    user_folder = os.path.expanduser("~")
    lunar_accounts_path = os.path.join(user_folder, ".lunarclient", "settings", "game", "accounts.json")

    @classmethod
    def create_account(cls, username, uuid):
        new_account = {
            "accessToken": uuid,
            "accessTokenExpiresAt": "2050-07-02T10:56:30.717167800Z",
            "eligibleForMigration": False,
            "hasMultipleProfiles": False,
            "legacy": True,
            "persistent": True,
            "userProperites": [],
            "localId": uuid,
            "minecraftProfile": {"id": uuid, "name": username},
            "remoteId": uuid,
            "type": "Xbox",
            "username": username,
        }

        cls.json_data["accounts"][uuid] = new_account
        print_line_with_color("SUCCESS", get_text("success_created"), Fore.CYAN)

    @classmethod
    def remove_all_accounts(cls):
        cls.json_data["accounts"] = {}
        print_line_with_color("SUCCESS", get_text("success_removed_all"), Fore.CYAN)

    @classmethod
    def remove_cracked_accounts(cls):
        accounts_to_remove = [
            uuid for uuid, account in cls.json_data["accounts"].items()
            if not is_valid_uuid(account["accessToken"])
        ]
        for uuid in accounts_to_remove:
            del cls.json_data["accounts"][uuid]
        print_line_with_color("SUCCESS", get_text("success_removed_cracked"), Fore.CYAN)

    @classmethod
    def remove_premium_accounts(cls):
        accounts_to_remove = [
            uuid for uuid, account in cls.json_data["accounts"].items()
            if is_valid_uuid(account["accessToken"])
        ]
        for uuid in accounts_to_remove:
            del cls.json_data["accounts"][uuid]
        print_line_with_color("SUCCESS", get_text("success_removed_premium"), Fore.CYAN)

    @classmethod
    def view_installed_accounts(cls):
        print_line_with_color("INFO", get_text("installed_accounts"), Fore.CYAN)
        if not cls.json_data["accounts"]:
            print_line_with_color("INFO", " - " + ("No accounts found." if selected_language == "en" else "Nenhuma conta encontrada." if selected_language == "pt" else "No se encontraron cuentas."), Fore.YELLOW)
            return
        for uuid, account in cls.json_data["accounts"].items():
            print_line_with_color("ACCOUNT", f"{uuid}: {account['username']}", Fore.GREEN)

    @classmethod
    def load_json(cls):
        try:
            if os.path.exists(cls.lunar_accounts_path):
                with open(cls.lunar_accounts_path, "r") as file:
                    cls.json_data = json.load(file)
            else:
                cls.json_data = {"accounts": {}}
        except Exception as e:
            print_line_with_color("ERROR", get_text("failed_load") + str(e), Fore.RED)
            print_line_with_color("NOTICE", get_text("check_lunar"), Fore.RED)
            print_line_with_color("NOTICE", get_text("exiting"), Fore.RED)
            time.sleep(3)
            sys.exit(1)

    @classmethod
    def save_json(cls):
        try:
            os.makedirs(os.path.dirname(cls.lunar_accounts_path), exist_ok=True)
            with open(cls.lunar_accounts_path, "w") as file:
                json.dump(cls.json_data, file, indent=4)
            print_line_with_color("SUCCESS", get_text("success_save"), Fore.CYAN)
        except Exception as e:
            print_line_with_color("ERROR", get_text("save_failed") + str(e), Fore.RED)

# Main program functions
def main_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print_with_color("INFO", get_text("menu_title"), Fore.BLUE)
        for option in get_text("menu_options"):
            print_with_color("OPTION", option, Fore.GREEN)
        print_with_color("INPUT", get_text("input_option"), Fore.BLUE)
        
        try:
            choice = int(input().strip())
            if choice == 1:
                create_account_prompt()
            elif choice == 2:
                remove_accounts_menu()
            elif choice == 3:
                AccountManager.view_installed_accounts()
            elif choice == 4:
                print_line_with_color("INFO", get_text("exiting"), Fore.CYAN)
                break
            else:
                print_line_with_color("ERROR", get_text("invalid_option"), Fore.RED)
        except ValueError:
            print_line_with_color("ERROR", get_text("invalid_option"), Fore.RED)
        except Exception as e:
            print_line_with_color("ERROR", f"An error occurred: {e}", Fore.RED)

        print_line_with_color("INFO", get_text("press_to_continue"), Fore.CYAN)
        input()

def create_account_prompt():
    print_with_color("INPUT", get_text("username_prompt"), Fore.BLUE)
    username = input().strip()
    if not is_valid_minecraft_username(username):
        print_line_with_color("WARNING", get_text("invalid_username_warning"), Fore.RED)

    while True:
        print_with_color("INPUT", get_text("uuid_prompt"), Fore.BLUE)
        uuid = input().strip()
        if not is_valid_uuid(uuid):
            print_line_with_color("WARNING", get_text("invalid_uuid_warning"), Fore.RED)
            retry = input(get_text("retry_prompt")).strip().lower()
            if selected_language == "es":
                if retry == "n":
                    print_line_with_color("INFO", get_text("returning_to_menu"), Fore.CYAN)
                    return
            else:
                if retry == "n":
                    print_line_with_color("INFO", get_text("returning_to_menu"), Fore.CYAN)
                    return
        else:
            AccountManager.create_account(username, uuid)
            AccountManager.save_json()
            break

def remove_accounts_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print_line_with_color("INFO", get_text("remove_menu_title"), Fore.BLUE)
    for option in get_text("remove_menu_options"):
        print_line_with_color("OPTION", option, Fore.GREEN)
    print_with_color("INPUT", get_text("input_remove_option"), Fore.BLUE)

    try:
        choice = int(input().strip())
        if choice == 1:
            AccountManager.remove_all_accounts()
        elif choice == 2:
            AccountManager.remove_cracked_accounts()
        elif choice == 3:
            AccountManager.remove_premium_accounts()
        else:
            print_line_with_color("ERROR", get_text("invalid_remove_option"), Fore.RED)
    except ValueError:
        print_line_with_color("ERROR", get_text("invalid_remove_option"), Fore.RED)
    except Exception as e:
        print_line_with_color("ERROR", f"An error occurred: {e}", Fore.RED)

    AccountManager.save_json()

def main():
    choose_language()
    AccountManager.load_json()
    main_menu()
    AccountManager.save_json()

if __name__ == "__main__":
    main()
