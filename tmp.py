from pathlib import Path 
dq=chr(34) 
dashboard_path=Path('C:/laragon/www/module-test/Modules/Admin/resources/views/dashboard/dashboard.blade.php') 
master_path=Path('C:/laragon/www/module-test/Modules/Admin/resources/views/components/layouts/master.blade.php') 
text=dashboard_path.read_text(encoding='utf-8') 
text=text.replace('../../assets/','{{ asset('+dq+'assets'+dq+') }}/') 
marker_start='<!-- Content -->' 
marker_end='<!-- / Content -->' 
prefix,rest=text.split(marker_start,1) 
content,suffix=rest.split(marker_end,1) 
yield_content='@yield('+dq+'content'+dq+')' 
master=prefix+marker_start+'\n            '+yield_content+'\n            '+marker_end+suffix 
master=master.replace('<title>Demo: Dashboard - Analytics | Vuexy - Bootstrap Dashboard PRO</title>','<title>@yield('+dq+'title'+dq+', '+dq+'Dashboard - Analytics'+dq+')</title>') 
master_path.write_text(master,encoding='utf-8') 
content_clean=content.strip('\\n') 
dashboard_view=('@extends('+dq+'admin::components.layouts.master'+dq+')\\n\\n'+'@section('+dq+'title'+dq+', '+dq+'Demo: Dashboard - Analytics | Vuexy - Bootstrap Dashboard PRO'+dq+')\\n\\n'+'@section('+dq+'content'+dq+')\\n'+content_clean+'\\n@endsection\\n') 
dashboard_path.write_text(dashboard_view,encoding='utf-8') 
