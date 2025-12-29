from pathlib import Path


path = Path(
    r"C:\laragon\www\module-test\Modules\Admin\resources\views\components\layouts\master.blade.php"
)
text = path.read_text(encoding="utf-8")


def slice_between(start_marker: str, end_marker: str):
    start_index = text.index(start_marker)
    end_index = text.index(end_marker, start_index) + len(end_marker)
    return start_index, end_index, text[start_index:end_index]


head_start, head_end, head = slice_between("<head>", "</head>")
menu_start, menu_end, menu = slice_between("<!-- Menu -->", "<!-- / Menu -->")
navbar_start, navbar_end, navbar = slice_between("<!-- Navbar -->", "<!-- / Navbar -->")
footer_start, footer_end, footer = slice_between("<!-- Footer -->", "<!-- / Footer -->")

scripts_start = text.index("<!-- Core JS -->")
body_end = text.index("</body>", scripts_start)
scripts = text[scripts_start:body_end]

partials_dir = path.parent / "partials"
partials_dir.mkdir(parents=True, exist_ok=True)

(partials_dir / "head.blade.php").write_text(head, encoding="utf-8")
(partials_dir / "sidebar.blade.php").write_text(menu, encoding="utf-8")
(partials_dir / "navbar.blade.php").write_text(navbar, encoding="utf-8")
(partials_dir / "footer.blade.php").write_text(footer, encoding="utf-8")
(partials_dir / "scripts.blade.php").write_text(scripts, encoding="utf-8")

replacements = [
    (head_start, head_end, '  @include("components.layouts.partials.head")'),
    (menu_start, menu_end, '        @include("components.layouts.partials.sidebar")'),
    (navbar_start, navbar_end, '          @include("components.layouts.partials.navbar")'),
    (footer_start, footer_end, '            @include("components.layouts.partials.footer")'),
    (scripts_start, body_end, '    @include("components.layouts.partials.scripts")'),
]

new_text = text
for start, end, replacement in sorted(replacements, key=lambda item: item[0], reverse=True):
    new_text = new_text[:start] + replacement + new_text[end:]

path.write_text(new_text, encoding="utf-8")
