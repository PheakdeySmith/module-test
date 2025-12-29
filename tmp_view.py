from pathlib import Path 
path=Path('C:/laragon/www/module-test/Modules/Admin/resources/views/components/layouts/master.blade.php') 
lines=path.read_text(encoding='utf-8').splitlines() 
for i,l in enumerate(lines,1): 
    if 'asset(' in l: print(f\"{i}: {l}\") 
