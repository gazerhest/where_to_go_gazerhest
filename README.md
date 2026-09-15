## How to run project

1. Create virtual env
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Apply migrations
```bash
python manage.py migrate
```
4. Run the server
```bash
python manage.py runserver
```

## Endpoints
### Where To GO
- / - Where To Go main page
- ?random=true - pick a random place from list of places
- places/ - list of places
- \<int:place_id\>/ - individual place view
- add/ - add place