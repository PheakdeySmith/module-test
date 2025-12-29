from pathlib import Path 
path=Path('C:/laragon/www/module-test/Modules/Admin/resources/views/dashboard/dashboard.blade.php') 
text=path.read_text(encoding='utf-8') 
text=text.replace('asset(\"assets\")','asset(\"assets/assets\")') 
path.write_text(text,encoding='utf-8') 
