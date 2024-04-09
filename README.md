Aby odpalić venv trzeba uzyc komendy
.venv\Scripts\Activate
Aby wyłaczyć wystarczy wpissać deactivate


Aby zastartowac projecta django trzeba wejsc do folderu z projektem: 
"cd CMS_website" 
nastepnie wpisujemy "python manage.py runserver"


settings
STATIC_URL tu znajduja sie CSS, JavaScript i obrazy  
LANGUAGE_CODE i TIME_ZONE: Ustawienia lokalizacji i strefy czasowej dla projektu.
DATABASES: Słownik konfiguracji baz danych
TEMPLATES: Konfiguracja systemu szablonów Django
ROOT_URLCONF: Ścieżka do modułu URLconf głównego projektu, sluzy do przekierowania żądań HTTP do odpowiednich widoków na podstawie URL.
INSTALLED_APPS: Lista aplikacji, które są włączone w projekcie.

URL
URLi pozwalają na uporządkowane mapowanie adresów internetowych
na logikę aplikacji. Każdy adres URL może prowadzić do innego
widoku.

WSGI  
jest interfejsem w który definiuje sposób komunikacji między 
aplikacją internetową napisaną w Pythonie a serwerem internetowym, 
na którym ta aplikacja jest uruchamiana

migrations initial

Kod w pliku initial.py ma na celu przechowywanie początkowych 
migracji dla modeli danych. Migracje są mechanizmem 
w Django, który umożliwia zarządzanie zmianami struktury 
bazy danych w trakcie rozwoju aplikacji.


templates
uzytkownicy jest szablonem strony internetowej, 
który wykorzystuje Django do dynamicznego ładowania zasobów
statycznych (takich jak pliki CSS i JavaScript) oraz renderowania 
dynamicznego kodu JavaScript.


vievs
Ten widok pobiera wszystkich użytkowników z bazy danych,
przekazuje ich do szablonu HTML i zwraca odpowiedź HTTP 
zawierającą wyrenderowany szablon. Widok ten jest dostępny
pod adresem URL skonfigurowanym w aplikacji Django.

manage.py
Ten plik manage.py jest głównym punktem wejścia 
dla wielu poleceń zarządzania Django, takich jak 
uruchamianie serwera deweloperskiego, tworzenie 
migracji bazy danych, tworzenie superużytkownika itp.







