from pathlib import Path


path = Path(
    r"C:\laragon\www\module-test\Modules\Admin\resources\views\dashboard\crm-dashboard.blade.php"
)
text = path.read_text(encoding="utf-8")

start_marker = "<!-- Content -->"
end_marker = "<!-- / Content -->"

if start_marker in text and end_marker in text:
    start_index = text.index(start_marker) + len(start_marker)
    end_index = text.index(end_marker, start_index)
    content = text[start_index:end_index].strip()
    content = content.replace("../../assets/", "{{ asset('assets/assets') }}/")

    new_text = (
        "@extends('admin::components.layouts.master')\n"
        "@section('title', 'Demo: Dashboard - CRM | Vuexy - Bootstrap Dashboard PRO')\n"
        "@section('content')\n"
        f"{content}\n"
        "@endsection\n"
        "\n"
        "@push('page-scripts')\n"
        "<script src=\"{{ asset('assets/assets') }}/js/dashboards-crm.js\"></script>\n"
        "@endpush\n"
    )

    path.write_text(new_text, encoding="utf-8")
else:
    path.write_text(
        text.replace("../../assets/", "{{ asset('assets/assets') }}/"),
        encoding="utf-8",
    )
